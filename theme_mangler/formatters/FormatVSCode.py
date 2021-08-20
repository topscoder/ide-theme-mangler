
from FormatInterface import ThemeManglerIntermediateFormat, FormatInterface


class FormatVSCode(FormatInterface):
    def parse_to_intermediate(self, src_data: str):
        pass

    def get_intermediate(self) -> ThemeManglerIntermediateFormat:
        pass

    def get_src_data(self) -> str:
        pass

    def read_file(filepath: str) -> str:
        pass
