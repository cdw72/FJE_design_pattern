from visualizer.tree import TreeVisualizer
from visualizer.rectangle import RectangleVisualizer


# 工厂方法模式，定义创建Visualizer对象的接口
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
