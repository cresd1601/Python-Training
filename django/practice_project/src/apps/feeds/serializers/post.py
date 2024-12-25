from rest_framework import serializers

from apps.feeds.models import Post


class PostSerializer(serializers.ModelSerializer):
    """Serializer for handling Post creation, update, and listing."""

    content = serializers.CharField(required=False)
    latitude = serializers.FloatField(write_only=True)
    longitude = serializers.FloatField(write_only=True)
    author = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()
    location = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            "id",
            "category",
            "title",
            "content",
            "author",
            "latitude",
            "longitude",
            "likes_count",
            "comments_count",
            "location",
            "created",
            "modified",
        ]

    def get_author(self, obj):
        # Return the location data for the post
        return obj.author

    def get_location(self, obj):
        # Return the location data for the post
        return obj.location

    def get_likes_count(self, obj):
        # Return the location data for the post
        return obj.likes_count if obj.likes_count is not None else 0

    def get_comments_count(self, obj):
        # Return the location data for the post
        return obj.comments_count if obj.comments_count is not None else 0
