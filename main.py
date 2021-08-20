# CLI interface


from theme_mangler.FormatVSCode import FormatVSCode


# theme-mangler.py
#   --from=vscode
#   --to=intellij
#   --output_dir=./output
#   --output_format=intermediate (defaults to: target lang)
class ThemeManglerCLI:
    # parse_to_intermediate

    def __init__(self, source_filepath: str, source_format: str, target_format: str, output_dir: str = "./output"):
        intermediate = NotImplemented

        if source_format == "vscode":
            formatter = FormatVSCode(source_filepath)
            intermediate = formatter.get_intermediate()

        if target_format == "intellij":
            result = formatter.to_output_format()
            print(result)
            return

        if intermediate is NotImplemented:
            print(self.usage())
            return

        print(intermediate.raw())

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
