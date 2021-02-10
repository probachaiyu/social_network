import logging
import urllib.error
import urllib.parse
import urllib.request
from http import HTTPStatus

from bot.config import Settings
from bot.models.user import User
from bot.service.base import BaseClient
from bot.utils import _prepare_register_data, _prepare_post_data

log = logging.getLogger(__name__)


class UserActionsClient(BaseClient):
    base_url = Settings.DOMAIN

    def auth_request(self, endpoint: str, data: dict, user: User):
        headers = {"Authorization": "Bearer " + user.access_token}
        try:
            response = self._do_request(endpoint=endpoint, data=data, headers=headers)
        except urllib.error.HTTPError as e:
            if e.code in [HTTPStatus.UNAUTHORIZED, HTTPStatus.FORBIDDEN]:
                self.renew_token(user)
                response = self.auth_request(endpoint, data, user)
        except Exception as e:
            log.exception("Request to %s. Error: %s" % (endpoint, str(e)))
            raise
        return response

    def renew_token(self, user: User) -> None:
        try:
            response = self._do_request(Settings.REFRESH_TOKEN_URL, user.refresh_token)
            user._set_new_token(response.get('access_token'))
        except urllib.error.HTTPError as e:
            self.login_user(user)

    def login_user(self, user: User):
        data = {"username": user.username, "password": user.password}
        result = self._do_request(Settings.LOGIN, data)
        return result["access_token"]

    def create_post(self, user):
        data = _prepare_post_data(user)
        response = self.auth_request(Settings.CREATE_POST, data=data, user=user)
        return response.get('id')

    def set_like(self, user: User, post_id: int):
        endpoint = Settings.LIKE
        request_url = Settings.CREATE_POST + f'{post_id}' + endpoint
        self.auth_request(request_url, data={}, user=user)

    def register_user(self):
        data, password, username = _prepare_register_data()
        response = self._do_request(Settings.REGISTER, data)
        user = User(username=username, password=password, id=response.get('user', {}).get('id'))
        user._set_new_token(response.get('access_token'))
        return user
