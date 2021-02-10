from rest_framework import serializers

from social.models import Post


class PostSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    image = serializers.ImageField(required=False)
    likes_count = serializers.SerializerMethodField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def get_likes_count(self, obj):
        return obj.post_likes.count()

    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'image', 'created_at', 'updated_at', 'likes_count']
