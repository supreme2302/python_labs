import baseclass

import requests


class Friends(baseclass.BaseClient):
    BASE_URL = 'https://api.vk.com/method/'
    method = 'friends.get'


    def _get_data(self, id):
        t = requests.get(Friends.BASE_URL + Friends.method + '?user_id=' + str(id) + '&fields=bdate&v=5.62').json()
        return t

    def response_handler(self, id):
        t = self._get_data(id)
        a = t["response"]['items']

        return a