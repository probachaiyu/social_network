from environs import Env

env = Env()
# Read .env into os.environ
env.read_env()


class Settings:
    DOMAIN = env.str("DOMAIN", 'localhost')
    LOGIN = env.str("LOGIN")
    REGISTER = env.str("REGISTER")
    REFRESH_TOKEN_URL = env.str("REFRESH")
    CREATE_POST = env.str("CREATE_POST")
    LIKE = env.str("LIKE")
    number_of_users = env.int("number_of_users")
    max_posts_per_user = env.int("max_posts_per_user")
    max_likes_per_user = env.int("max_likes_per_user")
