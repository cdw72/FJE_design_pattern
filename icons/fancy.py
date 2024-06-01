from .base import IconFamily


# 具体产品类，表示花哨的图标集
class FancyIconFamily(IconFamily):
    def get_icons(self):
        return {
            'node': '♢',
            'leaf': '♤'
        }
