from visualizer.tree import TreeVisualizer
from visualizer.rectangle import RectangleVisualizer


class VisualizerFactory:
    @staticmethod
    def create_visualizer(style):
        if style == 'tree':
            return TreeVisualizer()
        elif style == 'rectangle':
            return RectangleVisualizer()
        else:
            raise ValueError(f"Unknown style: {style}")

    @staticmethod
    def get_styles():
        return ['tree', 'rectangle']
