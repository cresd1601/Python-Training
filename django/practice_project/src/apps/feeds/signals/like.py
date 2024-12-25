from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

# Models
from apps.feeds import models

# Tasks
from apps.feeds import tasks


@receiver(post_save, sender=models.Like)
def created_like_signal(sender, instance, created, **kwargs):
    """
    Trigger tasks for like creation:
    - Increment the likes count in PostStatistics.
    - Notify the author of the post about the new like (only if post is liked).
    """
    if created:
        # Notify the post author, but not if the post author liked their own post
        post_id = instance.post.id
        post_tile = instance.post.title
        post_author = instance.post.user  # Get the author of the post
        like_user = instance.user  # Get the user who liked the post

        # Increment the likes count for the post
        tasks.increment_likes_count_task.delay(post_id)

        if post_author != like_user:
            # Notify the post author if the liked is by someone else
            tasks.send_notification_task.delay(
                user_id=post_author.id,
                message=f"Your post titled '{post_tile}' was liked.",
            )


@receiver(post_delete, sender=models.Like)
def deleted_like_signal(sender, instance, **kwargs):
    """
    Trigger tasks for like deletion:
    - Decrement the likes count in PostStatistics.
    """
    tasks.decrement_likes_count_task.delay(instance.post.id)
