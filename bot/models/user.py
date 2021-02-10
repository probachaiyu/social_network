class User(object):
    username: str
    password: str
    id: int
    access_token: str or None
    refresh_token: str or None

    def __init__(self, username: str, password: str, id: int) -> None:
        super().__init__()
        self.username = username
        self.password = password
        self.id = id
        self.access_token = None
        self.refresh_token = None

    def _set_new_token(self, access_token: str) -> None:
        self.access_token = access_token
