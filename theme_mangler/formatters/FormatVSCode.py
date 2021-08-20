
from theme_mangler.formatters.FormatInterface import FormatInterface
from theme_mangler.formatters.ThemeManglerIntermediateFormat import ThemeManglerIntermediateFormat


class FormatVSCode(FormatInterface):

    intermediate_result: ThemeManglerIntermediateFormat
    src_data: str

    def __init__(self, src_file: str):
        self.intermediate_result = NotImplemented
        self.src_file = src_file
        self.parse_to_intermediate(src_file)

    def parse_to_intermediate(self, src_file: str):
        fd = open(src_file, 'r')
        file_content = fd.read()
        self.src_data = file_content

        intmd = ThemeManglerIntermediateFormat()
        intmd.original_file_format("bla")
        intmd.theme("foo")
        intmd.name("bar")

        self.intermediate_result = intmd

    def get_intermediate(self) -> ThemeManglerIntermediateFormat:
        return self.intermediate_result

    def get_src_data(self) -> str:
        pass

    def read_file(filepath: str) -> str:
        pass
