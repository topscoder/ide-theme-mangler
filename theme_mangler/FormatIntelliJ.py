
from theme_mangler.FormatInterface import FormatInterface
from theme_mangler.ThemeManglerIntermediateFormat import ThemeManglerIntermediateFormat

from yattag import Doc, indent
import json


class FormatIntelliJ(FormatInterface):

    intermediate: ThemeManglerIntermediateFormat
    src_file: str

    def __init__(self):
        self.intermediate = NotImplemented

    def add_source_file(self, src_file: str):
        self.src_file = src_file
        self.parse_to_intermediate(src_file)

    def parse_to_intermediate(self, src_file: str):
        pass

    def get_intermediate(self) -> ThemeManglerIntermediateFormat:
        return self.intermediate

    def set_intermediate(self, intmd: ThemeManglerIntermediateFormat):
        self.intermediate = intmd

    def get_src_data(self) -> str:
        pass

    def read_file(filepath: str) -> str:
        pass

    def to_output_format(self) -> str:
        doc, tag, text = Doc().tagtext()

        with tag('scheme'):
            with tag('metaInfo'):
                with tag('property', name='generator'):
                    text('ThemeMangler')
            with tag('colors'):
                source_formatter = self.get_intermediate()
                colors = source_formatter.intermediate.container['colors']

                color_options = {
                    'CARET_COLOR': colors.get('editor.foreground').strip('#')[0:6] or '',
                    'CARET_ROW_COLOR': colors.get('editor.foreground').strip('#')[0:6] or '',
                    'GUTTER_BACKGROUND': colors.get('editor.foreground').strip('#')[0:6] or '',
                    'INDENT_GUIDE': colors.get('editorIndentGuide.background').strip('#')[0:6],
                    'LINE_NUMBERS_COLOR': colors.get('editor.foreground').strip('#')[0:6] or '',
                    'SELECTED_INDENT_GUIDE': colors.get('editorIndentGuide.background').strip('#')[0:6],
                    'SELECTION_BACKGROUND': colors.get('editorIndentGuide.background').strip('#')[0:6],
                    'WHITESPACES': colors.get('editorWhitespace.foreground').strip('#')[0:6] or ''
                }

                for attr_key, attr_val in color_options.items():
                    doc.stag('option', name=attr_key, value=attr_val)

            attribute_options = {
                'TEXT': {
                    'FOREGROUND': colors.get('editor.foreground').strip('#')[0:6] or '',
                    'BACKGROUND': colors.get('editor.background').strip('#')[0:6] or ''
                },
                'BAD_CHARACTER': {
                    'FOREGROUND': colors.get('errorForeground').strip('#')[0:6] or ''
                },
                'CONSOLE_RED_OUTPUT': {
                    'FOREGROUND': colors.get('errorForeground').strip('#')[0:6] or ''
                },
                'DEFAULT_INVALID_STRING_ESCAPE': {
                    'FOREGROUND': colors.get('errorForeground').strip('#')[0:6] or ''
                },
                'BUILDOUT.LINE_COMMENT': {
                    'FOREGROUND': colors.get('descriptionForeground').strip('#')[0:6] or ''
                },
                'DEFAULT_BLOCK_COMMENT': {
                    'FOREGROUND': colors.get('descriptionForeground').strip('#')[0:6] or ''
                },
                'DEFAULT_DOC_COMMENT': {
                    'FOREGROUND': colors.get('descriptionForeground').strip('#')[0:6] or ''
                },
                'DEFAULT_DOC_COMMENT_TAG': {
                    'FOREGROUND': colors.get('descriptionForeground').strip('#')[0:6] or ''
                },
                'DEFAULT_DOC_MARKUP': {
                    'FOREGROUND': colors.get('editor.foreground').strip('#')[0:6] or ''
                },
                'DEFAULT_LINE_COMMENT': {
                    'FOREGROUND': colors.get('editor.foreground').strip('#')[0:6] or ''
                },
                'DEFAULT_OPERATION_SIGN': {
                    'FOREGROUND': colors.get('textPreformat.foreground').strip('#')[0:6] or ''
                },
                'DEFAULT_KEYWORD': {
                    'FOREGROUND': colors.get('textPreformat.foreground').strip('#')[0:6] or ''
                },
                'BUILDOUT.KEY': {
                    'FOREGROUND': colors.get('textPreformat.foreground').strip('#')[0:6] or ''
                },
                'BUILDOUT.KEY_VALUE_SEPARATOR': {
                    'FOREGROUND': colors.get('textPreformat.foreground').strip('#')[0:6] or ''
                },
                'ERRORS_ATTRIBUTES': {
                    'EFFECT_COLOR': colors.get('errorForeground').strip('#')[0:6] or '',
                    'ERROR_STRIPE_COLOR': colors.get('errorForeground').strip('#')[0:6] or ''
                },
            }

            with tag('attributes'):
                for attr_key in attribute_options:
                    with tag('option', name=attr_key):
                        with tag('value'):
                            for opt_key, opt_val in attribute_options[attr_key].items():
                                doc.stag('option', name=opt_key, value=opt_val)

        result = indent(
            doc.getvalue(),
            indentation=' ' * 2,
            newline='\r\n'
        )

        return result
