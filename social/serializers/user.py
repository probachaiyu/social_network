from rest_framework import serializers

from social.models import Post


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    username = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    last_login = serializers.DateTimeField(read_only=True)
    last_activity = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'username', 'email', 'last_login', 'last_activity', ]


class AnaliticSerializer(serializers.Serializer):
    user_id = serializers.CharField(required=False, read_only=True)
    post_id = serializers.CharField(required=False, read_only=True)
    likes_count = serializers.IntegerField()
