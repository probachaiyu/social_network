from dataclasses import dataclass

from social.models import PostLike, User, Post


@dataclass
class UserAction:
    user: object
    post: object


class PostLikeManager:

    def __init__(self, user: User):
        self.user = user

    def like(self, post: Post):
        PostLike.objects.create(user=self.user, post=post)
        return {"success": True, "message": "You liked the post"}

    def unlike(self, post: Post):
        PostLike.objects.filter(user=self.user, post=post).delete()
        return {"success": True, "message": "You unliked the post"}

    def like_unlike(self, post: Post):
        if self.is_post_liked(post):
            return self.unlike(post)
        else:
            return self.like(post)

    def is_post_liked(self, post: Post):
        return PostLike.objects.filter(user=self.user, post=post).exists()
