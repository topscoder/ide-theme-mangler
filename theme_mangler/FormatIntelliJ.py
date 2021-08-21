
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

        result = ""

        mapping = {
            "editorLineNumber.foreground": "CARET_COLOR",
            "editorLineNumber.foreground": "CARET_ROW_COLOR", # a mark (‸, ⁁) placed below the line to indicate a proposed insertion in a printed or written text.

            "editorGutter.background": "GUTTER_BACKGROUND",
            "editorIndentGuide.background": "INDENT_GUIDE",
            "editorLineNumber.foreground": "LINE_NUMBERS_COLOR",
            "tree.indentGuidesStroke": "SELECTED_INDENT_GUIDE",
            "selection.background": "SELECTION_BACKGROUND",
            "editorWhitespace.foreground": "WHITESPACES",
        }

        doc, tag, text = Doc().tagtext()

        with tag('scheme'):
            with tag('metaInfo'):
                with tag('property', name='generator'):
                    text('ThemeMangler')
            with tag('colors'):
                source_formatter = self.get_intermediate()
                colors = source_formatter.intermediate.container['colors']

                editor_foreground = colors.get('editor.foreground').strip('#')[0:6] or ''

                doc.stag('option', name='CARET_COLOR', value=editor_foreground)
                doc.stag('option', name='CARET_ROW_COLOR', value=editor_foreground)
                doc.stag('option', name='GUTTER_BACKGROUND', value=editor_foreground)
                doc.stag('option', name='INDENT_GUIDE', value=colors.get('editorIndentGuide.background').strip('#')[0:6] or '')
                doc.stag('option', name='LINE_NUMBERS_COLOR', value=editor_foreground)
                doc.stag('option', name='SELECTED_INDENT_GUIDE', value=colors.get('editorIndentGuide.background').strip('#')[0:6] or '')
                doc.stag('option', name='SELECTION_BACKGROUND', value=colors.get('editorIndentGuide.background').strip('#')[0:6] or '')
                doc.stag('option', name='WHITESPACES', value=colors.get('editorWhitespace.foreground').strip('#')[0:6] or '')

                # for prop, value in colors.items():
                #     prop_def = mapping.get(prop) or prop
                #     doc.stag('option', name=prop_def, value=value)

            with tag('attributes'):
                with tag('option', name='TEXT'):
                    with tag('value'):
                        doc.stag('option', name="FOREGROUND", value=colors.get('editor.foreground').strip('#')[0:6] or '')
                        doc.stag('option', name="BACKGROUND", value=colors.get('editor.background').strip('#')[0:6] or '')
                with tag('option', name='BAD_CHARACTER'):
                    with tag('value'):
                        doc.stag('option', name="FOREGROUND", value=colors.get('errorForeground').strip('#')[0:6] or '')
                with tag('option', name='CONSOLE_RED_OUTPUT'):
                    with tag('value'):
                        doc.stag('option', name="FOREGROUND", value=colors.get('errorForeground').strip('#')[0:6] or '')
                with tag('option', name='DEFAULT_INVALID_STRING_ESCAPE'):
                    with tag('value'):
                        doc.stag('option', name="FOREGROUND", value=colors.get('errorForeground').strip('#')[0:6] or '')

                with tag('option', name='BUILDOUT.LINE_COMMENT'):
                    with tag('value'):
                        doc.stag('option', name="FOREGROUND", value=colors.get('descriptionForeground').strip('#')[0:6] or '')
                with tag('option', name='DEFAULT_BLOCK_COMMENT'):
                    with tag('value'):
                        doc.stag('option', name="FOREGROUND", value=colors.get('descriptionForeground').strip('#')[0:6] or '')
                with tag('option', name='DEFAULT_DOC_COMMENT'):
                    with tag('value'):
                        doc.stag('option', name="FOREGROUND", value=colors.get('descriptionForeground').strip('#')[0:6] or '')
                with tag('option', name='DEFAULT_DOC_COMMENT_TAG'):
                    with tag('value'):
                        doc.stag('option', name="FOREGROUND", value=colors.get('descriptionForeground').strip('#')[0:6] or '')
                with tag('option', name='DEFAULT_DOC_MARKUP'):
                    with tag('value'):
                        doc.stag('option', name="FOREGROUND", value=colors.get('editor.foreground').strip('#')[0:6] or '')
                with tag('option', name='DEFAULT_LINE_COMMENT'):
                    with tag('value'):
                        doc.stag('option', name="FOREGROUND", value=colors.get('editor.foreground').strip('#')[0:6] or '')

                with tag('option', name='DEFAULT_OPERATION_SIGN'):
                    with tag('value'):
                        doc.stag('option', name="FOREGROUND", value=colors.get('textPreformat.foreground').strip('#')[0:6] or '')
                with tag('option', name='DEFAULT_KEYWORD'):
                    with tag('value'):
                        doc.stag('option', name="FOREGROUND", value=colors.get('textPreformat.foreground').strip('#')[0:6] or '')
                with tag('option', name='BUILDOUT.KEY'):
                    with tag('value'):
                        doc.stag('option', name="FOREGROUND", value=colors.get('textPreformat.foreground').strip('#')[0:6] or '')
                with tag('option', name='BUILDOUT.KEY_VALUE_SEPARATOR'):
                    with tag('value'):
                        doc.stag('option', name="FOREGROUND", value=colors.get('textPreformat.foreground').strip('#')[0:6] or '')

                with tag('option', name='ERRORS_ATTRIBUTES'):
                    with tag('value'):
                        doc.stag('option', name="EFFECT_COLOR", value=colors.get('errorForeground').strip('#')[0:6] or '')
                        doc.stag('option', name="ERROR_STRIPE_COLOR", value=colors.get('errorForeground').strip('#')[0:6] or '')

        result = indent(
            doc.getvalue(),
            indentation=' ' * 2,
            newline='\r\n'
        )

        return result
