

import theme_mangler.ThemeManglerIntermediateFormat as ThemeManglerIntermediateFormat


class FormatInterface:
    intermediate: ThemeManglerIntermediateFormat
    src_data: str

    def __init__(self):
        self.intermediate = NotImplemented
        self.src_data = NotImplemented

    def parse_to_intermediate(self, src_file: str):
        raise NotImplementedError

    def get_intermediate(self) -> ThemeManglerIntermediateFormat:
        raise NotImplementedError

    def get_src_data(self) -> str:
        raise NotImplementedError

    def read_file(filepath: str) -> str:
        raise NotImplementedError

    def to_output_format(self):
        raise NotImplementedError