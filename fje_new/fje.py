import json
import argparse
from icon_factory import PokerFaceIconFactory, NewIconFamilyFactory
from config_manager import ConfigManager
from visualization_strategy import TreeVisualizationStrategy, RectangleVisualizationStrategy

class FunnyJSONExplorer:
    def __init__(self, json_file: str, style: str, icon_family: str, config_file: str):
        self.json_file = json_file
        self.style = style
        self.icon_family = icon_family
        self.config_file = config_file

    def _load_json(self) -> dict:
        with open(self.json_file, 'r') as file:
            return json.load(file)

    def show(self):
        data = self._load_json()
        config_manager = ConfigManager(self.config_file)
        config_manager.load_config()

        if self.icon_family == "poker-face":
            icon_factory = PokerFaceIconFactory(config_manager)
        elif self.icon_family == "new-icon-family":
            icon_factory = NewIconFamilyFactory(config_manager)
        else:
            raise ValueError("Unsupported icon family")

        if self.style == "tree":
            visualizer = TreeVisualizationStrategy(icon_factory)
        elif self.style == "rectangle":
            visualizer = RectangleVisualizationStrategy(icon_factory)
        else:
            raise ValueError("Unsupported style")

        visualizer.visualize(data)

def main():
    parser = argparse.ArgumentParser(description="Funny JSON Explorer")
    parser.add_argument('-f', '--file', required=True, help='JSON file to visualize')
    parser.add_argument('-s', '--style', required=True, choices=['tree', 'rectangle'], help='Visualization style')
    parser.add_argument('-i', '--icon', required=True, help='Icon family')
    parser.add_argument('-c', '--config', default='config.json', help='Config file')

    args = parser.parse_args()

    explorer = FunnyJSONExplorer(args.file, args.style, args.icon, args.config)
    explorer.show()

if __name__ == "__main__":
    main()
