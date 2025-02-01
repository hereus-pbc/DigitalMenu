from objects.Activity import Activity


class Item(Activity):
    def __init__(self, uri: str):
        super().__init__(uri)
        self.type = 'Item'

    def _assign(self, data) -> None:
        self.name = data['name']
        self.description = data['description']
        self.price = int(data['price'])
