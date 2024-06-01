from .default import DefaultIconFamily
from .fancy import FancyIconFamily


class IconFactory:
    @staticmethod
    def create_icon_family(name):
        if name == 'default':
            return DefaultIconFamily().get_icons()
        elif name == 'fancy':
            return FancyIconFamily().get_icons()
        else:
            raise ValueError(f"Unknown icon family: {name}")

    @staticmethod
    def get_families():
        return ['default', 'fancy']
