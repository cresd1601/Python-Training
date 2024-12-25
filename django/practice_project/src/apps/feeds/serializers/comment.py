from rest_framework import serializers

# Models
from apps.feeds.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "content", "user", "created", "modified"]
