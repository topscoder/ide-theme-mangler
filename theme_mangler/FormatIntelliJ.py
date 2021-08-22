
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

    def select(self, library: dict, element: str):
        if not library.get(element):
            return ''

        return library.get(element).strip('#')[0:6]

    def one_of(self, library: dict, first: str, second: str):
        if library.get(first):
            return library.get(first)

        if library.get(second):
            return library.get(second)

        return 'not found'

    def to_output_format(self) -> str:
        doc, tag, text = Doc().tagtext()

        with tag('scheme'):
            with tag('metaInfo'):
                with tag('property', name='generator'):
                    text('ThemeMangler')
                with tag('property', name='ide'):
                    text('idea')
                with tag('property', name='ideVersion'):
                    text('2019.1.0.0')
            with tag('colors'):
                source_formatter = self.get_intermediate()
                colors = source_formatter.intermediate.container['colors']

                color_options = {
                    'CARET_COLOR': self.one_of(colors, 'editorCursor.background', 'editor.foreground'),
                    'CARET_ROW_COLOR': self.select(colors, 'editor.foreground'),
                    'CONSOLE_BACKGROUND_KEY': self.one_of(colors, 'panel.background', 'sideBar.background'),
                    'GUTTER_BACKGROUND': self.one_of(colors, 'editorGutter.foreground', 'editor.foreground'),
                    'INDENT_GUIDE': self.select(colors, 'editorIndentGuide.background'),
                    'LINE_NUMBERS_COLOR': self.select(colors, 'editorLineNumber.foreground'),
                    'SELECTED_INDENT_GUIDE': self.select(colors, 'editor.lineHighlightBackground'),
                    'SELECTION_BACKGROUND': self.select(colors, 'editorIndentGuide.background'),
                    'WHITESPACES': self.select(colors, 'editorWhitespace.foreground'),
                    'ADDED_LINES_COLOR': self.select(colors, 'editorGutter.addedBackground'),
                    'ANNOTATIONS_COLOR': self.select(colors, 'variable.function'),
                    'DELETED_LINES_COLOR': self.select(colors, 'editorGutter.deletedBackground'),
                    'DIFF_SEPARATORS_BACKGROUND': self.select(colors, 'panel.background'),
                    'DOCUMENTATION_COLOR': self.select(colors, 'comment'),
                    'ERROR_HINT': self.select(colors, 'editorError.foreground'),
                    'FILESTATUS_ADDED': self.select(colors, 'gitDecoration.addedResourceForeground'),
                    'FILESTATUS_COPIED': self.select(colors, 'gitDecoration.modifiedResourceForeground'),
                    'FILESTATUS_DELETED': self.select(colors, 'gitDecoration.deletedResourceForeground'),
                    'FILESTATUS_IDEA_FILESTATUS_DELETED_FROM_FILE_SYSTEM': self.select(colors, 'gitDecoration.deletedResourceForeground'),
                    'FILESTATUS_IDEA_FILESTATUS_IGNORED': self.select(colors, 'gitDecoration.untrackedResourceForeground'),
                    'FILESTATUS_MERGED': self.select(colors, 'gitDecoration.modifiedResourceForeground'),
                    'FILESTATUS_MODIFIED': self.select(colors, 'gitDecoration.modifiedResourceForeground'),
                    'FILESTATUS_RENAMED': self.select(colors, 'gitDecoration.modifiedResourceForeground'),
                    'FILESTATUS_UNKNOWN': self.select(colors, 'gitDecoration.untrackedResourceForeground'),
                    'FILESTATUS_ADDEDOUTSIDE': self.select(colors, 'gitDecoration.addedResourceForeground'),
                    'FOLDED_TEXT_BORDER_COLOR': self.select(colors, 'sideBar.foreground'),
                    'INFORMATION_HINT': self.select(colors, 'editorOverviewRuler.infoForeground'),
                    'LINE_NUMBER_ON_CARET_ROW_COLOR': self.select(colors, 'editorLineNumber.foreground'),
                    'METHOD_SEPARATORS_COLOR': self.select(colors, 'editor.foreground'),
                    'MODIFIED_LINES_COLOR': self.select(colors, 'editorOverviewRuler.modifiedForeground'),
                    'NOTIFICATION_BACKGROUND': self.select(colors, 'notifications.background'),
                    'QUESTION_HINT': self.select(colors, 'editorOverviewRuler.infoForeground'),
                    'RECENT_LOCATIONS_SELECTION': self.select(colors, 'editorOverviewRuler.infoForeground'),
                    'RECURSIVE_CALL_ATTRIBUTES': self.select(colors, 'editorOverviewRuler.infoForeground'),
                    'RIGHT_MARGIN_COLOR': self.select(colors, 'editorOverviewRuler.infoForeground'),
                    'SELECTED_TEARLINE_COLOR': self.select(colors, 'editor.lineHighlightBackground'),
                    'SEPARATOR_BELOW_COLOR': self.select(colors, 'editorWhitespace.foreground'),
                    'SOFT_WRAP_SIGN_COLOR': self.select(colors, 'editorWhitespace.foreground'),
                    'TEARLINE_COLOR': self.select(colors, 'editor.foreground'),
                    'VCS_ANNOTATIONS_COLOR_1': self.select(colors, 'gitDecoration.addedResourceForgeround'),
                    'VCS_ANNOTATIONS_COLOR_2': self.select(colors, 'gitDecoration.modifiedResourceForeground'),
                    'VCS_ANNOTATIONS_COLOR_3': self.select(colors, 'gitDecoration.deletedResourceForeground'),
                    'VCS_ANNOTATIONS_COLOR_4': self.select(colors, 'gitDecoration.untrackedResourceForeground'),
                    'VCS_ANNOTATIONS_COLOR_5': self.select(colors, 'gitDecoration.conflictingResourceForeground'),
                    'VISUAL_INDENT_GUIDE': self.select(colors, 'editorWhitespace.foreground'),
                    'WHITESPACES_MODIFIED_LINES_COLOR': self.select(colors, 'gitDecoration.modifiedResourceForeground')
                }

                for attr_key, attr_val in color_options.items():
                    doc.stag('option', name=attr_key, value=attr_val)

            attribute_options = {
                'TEXT': {
                    'FOREGROUND': self.select(colors, 'editor.foreground'),
                    'BACKGROUND': self.select(colors, 'editor.background')
                },
                'BAD_CHARACTER': {
                    'FOREGROUND': self.select(colors, 'errorForeground')
                },
                'CONSOLE_RED_OUTPUT': {
                    'FOREGROUND': self.select(colors, 'errorForeground')
                },
                'DEFAULT_INVALID_STRING_ESCAPE': {
                    'FOREGROUND': self.select(colors, 'errorForeground')
                },
                'BUILDOUT.LINE_COMMENT': {
                    'FOREGROUND': self.select(colors, 'descriptionForeground')
                },
                'DEFAULT_BLOCK_COMMENT': {
                    'FOREGROUND': self.select(colors, 'descriptionForeground')
                },
                'DEFAULT_DOC_COMMENT': {
                    'FOREGROUND': self.select(colors, 'descriptionForeground')
                },
                'DEFAULT_DOC_COMMENT_TAG': {
                    'FOREGROUND': self.select(colors, 'descriptionForeground')
                },
                'DEFAULT_DOC_MARKUP': {
                    'FOREGROUND': self.select(colors, 'editor.foreground')
                },
                'DEFAULT_LINE_COMMENT': {
                    'FOREGROUND': self.select(colors, 'editor.foreground')
                },
                'DEFAULT_OPERATION_SIGN': {
                    'FOREGROUND': self.select(colors, 'textPreformat.foreground')
                },
                'DEFAULT_KEYWORD': {
                    'FOREGROUND': self.select(colors, 'textPreformat.foreground')
                },
                'BUILDOUT.KEY': {
                    'FOREGROUND': self.select(colors, 'textPreformat.foreground')
                },
                'BUILDOUT.KEY_VALUE_SEPARATOR': {
                    'FOREGROUND': self.select(colors, 'textPreformat.foreground')
                },
                'ERRORS_ATTRIBUTES': {
                    'EFFECT_COLOR': self.select(colors, 'errorForeground'),
                    'ERROR_STRIPE_COLOR': self.select(colors, 'errorForeground')
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
