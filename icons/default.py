from .base import IconFamily


# 具体产品类，表示默认的图标集
class DefaultIconFamily(IconFamily):
    def get_icons(self):
        return {
            'node': ' ',
            'leaf': ' '
        }
