from rest_framework import serializers

from apps.feeds.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "created", "modified"]
