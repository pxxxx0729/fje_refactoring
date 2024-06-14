class ConfigManager:
    def __init__(self, config_file):
        self.config_file = config_file
        self.icon_families = {}

    def load_config(self):
        try:
            with open(self.config_file, 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.strip()
                    if line:
                        parts = line.split()
                        if len(parts) == 3:
                            icon_family = parts[0]
                            middle_icon = parts[1]
                            leaf_icon = parts[2]
                            self.icon_families[icon_family] = {"middle_icon": middle_icon, "leaf_icon": leaf_icon}
        except FileNotFoundError:
            print(f"Config file '{self.config_file}' not found.")

    def get_middle_icon(self, icon_family):
        return self.icon_families.get(icon_family, {}).get("middle_icon", "")

    def get_leaf_icon(self, icon_family):
        return self.icon_families.get(icon_family, {}).get("leaf_icon", "")
