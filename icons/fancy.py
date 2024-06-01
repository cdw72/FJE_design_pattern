from .base import IconFamily

class FancyIconFamily(IconFamily):
    def __init__(self):
        super().__init__()
        self.icons = {
            'node': '♢',
            'leaf': '♤'
        }
