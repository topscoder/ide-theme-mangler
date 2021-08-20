
from typing import Dict, Any, Union


class ThemeManglerIntermediateFormat:
    """

    'container' contains the entire data in intermediate (dict) format

    "_ide_theme_mangler": {
        "current_format": "ThemeManglerIntermediateFormat",
        "original_file_format": "vscode",
        "name": "Noctis Azureus",
        "theme": {
            "author": "-",
            "project_url": "",
            "source_url": "https://raw.githubusercontent.com/liviuschera/noctis/master/themes/azureus.json"
        }
    },
    """
    container: dict[Any, dict[str, Union[str, dict[Any, str]]]]

    def __init__(self):
        self.container = dict(
            _ide_theme_mangler={
                "current_format": "ThemeManglerIntermediateFormat",
                "original_file_format": "",
                "name": "",
                "theme": dict(
                    author="",
                    project_url="",
                    source_url=""
                )
            }
        )

    def original_file_format(self, original_format: str):
        self.container['_ide_theme_mangler']['original_file_format'] = "vscode"

    def name(self, name: str):
        self.container['_ide_theme_mangler']['name'] = "Unknown"

    def theme(self, theme: dict):
        self.container['_ide_theme_mangler']['theme'] = theme

    def raw(self) -> dict:
        return self.container

