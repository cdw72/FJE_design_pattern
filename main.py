import argparse
import shlex
import sys
from json_parser import parse_json
from visualizer.factory import VisualizerFactory
from icons.factory import IconFactory


def process_command(command):
    # 使用argparse解析命令行参数
    parser = argparse.ArgumentParser(description='Funny JSON Explorer (FJE)')
    parser.add_argument('-f', '--file', required=True, help='Path to the JSON file')
    parser.add_argument('-s', '--style', choices=VisualizerFactory.get_styles(), default='tree',
                        help='Visualization style')
    parser.add_argument('-i', '--icon', choices=IconFactory.get_families(), default='default', help='Icon family')

    try:
        # 移除 "fje" 前缀并解析参数
        args = parser.parse_args(shlex.split(command))
        json_data = parse_json(args.file)
        # 使用工厂方法模式创建相应的Visualizer对象
        visualizer = VisualizerFactory.create_visualizer(args.style)
        # 使用抽象工厂模式创建相应的IconFamily对象
        icons = IconFactory.create_icon_family(args.icon)
        # 可视化JSON数据
        visualizer.visualize(json_data, icons)
    except SystemExit:
        print("Invalid command. Please use the format: fje -f <json file> -s <style> -i <icon family>")


def main():
    print("Welcome to Funny JSON Explorer (FJE)")
    print("Enter your command in the format: fje -f <json file> -s <style> -i <icon family>")

    while True:
        try:
            command = input()
            if command.strip().lower() in ['exit', 'quit']:
                print("Exiting Funny JSON Explorer. Goodbye!")
                break

            # 确保命令以 "fje" 开头
            if not command.startswith("fje"):
                print("Invalid command. Commands should start with 'fje'.")
                continue

            # 去掉 "fje" 前缀并处理命令
            command = command[len("fje"):].strip()
            process_command(command)
        except (EOFError, KeyboardInterrupt):
            print("\nExiting Funny JSON Explorer. Goodbye!")
            break


if __name__ == '__main__':
    main()
