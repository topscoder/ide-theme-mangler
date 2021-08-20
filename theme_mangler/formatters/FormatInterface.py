

import ThemeManglerIntermediateFormat


class FormatInterface: # (or maybe abstract class?)
    intermediate_result: ThemeManglerIntermediateFormat
    src_data: str

    def __init__(self):
        self.intermediate_result = NotImplemented
        self.src_data = NotImplemented

    def parse_to_intermediate(self, src_data: str):
        raise NotImplementedError

    def get_intermediate(self) -> ThemeManglerIntermediateFormat:
        raise NotImplementedError

    def get_src_data(self) -> str:
        raise NotImplementedError

    def read_file(filepath: str) -> str:
        raise NotImplementedError