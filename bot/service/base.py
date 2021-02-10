import requests


class BaseClient:
    base_url = ''

    def _get_url(self, endpoint):
        return self.base_url + endpoint

    def _do_request(self, endpoint: str, data: dict, headers=None):
        request_url = self._get_url(endpoint)
        response = requests.post(request_url, data=data, headers=headers)
        return response.json()
