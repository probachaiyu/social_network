import logging
import os
import random
import sys

from bot.service.user_client import UserActionsClient

parent_dir = os.path.abspath(os.path.join(os.getcwd(), ""))
sys.path.append(parent_dir)


class Bot:

    def __init__(self, number_of_users: int, max_posts_per_user: int, max_likes_per_user: int) -> None:
        self.number_of_users = number_of_users
        self.max_posts_per_user = max_posts_per_user
        self.max_likes_per_user = max_likes_per_user
        self.post_ids = []
        self.client = UserActionsClient()
        self.users = []

    def create_dataset(self):
        for i in range(int(self.number_of_users)):
            user = self.client.register_user()
            self.users.append(user)
            logging.warning("User %s registered" % user.username)

            posts_number = random.randint(1, self.max_posts_per_user)
            for j in range(posts_number):
                post_id = self.client.create_post(user)
                self.post_ids.append(post_id)
            logging.warning("User {} created {} number of posts".format(user.username, posts_number))

    def perform_likes(self, users: list, post_ids: list):
        for user in users:

            logging.warning("User %s is starting make likes" % user.username)
            number_of_likes_per_user = random.randint(1, self.max_likes_per_user)
            for post_id in random.sample(post_ids, number_of_likes_per_user):
                res = self.client.set_like(
                    user=user,
                    post_id=post_id)
                logging.warning("User liked post %s", post_id)
            logging.warning("User %s made %s likes", user.username, number_of_likes_per_user)

    def run(self):
        self.create_dataset()
        self.perform_likes(self.users, self.post_ids)


if __name__ == "__main__":
    from bot.config import Settings

    bot = Bot(Settings.number_of_users, Settings.max_posts_per_user, Settings.max_likes_per_user)
    bot.run()
