import bs4
from htmlToDict import line
import printing
import paths


def main_loop(bmdict: dict[bs4.element.Tag, list[bs4.element.Tag | dict]]) -> None:
    printing.print_folder_name(bmdict)
    root = paths.extract_key(bmdict)
    for item in bmdict[root]:
        if isinstance(item, dict):
            main_loop(item)
        else:
            printing.print_link(item)
            print('\t' + printing.get_link_text(item))
            print()
    print(line)
