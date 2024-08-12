import bs4
from htmlToDict import line, bookmarksDict
import printing
import paths

def n_tabs(n: int) -> str:
    tabs_string = ''
    for num in range(n):
        tabs_string+= '\t'
    return tabs_string

def main_loop(bmdict: dict[bs4.element.Tag, list[bs4.element.Tag | dict]], tabs) -> None:
    print()
    print( n_tabs(tabs) + printing.get_folder_name(bmdict))
    root = paths.extract_key(bmdict)
    
    for item in bmdict[root]:
        if isinstance(item, dict):
            tabs += 1
            main_loop(item, tabs)
            tabs -= 1
        else:
            print(n_tabs(tabs + 1) + printing.get_link_href(item))
            print(n_tabs(tabs + 2) + printing.get_link_text(item))
            print()
    print(line)


main_loop(bookmarksDict, 0)
