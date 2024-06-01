from .base import Container, Leaf


class RectangleContainer(Container):
    def draw(self, icon_family, level=0, is_last=False, width=0, isfirst=True, the_last=""):
        if level == 1:
            if isfirst:
                prefix = '┌─' + icon_family['node']
                suffix = ' ' + '─' * (width - len(self.name) - len(prefix) - len(' ') - len('┐')) + '┐'
                print(prefix + self.name + suffix)
            else:
                prefix = '├─' + icon_family['node']
                suffix = ' ' + '─' * (width - len(self.name) - len(prefix) - len(' ') - len('┤')) + '┤'
                print(prefix + self.name + suffix)
        if level > 1:
            prefix = '│ ' + ' │ ' * (level - 2) + ' ├─' + icon_family['node']
            suffix = ' ' + '─' * (width - len(self.name) - len(prefix) - len(' ') - len('┤')) + '┤'
            print(prefix + self.name + suffix)
        for i, child in enumerate(self.children):
            child.draw(icon_family, level + 1, i == len(self.children) - 1, width, isfirst, the_last)
            if level == 0 and isfirst:
                isfirst = False


class RectangleLeaf(Leaf):
    def draw(self, icon_family, level=0, is_last=False, width=0, isfirst=False, the_last=""):
        if self.name is not the_last:
            prefix = '│ ' + ' │ ' * (level - 2) + ' ├─' + icon_family['leaf']
            suffix = ' ' + '─' * (width - len(self.name) - len(prefix) - len(' ') - len('┤')) + '┤'
        else:
            prefix = '└' + '─' * level + '┴─' + icon_family['leaf']
            suffix = ' ' + '─' * (width - len(self.name) - len(prefix) - len(' ') - len('┘')) + '┘'
        print(prefix + self.name + suffix)


# 工厂方法模式，通过VisualizerFactory创建具体的Visualizer对象
class RectangleVisualizer:
    def visualize(self, data, icon_family):
        root = self._build_tree(data)
        lines = self._collect_lines(root, icon_family)
        width = max(len(line) for line in lines) + 24
        root.draw(icon_family, width=width, the_last=lines[-1])

    def _build_tree(self, data, name='root'):
        root = RectangleContainer(name)
        for key, value in data.items():
            if isinstance(value, dict):
                root.add(self._build_tree(value, key))
            else:
                root.add(RectangleLeaf(f"{key}: {value}"))
        return root

    def _collect_lines(self, component, icon_family, level=0):
        lines = []
        for child in component.children:
            lines.append(child.name)
            if isinstance(child, Container):
                lines.extend(self._collect_lines(child, icon_family, level + 1))
        return lines
