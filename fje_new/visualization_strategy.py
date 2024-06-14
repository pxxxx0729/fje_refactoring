from abc import ABC, abstractmethod
from json_iterator import JSONIterator


class VisualizationStrategy(ABC):
    def __init__(self, icon_factory):
        self.icon_factory = icon_factory

    @abstractmethod
    def visualize(self, data: dict) -> None:
        pass


class TreeVisualizationStrategy(VisualizationStrategy):
    def _print_tree(self, data, indent="", is_last=True):
        if isinstance(data, dict):
            total_items = len(data)
            for index, (key, value) in enumerate(data.items()):
                icon = self.icon_factory.create_middle_icon()
                is_last_item = (index == total_items - 1)
                connector = "└─" if is_last_item else "├─"
                new_indent = indent + ("    " if is_last_item else "│   ")

                if isinstance(value, dict):
                    print(f"{indent}{connector} {icon} {key}")
                    self._print_tree(value, new_indent, is_last_item)
                else:
                    icon = self.icon_factory.create_leaf_icon()
                    if value is not None:
                        print(f"{indent}{connector} {icon} {key}: {value}")
                    else:
                        print(f"{indent}{connector} {icon} {key}")
        elif isinstance(data, list):
            for index, item in enumerate(data):
                is_last_item = (index == len(data) - 1)
                self._print_tree(item, indent, is_last_item)
        else:
            if data is not None:  # Skip displaying null nodes
                icon = self.icon_factory.create_leaf_icon()
                connector = "└─" if is_last else "├─"
                print(f"{indent}{connector} {icon} {data}")

    def visualize(self, data: dict) -> None:
        self._print_tree(data)


class RectangleVisualizationStrategy(VisualizationStrategy):
    def _print_rectangle(self, data, indent="", max_width=50, level=0, is_last_level=False):
        flag = 0
        if isinstance(data, dict):
            total_items = len(data)
            for index, (key, value) in enumerate(data.items()):
                is_last_item = (index == total_items - 1 and value is None)
                line_indent = self._get_line_indent(level, is_last_item)
                icon = self.icon_factory.create_middle_icon()

                if isinstance(value, dict):
                    if level == 0 and flag == 0:
                        line = f"{line_indent}┌─ {icon} {key} "
                    else:
                        line = f"{line_indent}├─ {icon} {key} "

                    if level == 0 and flag == 0:
                        flag = 1
                        print(f"{line}{'─' * (max_width - len(line))}┐")
                    else:
                        print(f"{line}{'─' * (max_width - len(line))}┤")

                    new_indent = indent + ("│   " if not is_last_item else "    ")
                    self._print_rectangle(value, new_indent, max_width, level + 1, is_last_item)
                else:
                    icon = self.icon_factory.create_leaf_icon()
                    if value is not None:
                        line = f"{line_indent}└─ {icon} {key}: {value} "
                        print(f"{line}{'─' * (max_width - len(line))}┤")
                    else:
                        if is_last_item:
                            line = f"{line_indent}└─ {icon} {key} "
                            print(f"{line}{'─' * (max_width - len(line))}┘")
                        else:
                            line = f"{line_indent}├─ {icon} {key} "
                            print(f"{line}{'─' * (max_width - len(line))}┤")
        elif isinstance(data, list):
            for item in data:
                self._print_rectangle(item, indent, max_width, level, is_last_level)
        else:
            if data is not None:
                icon = self.icon_factory.create_leaf_icon()
                line = f"{indent}└───┴─ {icon} {data} "
                print(f"{line}{'─' * (max_width - len(line))}┤")

    def _get_line_indent(self, level, is_last_item):
        if level == 0:
            return ""
        elif is_last_item:
            return "│   " * (level - 1) + "└───"
        else:
            return "│   " * level

    def visualize(self, data: dict) -> None:
        max_width = self.calculate_max_width(data)
        self._print_rectangle(data, max_width=max_width, level=0)

    def calculate_max_width(self, data, indent=""):
        max_width = 0
        if isinstance(data, dict):
            for key, value in data.items():
                if isinstance(value, dict):
                    max_width = max(max_width, len(f"{indent}┌─ {key} ") + 20)
                    max_width = max(max_width, self.calculate_max_width(value, indent + "│   "))
                else:
                    max_width = max(max_width, len(f"{indent}└─ {key}: {value} ") + 20)
        elif isinstance(data, list):
            for item in data:
                max_width = max(max_width, self.calculate_max_width(item, indent))
        else:
            if data is not None:
                max_width = max(max_width, len(f"{indent}└───┴─ {data} ") + 20)
        return max_width
