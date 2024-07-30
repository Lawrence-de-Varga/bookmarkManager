# TODO: remove star import once no longer useful for testing
from processBmDict import *
from processBmDict import extract_key, line, find_item
import bs4

link_options = ['Move', 'Delete']
folder_options = ['Move', 'Delete', 'Add', 'Rename']


def print_options(options: list[str]) -> None:
    index = 1
    for option in options:
        print(f"{index}: {option}.")
        index += 1


def get_folder_name(folder: dict[bs4.element.Tag, list[bs4.element.Tag | dict]]) -> str:
    return extract_key(folder).h3.string


def print_folder_name(folder: dict[bs4.element.Tag, list[bs4.element.Tag | dict]]) -> None:
    print(get_folder_name(folder))


def get_link_href(link: bs4.element.Tag) -> str:
    return link.a.get('href')


def get_link_text(link: bs4.element.Tag) -> str:
    return link.a.string


def print_link(link: bs4.element.Tag) -> None:
    print(get_link_href(link))


def print_link_text(link: bs4.element.Tag) -> None:
    print(get_link_text(link))


def find_item_from_path(path: list[bs4.element.Tag | dict], bmdict: dict[bs4.element.Tag, list]) -> bs4.element.Tag | dict:
    if len(path) == 0:
        return bmdict
    else:
        return find_item_from_path(path[1:], bmdict[path[0]])


def print_item_from_path(path: list[bs4.element.Tag | dict], bmdict: dict[bs4.element.Tag, list]) -> None:
    item = find_item_from_path(path, bmdict)
    if isinstance(item, dict):
        print_folder_name(item)
    else:
        print_link(item)


def extract_name_from_path(path: list[bs4.element.Tag | dict], bmdict: dict[bs4.element.Tag, list]) -> str:
    item = find_item_from_path(path, bmdict)
    if isinstance(item, dict):
        return get_folder_name(item)
    else:
        return get_link_href(item)


def path_desc_components(path: list[bs4.element.Tag | dict]) -> list[str]:
    path_desc = []

    for path_component in path:
        if isinstance(path_component, bs4.element.Tag):
            path_desc.append(path_component.h3.string)
    return path_desc


def detail_path_description(path_desc: list[str]) -> list[str]:
    for i in range(0, (len(path_desc) - 1)):
        path_desc[i] = f"Which is in {path_desc[i]}."
    path_desc[-1] = f"is in {path_desc[-1]}."
    return path_desc


def describe_path(link: bs4.element.Tag, bmdict: dict) -> None:
    path = find_item(link, bmdict)
    path_desc = detail_path_description(path_desc_components(path))

    description = f"{get_link_href(link)}"
    for item in path_desc[::-1]:
        description = description + ' ' + item

    print(description)


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
