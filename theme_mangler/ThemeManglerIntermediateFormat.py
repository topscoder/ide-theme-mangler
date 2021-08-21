
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
    "colors": {
    }
    """
    container: dict[Any, dict[str, Union[str, dict[Any, str]]]]

    def __init__(self):
        self.intermediate = None
        self.container = dict(
            _ide_theme_mangler={
                "current_format": "ThemeManglerIntermediateFormat",
                "original_file_format": "",
                "name": "",
                "theme": dict(
                    type="dark|light",
                    author="",
                    project_url="",
                    source_url=""
                )
            },
            colors={

            }
        )

    def original_file_format(self, original_format: str):
        self.container['_ide_theme_mangler']['original_file_format'] = original_format

    def theme_name(self, name: str):
        self.container['_ide_theme_mangler']['name'] = name

    def theme_type(self, theme_type: str):
        self.container['_ide_theme_mangler']['theme']['type'] = theme_type

    def add_prop(self, space: str, prop_name: str, prop_val: Any):
        self.container[space][prop_name] = prop_val

    def get_container(self):
        return self.container

    def get_properties(self, space: str) -> list:
        return list(self.container[space])

    def raw(self) -> dict:
        return self.container

