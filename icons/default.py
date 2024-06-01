from .base import IconFamily


class DefaultIconFamily(IconFamily):
    def __init__(self):
        super().__init__()
        self.icons = {
            'node': ' ',
            'leaf': ' '
        }
