from ..models.base import Login


class User:
    def __init__(self, item: Login):
        self.item = item

    def login(self):
        print(self.item)
        return {
            'code': 0,
            'msg': 'hello'
        }
