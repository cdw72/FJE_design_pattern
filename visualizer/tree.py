from .base import Container, Leaf


class TreeContainer(Container):
    def draw(self, icon_family, level=0, is_last=False, next_level1=True):
        if level > 0:
            prefix = ('│' if level > 1 else '') + ' ' * (level - 1) * 2 + ('└─' if is_last else '├─') \
                     + icon_family['node']
            print(prefix + self.name)
        for i, child in enumerate(self.children):
            if level == 0 and i == len(self.children) - 1:
                next_level1 = False
            child.draw(icon_family, level + 1, i == len(self.children) - 1, next_level1)


class TreeLeaf(Leaf):
    def draw(self, icon_family, level=0, is_last=False, next_level1=False):
        prefix = ('│' if level > 1 and next_level1 else '') + ' ' * (level - 1) * 2 + ('└─' if is_last else '├─') \
                 + icon_family['leaf']
        print(prefix + self.name)


# 工厂方法模式，通过VisualizerFactory创建具体的Visualizer对象
class TreeVisualizer:
    def visualize(self, data, icon_family):
        root = self._build_tree(data)
        root.draw(icon_family)

    def _build_tree(self, data, name='root'):
        root = TreeContainer(name)
        for key, value in data.items():
            if isinstance(value, dict):
                root.add(self._build_tree(value, key))
            else:
                root.add(TreeLeaf(f"{key}: {value}"))
        return root
