from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

# Models
from apps.feeds import models

# Tasks
from apps.feeds import tasks


@receiver(post_save, sender=models.Comment)
def created_comment_signal(sender, instance, created, **kwargs):
    """
    Trigger tasks for comment creation:
    - Increment the comments count in PostStatistics.
    - Notify the author of the post about the new comment (if not self-comment).
    """
    if created:
        # Increment the comments count
        tasks.increment_comments_count_task.delay(instance.post.id)

        # Check if the comment author is not the post author
        post_author = instance.post.user  # Get the post author
        comment_author = instance.user  # Get the user who made the comment

        if post_author and post_author != comment_author:
            # Notify the post author if the comment is by someone else
            tasks.send_notification_task.delay(
                user_id=post_author.id,
                message=f"Your post titled '{instance.post.title}' has a new comment.",
            )


@receiver(post_delete, sender=models.Comment)
def deleted_comment_signal(sender, instance, **kwargs):
    """
    Trigger tasks for comment deletion:
    - Decrement the comments count in PostStatistics.
    """
    if instance.is_deleted:
        tasks.decrement_comments_count_task.delay(instance.post.id)
