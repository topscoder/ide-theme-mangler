
from theme_mangler.FormatInterface import FormatInterface
from theme_mangler.ThemeManglerIntermediateFormat import ThemeManglerIntermediateFormat

from yattag import Doc, indent
import json


class FormatVSCode(FormatInterface):

    intermediate: ThemeManglerIntermediateFormat
    src_file: str

    def __init__(self):
        self.intermediate = NotImplemented

    def add_source_file(self, src_file: str):
        self.src_file = src_file
        self.parse_to_intermediate(src_file)

    def parse_to_intermediate(self, src_file: str):
        fd = open(src_file, 'r')
        file_content = fd.read()

        theme_parsed = json.loads(file_content)

        intmd = ThemeManglerIntermediateFormat()

        # General info about the theme
        intmd.original_file_format("vscode")
        intmd.theme_name(theme_parsed['name'])
        intmd.theme_type(theme_parsed['type'])

        # Add colors to intermediate format
        for key, val in list(theme_parsed['colors'].items()):
            intmd.add_prop('colors', key, val)

        self.intermediate = intmd

    def get_intermediate(self) -> ThemeManglerIntermediateFormat:
        return self.intermediate

    def set_intermediate(self, intmd: ThemeManglerIntermediateFormat):
        self.intermediate = intmd

    def get_src_data(self) -> str:
        pass

    def to_output_format(self):
        # from self.intermediate_results to
        # the target format (vscode in this case)
        # prepare output dict
        result = ""
        return result

    def read_file(filepath: str) -> str:
        pass
