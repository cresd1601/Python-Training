from django.db.models.signals import post_save
from django.dispatch import receiver

# Models
from apps.feeds import models

# Tasks
from apps.feeds import tasks


@receiver(post_save, sender=models.Post)
def created_post_signal(sender, instance, created, **kwargs):
    """
    Trigger background task for creating PostStatistics when a new post is created.
    """
    if created:
        # Trigger the task to create post statistics
        models.PostStatistics.objects.create(post=instance)

    tasks.extract_and_associate_hashtags_task.delay(instance.id)
