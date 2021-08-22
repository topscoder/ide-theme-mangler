# CLI interface


from theme_mangler.FormatVSCode import FormatVSCode
from theme_mangler.FormatIntelliJ import FormatIntelliJ


class ThemeManglerCLI:

    def __init__(self, source_filepath: str, source_format: str, target_format: str, output_dir: str = "./output"):
        intermediate = NotImplemented
        result = None

        if source_format == "vscode":
            source_formatter = FormatVSCode()
            source_formatter.add_source_file(source_filepath)
            intermediate = source_formatter.get_intermediate()

        if target_format == "intellij":
            target_formatter = FormatIntelliJ()
            target_formatter.set_intermediate(source_formatter)
            result = target_formatter.to_output_format()
            #print(result)

        if intermediate is NotImplemented:
            print(self.usage())

        if result is not None:
            # print(result)

            target = './test-files/ThemeMangler.icls'

            fd = open(target, 'w')
            fd.write(result)
            fd.close()

            print('written to:')
            print(target)

    @staticmethod
    def usage() -> object:
        print(f'Usage: theme-mangler.py --from=vscode --to=intellij [--output_dir=./output]')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    ThemeManglerCLI(
        './test-files/night-owl.vscode.json',
        'vscode',
        'intellij',
        './converted'
    )
