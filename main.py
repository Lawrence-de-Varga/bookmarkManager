import cui
import mainLoop
import processBmDict
import htmlToDict


def main_loop(bmdict: dict[bs4.element.Tag, list[bs4.element.Tag | dict]]) -> None:
    print_folder_name(bmdict)
    root = extract_key(bmdict)
    for item in bmdict[root]:
        if isinstance(item, dict):
            main_loop(item)
        else:
            print_link(item)
            print('\t' + get_link_text(item))
            print()
    print(line)
