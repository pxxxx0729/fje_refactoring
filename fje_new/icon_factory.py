from abc import ABC, abstractmethod
from config_manager import ConfigManager

class IconFactory(ABC):
    @abstractmethod
    def create_middle_icon(self) -> str:
        pass

    @abstractmethod
    def create_leaf_icon(self) -> str:
        pass

class PokerFaceIconFactory(IconFactory):
    def __init__(self, config_manager: ConfigManager):
        self.config_manager = config_manager

    def create_middle_icon(self) -> str:
        return self.config_manager.get_middle_icon("poker-face")

    def create_leaf_icon(self) -> str:
        return self.config_manager.get_leaf_icon("poker-face")

class NewIconFamilyFactory(IconFactory):
    def __init__(self, config_manager: ConfigManager):
        self.config_manager = config_manager

    def create_middle_icon(self) -> str:
        return self.config_manager.get_middle_icon("new-icon-family")

    def create_leaf_icon(self) -> str:
        return self.config_manager.get_leaf_icon("new-icon-family")
