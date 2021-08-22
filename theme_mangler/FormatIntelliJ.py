
from theme_mangler.FormatInterface import FormatInterface
from theme_mangler.ThemeManglerIntermediateFormat import ThemeManglerIntermediateFormat

from yattag import Doc, indent

INTELLIJ_ATTRIBUTES = {
    'DEFAULT_METADATA': '',
    'DEFAULT_KEYWORD': '',
    'DEFAULT_STRING': '',
    'HTML_ATTRIBUTE_VALUE': '',
    'DEFAULT_VALID_STRING_ESCAPE': '',
    'DEFAULT_IDENTIFIER': '',
    'TEXT': ''
}


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
        if element in ("string", "array"):
            return self.select(library, 'textPreformat.foreground')

        if not library.get(element):
            return ''

        return library.get(element).strip('#')[0:6]

    def one_of(self, library: dict, first: str, second: str):
        if library.get(first):
            return self.select(library, first)

        if library.get(second):
            return self.select(library, second)

        return 'not found'

    def get_color_settings(self):
        source_formatter = self.get_intermediate()
        colors = source_formatter.intermediate.container['colors']

        return {
            'CARET_COLOR': self.one_of(colors, 'button.background', 'editor.foreground'),
            'CARET_ROW_COLOR': self.select(colors, 'editor.foreground'),
            'CONSOLE_BACKGROUND_KEY': self.one_of(colors, 'panel.background', 'sideBar.background'),
            'GUTTER_BACKGROUND': self.one_of(colors, 'editorGutter.foreground', 'editor.foreground'),
            'INDENT_GUIDE': self.select(colors, 'editorIndentGuide.background'),
            'LINE_NUMBERS_COLOR': self.one_of(colors, 'editorLineNumber.foreground', 'editor.selectionHighlightBackground'),
            'SELECTED_INDENT_GUIDE': self.select(colors, 'editor.lineHighlightBackground'),
            'SELECTION_BACKGROUND': self.select(colors, 'editor.selectionBackground'),
            # 'WHITESPACES': self.select(colors, 'editorWhitespace.foreground'),
            # 'ADDED_LINES_COLOR': self.select(colors, 'editorGutter.addedBackground'),
            # 'ANNOTATIONS_COLOR': self.select(colors, 'variable.function'),
            # 'DELETED_LINES_COLOR': self.select(colors, 'editorGutter.deletedBackground'),
            # 'DIFF_SEPARATORS_BACKGROUND': self.select(colors, 'panel.background'),
            # 'DOCUMENTATION_COLOR': self.select(colors, 'comment'),
            # 'ERROR_HINT': self.select(colors, 'editorError.foreground'),
            'FILESTATUS_ADDED': self.one_of(colors, 'gitDecoration.addedResourceForeground', 'terminal.ansiBrightCyan'),
            'FILESTATUS_COPIED': self.one_of(colors, 'gitDecoration.modifiedResourceForeground', 'terminal.ansiBrightCyan'),
            # 'FILESTATUS_DELETED': self.select(colors, 'gitDecoration.deletedResourceForeground'),
            # 'FILESTATUS_IDEA_FILESTATUS_DELETED_FROM_FILE_SYSTEM': self.select(colors, 'gitDecoration.deletedResourceForeground'),
            # 'FILESTATUS_IDEA_FILESTATUS_IGNORED': self.select(colors, 'gitDecoration.untrackedResourceForeground'),
            'FILESTATUS_MERGED': self.one_of(colors, 'gitDecoration.modifiedResourceForeground', 'terminal.ansiBrightCyan'),
            'FILESTATUS_MODIFIED': self.one_of(colors, 'gitDecoration.modifiedResourceForeground', 'terminal.ansiBrightCyan'),
            'FILESTATUS_RENAMED': self.one_of(colors, 'gitDecoration.modifiedResourceForeground', 'terminal.ansiBrightCyan'),
            # 'FILESTATUS_UNKNOWN': self.select(colors, 'gitDecoration.untrackedResourceForeground'),
            # 'FILESTATUS_ADDEDOUTSIDE': self.select(colors, 'gitDecoration.addedResourceForeground'),
            # 'FOLDED_TEXT_BORDER_COLOR': self.select(colors, 'sideBar.foreground'),
            # 'INFORMATION_HINT': self.select(colors, 'editorOverviewRuler.infoForeground'),
            # 'LINE_NUMBER_ON_CARET_ROW_COLOR': self.select(colors, 'editorLineNumber.foreground'),
            # 'METHOD_SEPARATORS_COLOR': self.select(colors, 'editor.foreground'),
            # 'MODIFIED_LINES_COLOR': self.select(colors, 'editorOverviewRuler.modifiedForeground'),
            # 'NOTIFICATION_BACKGROUND': self.select(colors, 'notifications.background'),
            # 'QUESTION_HINT': self.select(colors, 'editorOverviewRuler.infoForeground'),
            # 'RECENT_LOCATIONS_SELECTION': self.select(colors, 'editorOverviewRuler.infoForeground'),
            # 'RECURSIVE_CALL_ATTRIBUTES': self.select(colors, 'editorOverviewRuler.infoForeground'),
            # 'RIGHT_MARGIN_COLOR': self.select(colors, 'editorOverviewRuler.infoForeground'),
            # 'SELECTED_TEARLINE_COLOR': self.select(colors, 'editor.lineHighlightBackground'),
            # 'SEPARATOR_BELOW_COLOR': self.select(colors, 'editorWhitespace.foreground'),
            # 'SOFT_WRAP_SIGN_COLOR': self.select(colors, 'editorWhitespace.foreground'),
            # 'TEARLINE_COLOR': self.select(colors, 'editor.foreground'),
            # 'VCS_ANNOTATIONS_COLOR_1': self.select(colors, 'gitDecoration.addedResourceForgeround'),
            # 'VCS_ANNOTATIONS_COLOR_2': self.select(colors, 'gitDecoration.modifiedResourceForeground'),
            # 'VCS_ANNOTATIONS_COLOR_3': self.select(colors, 'gitDecoration.deletedResourceForeground'),
            # 'VCS_ANNOTATIONS_COLOR_4': self.select(colors, 'gitDecoration.untrackedResourceForeground'),
            # 'VCS_ANNOTATIONS_COLOR_5': self.select(colors, 'gitDecoration.conflictingResourceForeground'),
            # 'VISUAL_INDENT_GUIDE': self.select(colors, 'editorWhitespace.foreground'),
            # 'WHITESPACES_MODIFIED_LINES_COLOR': self.select(colors, 'gitDecoration.modifiedResourceForeground')
        }

    def get_attribute_settings(self):
        source_formatter = self.get_intermediate()
        colors = source_formatter.intermediate.container['colors']

        return {
            'TEXT': {
                'FOREGROUND': self.select(colors, 'editor.foreground'),
                'BACKGROUND': self.select(colors, 'editor.background')
            },
            'BAD_CHARACTER': {
                'FOREGROUND': self.select(colors, 'errorForeground'),
                'EFFECT_COLOR': self.select(colors, 'markup.error')
            },
            'ERRORS_ATTRIBUTES': {
                'EFFECT_COLOR': self.select(colors, 'errorForeground'),
                'ERROR_STRIPE_COLOR': self.select(colors, 'errorForeground')
            },
            'ANNOTATION_ATTRIBUTE_NAME_ATTRIBUTES': {'FOREGROUND': self.select(colors, 'terminal.ansiBrightCyan')},
            'ANNOTATION_NAME_ATTRIBUTES': {'FOREGROUND': self.select(colors, 'terminal.ansiBrightCyan')},
            'BOOKMARKS_ATTRIBUTES': {'ERROR_STRIPE_COLOR': self.select(colors, 'invalid')},
            'BUILDOUT.LINE_COMMENT': {'FOREGROUND': self.select(colors, 'descriptionForeground')},
            'BUILDOUT.KEY': {'FOREGROUND': self.select(colors, 'textPreformat.foreground')},
            'BUILDOUT.KEY_VALUE_SEPARATOR': {'FOREGROUND': self.select(colors, 'textPreformat.foreground')},
            'BREADCRUMBS_CURRENT': {'FOREGROUND': self.select(colors, 'breadcrumb.activeSelectionForeground')},
            'BREADCRUMBS_DEFAULT': {'FOREGROUND': self.select(colors, 'breadcrumb.foreground')},
            'BREADCRUMBS_HOVERED': {'FOREGROUND': self.select(colors, 'breadcrumb.focusForeground')},
            'BREADCRUMBS_INACTIVE': {'FOREGROUND': self.select(colors, 'breadcrumb.foreground')},
            'BREAKPOINT_ATTRIBUTES': {'BACKGROUND': self.select(colors, 'invalid')},
            'CONSOLE_BLUE_BRIGHT_OUTPUT': {'FOREGROUND': self.select(colors, 'terminal.ansiBrightBlue')},
            'CONSOLE_BLUE_OUTPUT': {'FOREGROUND': self.select(colors, 'terminal.ansiBlue')},
            'CONSOLE_CYAN_BRIGHT_OUTPUT': {'FOREGROUND': self.select(colors, 'terminal.ansiBrightCyan')},
            'CONSOLE_CYAN_OUTPUT': {'FOREGROUND': self.select(colors, 'terminal.ansiCyan')},
            'CONSOLE_ERROR_OUTPUT': {'FOREGROUND': self.select(colors, 'editorError.foreground')},
            'CONSOLE_GREEN_BRIGHT_OUTPUT': {'FOREGROUND': self.select(colors, 'terminal.ansiBrightGreen')},
            'CONSOLE_GREEN_OUTPUT': {'FOREGROUND': self.select(colors, 'terminal.ansiGreen')},
            'CONSOLE_MAGENTA_BRIGHT_OUTPUT': {'FOREGROUND': self.select(colors, 'terminal.ansiBrightMagenta')},
            'CONSOLE_MAGENTA_OUTPUT': {'FOREGROUND': self.select(colors, 'terminal.ansiMagenta')},
            'CONSOLE_NORMAL_OUTPUT': {'FOREGROUND': self.select(colors, 'terminal.foreground')},
            'CONSOLE_RANGE_TO_EXECUTE': {'EFFECT_COLOR': self.select(colors, 'terminal.ansiGreen')},
            'CONSOLE_RED_BRIGHT_OUTPUT': {'FOREGROUND': self.select(colors, 'terminal.ansiBrightRed')},
            'CONSOLE_RED_OUTPUT': {'FOREGROUND': self.select(colors, 'terminal.ansiRed')},
            'CONSOLE_SYSTEM_OUTPUT': {'FOREGROUND': self.select(colors, 'terminal.ansiYellow')},
            'CONSOLE_USER_INPUT': {'FOREGROUND': self.select(colors, 'terminal.foreground')},
            'CONSOLE_YELLOW_BRIGHT_OUTPUT': {'FOREGROUND': self.select(colors, 'terminal.ansiBrightYellow')},
            'CONSOLE_YELLOW_OUTPUT': {'FOREGROUND': self.select(colors, 'terminal.ansiYellow')},
            'CSS.COLOR': {'FOREGROUND': self.select(colors, 'support.type.custom-property.name')},
            'CSS.IMPORTANT': {INTELLIJ_ATTRIBUTES['DEFAULT_KEYWORD']},
            'CSS.KEYWORD': {'FOREGROUND': self.select(colors, 'keyword.operator.word')},
            'CSS.TAG_NAME': {'FOREGROUND': self.select(colors, 'support.type.property-name')},
            'CSS.URL': {INTELLIJ_ATTRIBUTES['HTML_ATTRIBUTE_VALUE']},
            'CTRL_CLICKABLE': {'FOREGROUND': self.one_of(colors, 'terminal.ansiBrightCyan', 'button.background')},
            'CUSTOM_KEYWORD1_ATTRIBUTES': {'FOREGROUND': self.select(colors, 'entity.other.attribute-name')},
            'CUSTOM_KEYWORD2_ATTRIBUTES': {'FOREGROUND': self.select(colors, 'entity.name.tag support.class.component')},
            'CUSTOM_KEYWORD3_ATTRIBUTES': {'FOREGROUND': self.select(colors, 'support.variable')},
            'CUSTOM_KEYWORD4_ATTRIBUTES': {'FOREGROUND': self.select(colors, 'support.constant')},
            'CUSTOM_STRING_ATTRIBUTES': {INTELLIJ_ATTRIBUTES['DEFAULT_STRING']},
            'CUSTOM_VALID_STRING_ESCAPE_ATTRIBUTES': {INTELLIJ_ATTRIBUTES['DEFAULT_VALID_STRING_ESCAPE']},
            'DEBUGGER_INLINED_VALUES': {'FOREGROUND': self.select(colors, 'comment')},
            'DEBUGGER_INLINED_VALUES_EXECUTION_LINE': {'FOREGROUND': self.select(colors, 'editor.lineHighlightBackground')},
            'DEBUGGER_INLINED_VALUES_MODIFIED': {'FOREGROUND': self.select(colors, 'editorGutter.modifiedBackground')},
            'DEFAULT_BLOCK_COMMENT': {'FOREGROUND': self.select(colors, 'comment')},
            'DEFAULT_CLASS_REFERENCE': {INTELLIJ_ATTRIBUTES['DEFAULT_IDENTIFIER']},
            'DEFAULT_COMMA': {'FOREGROUND': self.select(colors, 'punctuation.definition')},
            'DEFAULT_CONSTANT': {'FOREGROUND': self.select(colors, 'support.constant')},
            'DEFAULT_DOC_COMMENT': {'FOREGROUND': self.select(colors, 'comment')},
            'DEFAULT_DOC_COMMENT_TAG': {'FOREGROUND': self.select(colors, 'entity.name.tag')},
            'DEFAULT_DOC_COMMENT_TAG_VALUE': {'FOREGROUND': self.select(colors, 'editor.foreground')},
            'DEFAULT_DOC_MARKUP': {'FOREGROUND': self.select(colors, 'entity.name.tag')},
            'DEFAULT_FUNCTION_CALL': {INTELLIJ_ATTRIBUTES['DEFAULT_IDENTIFIER']},
            'DEFAULT_FUNCTION_DECLARATION': {'FOREGROUND': self.select(colors, 'support.function')},
            'DEFAULT_IDENTIFIER': {'FOREGROUND': self.select(colors, 'variable.language')},
            'DEFAULT_INSTANCE_FIELD': {'FOREGROUND': self.select(colors, 'support.type.property-name')},
            'DEFAULT_INVALID_STRING_ESCAPE': {'FOREGROUND': self.select(colors, 'invalid')},
            'DEFAULT_KEYWORD': {'FOREGROUND': self.one_of(colors, 'keyword.operator.word', 'terminal.ansiBrightMagenta')},
            'DEFAULT_LINE_COMMENT': {'FOREGROUND': self.select(colors, 'comment')},
            'DEFAULT_METADATA': {'FOREGROUND': self.select(colors, 'entity.other.attribute-name')},
            'DEFAULT_NUMBER': {'FOREGROUND': self.select(colors, 'constant.numeric')},
            'DEFAULT_OPERATION_SIGN': {'FOREGROUND': self.select(colors, 'keyword.operator')},
            'DEFAULT_REASSIGNED_LOCAL_VARIABLE': {'FOREGROUND': self.select(colors, 'editor.foreground')},
            'DEFAULT_REASSIGNED_PARAMETER': {'FOREGROUND': self.select(colors, 'editor.foreground')},
            'DEFAULT_SEMICOLON': {'FOREGROUND': self.select(colors, 'punctuation.definition')},
            'DEFAULT_STATIC_FIELD': {'FOREGROUND': self.select(colors, 'editor.foreground')},
            'DEFAULT_STATIC_METHOD': {'FOREGROUND': self.select(colors, 'support.function')},
            'DEFAULT_STRING': {'FOREGROUND': self.select(colors, 'string')},
            'DEFAULT_TEMPLATE_LANGUAGE_COLOR': {INTELLIJ_ATTRIBUTES['TEXT']},
            'DEFAULT_VALID_STRING_ESCAPE': {'FOREGROUND': self.select(colors, 'string')},
        }

    def to_output_format(self) -> str:
        doc, tag, text = Doc().tagtext()

        with tag('scheme', name='ThemeMangler', parentScheme='Darcula'):
            with tag('metaInfo'):
                with tag('property', name='name'):
                    text('ThemeMangler')
                with tag('property', name='generator'):
                    text('github.com/topscoder/ThemeMangler')
                with tag('property', name='ide'):
                    text('idea')
                with tag('property', name='ideVersion'):
                    text('2019.1.0.0')
                with tag('property', name='themeManglerTheme'):
                    text('runtimeGenerated')

            # Generate color nodes
            with tag('colors'):
                color_options = self.get_color_settings()

                for attr_key, attr_val in color_options.items():
                    doc.stag('option', name=attr_key, value=attr_val)

            # Generate attribute nodes
            with tag('attributes'):
                attribute_options = self.get_attribute_settings()

                for attr_key in attribute_options:
                    with tag('option', name=attr_key):
                        with tag('value'):
                            if isinstance(attribute_options[attr_key], dict):
                                for opt_key, opt_val in attribute_options[attr_key].items():
                                    doc.stag('option', name=opt_key, value=opt_val)

        # Glue together for magic
        result = indent(
            doc.getvalue(),
            indentation=' ' * 2,
            newline='\r\n'
        )

        return result
