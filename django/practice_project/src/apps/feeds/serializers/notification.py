from rest_framework import serializers

# Models
from apps.feeds.models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ["id", "message"]
