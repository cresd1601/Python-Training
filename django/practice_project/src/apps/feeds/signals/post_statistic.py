from django.db.models.signals import post_save
from django.dispatch import receiver

# Models
from apps.feeds import models

# Tasks
from apps.feeds import tasks


@receiver(post_save, sender=models.PostStatistics)
def created_post_statistic_signal(sender, instance, created, **kwargs):
    """
    Trigger background task for creating PostStatistics when a new post is created.
    """
    tasks.sync_post_statistics_task.delay(instance.id)
