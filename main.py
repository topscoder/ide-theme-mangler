# CLI interface


import theme_mangler.formatters.FormatVSCode as FormatVSCode


# theme-mangler.py
#   --from=vscode
#   --to=intellij
#   --output_dir=./output
#   --output_format=intermediate (defaults to: target lang)
class ThemeManglerCLI():
    # parse_to_intermediate

    def __init__(self, source_filepath: str, source_format: str, target_format: str, output_dir: str = "./output"):
        result = NotImplemented

        if source_format == "vscode":
            formatter = FormatVSCode(source_filepath)
            result_intermediate = formatter.get_intermediate()

            print(formatter.get_intermediate().raw())

        if result is NotImplemented:
            self.usage()

    @staticmethod
    def usage() -> object:
        print(f'Usage: theme-mangler.py --from=vscode --to=intellij [--output_dir=./output]')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    ThemeManglerCLI(
        './test-files/vscode.1.json',
        'vscode',
        'intellij',
        './converted'
    )
