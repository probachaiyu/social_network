POST = "post"
USER = "user"

ANALYTICS_TYPES = (
    (POST, POST),
    (USER, USER)
)

GET_USER_ANALYTICS = """SELECT 'All', 'All' FROM post_like 
WHERE (created_at BETWEEN {date_from} AND {date_to})\
{}"""
