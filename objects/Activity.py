import requests


class Activity:
    def __init__(self, uri: str):
        self._uri = uri
        self._loaded = False
        self.type = ''

    def _load(self) -> None:
        if isinstance(self._uri, str) and self._uri.startswith("https://"):
            resp = requests.get(self._uri)
            if resp.status_code != 200:
                raise Exception(resp.status_code)
            if resp.headers["Content-Type"] != "application/activity+json":
                raise TypeError(resp.headers["Content-Type"])
            data = resp.json()
        elif isinstance(self._uri, dict):
            data = self._uri
        else:
            raise TypeError(f"uri must be str or dict")
        if "https://menu.hereus.net/ns/customActivityStreams" not in data.get('@context', []):
            raise TypeError('@context')
        if data.get('type', "") != self.type:
            raise TypeError(self.type)
        if isinstance(self._uri, str) and data.get('id', '').rstrip('/') != self._uri.rstrip('/'):
            raise TypeError('uri')
        self.id = data['id']
        self._assign(data)

    def _assign(self, data: dict):
        raise NotImplementedError()

    def __getattr__(self, item) -> any:
        if not object.__getattribute__(self, '_loaded'):
            self._load()
        return object.__getattribute__(self, item)
