from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    status = serializers.CharField(read_only=True)
    likes = serializers.IntegerField(read_only=True)
    dislikes = serializers.IntegerField(read_only=True)

    class Meta:
        model = Post
        fields = "__all__"
