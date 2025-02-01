from objects.Activity import Activity
from objects.Item import Item


class Group(Activity):
    def __init__(self, uri: str):
        super().__init__(uri)
        self.type = 'Group'

    def _assign(self, data) -> None:
        self.name = data['name']
        self.description = data['description']
        self.photo = data['photo']
        self.items = [
            Item(i) for i in data['items']
        ]
