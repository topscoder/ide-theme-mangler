
from theme_mangler.FormatInterface import FormatInterface
from theme_mangler.ThemeManglerIntermediateFormat import ThemeManglerIntermediateFormat
from yattag import Doc, indent


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

    def to_output_format(self):
        # from self.intermediate_results to
        # the target format (vscode in this case)
        # prepare output dict
        """
        <scheme name="Github" version="142" parent_scheme="Default">
          <metaInfo>
            <property name="created">2021-08-20T09:52:20</property>
            <property name="ide">Python</property>
            <property name="ideVersion">2021.2.0.0</property>
            <property name="modified">2021-08-20T09:52:33</property>
            <property name="originalScheme">_@user_Github</property>
          </metaInfo>
          <colors>
            <option name="CARET_COLOR" value="333333" />
        """

        node_colors = [
            {"name": "CARET_COLOR", "value": "a"},
            {"name": "CARET_ROW_COLOR", "value": "b"},
            {"name": "GUTTER_BACKGROUND", "value": "c"},
            {"name": "INDENT_GUIDE", "value": "d"},
            {"name": "LINE_NUMBERS_COLOR", "value": "e"},
            {"name": "SELECTED_INDENT_GUIDE", "value": "f"},
            {"name": "SELECTION_BACKGROUND", "value": "g"},
            {"name": "WHITESPACES", "value": "h"}
        ]

        doc, tag, text = Doc().tagtext()

        with tag('scheme'):
            with tag('metaInfo'):
                with tag('property', name='created'):
                    text('2021-08-20T09:52:20')
                with tag('property', name='ide'):
                    text('Python')
            with tag('colors'):
                for color in node_colors:
                    doc.stag('option', name=color.name, value=color.value)

        result = indent(
            doc.getvalue(),
            indentation=' ' * 2,
            newline='\r\n'
        )

        return result

    def read_file(filepath: str) -> str:
        pass
