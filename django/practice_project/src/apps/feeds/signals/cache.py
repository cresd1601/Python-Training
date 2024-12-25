from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache

# Models
from apps.feeds import models


@receiver(post_save, sender=models.Post)
@receiver(post_delete, sender=models.Post)
@receiver(post_save, sender=models.Comment)
@receiver(post_delete, sender=models.Comment)
@receiver(post_save, sender=models.Like)
@receiver(post_delete, sender=models.Like)
def invalidate_cache(sender, instance, **kwargs):
    """
    Common function to invalidate cache keys when a Category or Post instance is created, updated, or deleted.
    """
    model_name = instance.__class__.__name__.lower()

    match model_name:
        case "post":
            cache.delete_pattern("posts:params:*")
            cache.delete(f"posts:{instance.id}")
        case "comment":
            cache.delete_pattern("posts:params:*")
            cache.delete(f"posts:{instance.post.id}")
            cache.delete_pattern(f"posts:{instance.post.id}:comments:params:*")
            cache.delete(f"posts:{instance.post.id}:comments:{instance.id}")
        case "like":
            cache.delete_pattern("posts:params:*")
            cache.delete(f"posts:{instance.post.id}")
        case _:
            print(f"No cache invalidation rule defined for model: {model_name}")
