from objects.Activity import Activity
from objects.Group import Group


class Menu(Activity):
    def __init__(self, uri: str):
        super().__init__(uri)
        self.type = 'Menu'

    def _assign(self, data) -> None:
        self.actor = data['actor']
        self.name = data['name']
        self.description = data['description']
        self.icon = data['icon']
        self.banner = data['banner']
        self.groups = [
            Group(i) for i in data['groups']
        ]
