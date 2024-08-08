# TODO: remove star import once no longer useful for testing
from processBmDict import *
from processBmDict import extract_key, line, find_item
from bookmarkManager import isLink
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


# Gets a url
def get_link_href(link: bs4.element.Tag) -> str:
    return link.a.get('href')


# Gets the title of a folder or the url of the href
def get_link_or_folder_from_tag(item: bs4.element.Tag) -> str:
    if isLink(item):
        return get_link_href(item)
    else:
        return item.h3.string


# Gets the bookmarks description
def get_link_text(link: bs4.element.Tag) -> str:
    return link.a.string


def print_link(link: bs4.element.Tag) -> None:
    print(get_link_href(link))


def print_link_text(link: bs4.element.Tag) -> None:
    print(get_link_text(link))


# returns a link or folder at the end of a given path
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


# Grabs either the folder name or url from a given path
def extract_name_from_path(path: list[bs4.element.Tag | dict], bmdict: dict[bs4.element.Tag, list]) -> str:
    item = find_item_from_path(path, bmdict)
    if isinstance(item, dict):
        return get_folder_name(item)
    else:
        return get_link_href(item)


# Takes a folder_dict (which mnay be the whole bookmarks_dict) and returns a list
# containing only the contents of the folder in the first level. i.e. no recursion down the tree.
# It returns the items as bs4 tags which can then later be transformed.
def get_folder_contents(folder_dict: dict[bs4.element.Tag, list]) -> list[bs4.element.Tag]:
    items_list = []
    for item in list(folder_dict.values())[0]:
        if isinstance(item, dict):
            items_list.append(extract_key(item))
        else:
            items_list.append(item)
    return items_list


def simplify_folder_contents(folder_contents: list[bs4.element.Tag]) -> list[str]:
    return [get_link_or_folder_from_tag(item) for item in folder_contents]
        

# Extracts just the folder names froma  given path to be used
# is describing the links location
def path_desc_components(path: list[bs4.element.Tag | dict]) -> list[str]:
    path_desc = []

    for path_component in path:
        if isinstance(path_component, bs4.element.Tag):
            path_desc.append(path_component.h3.string)
    return path_desc

# creates the string for describe_path to print
def detail_path_description(path_desc: list[str]) -> list[str]:
    for i in range(0, (len(path_desc) - 1)):
        path_desc[i] = f"Which is in {path_desc[i]}."
    path_desc[-1] = f"is in {path_desc[-1]}."
    return path_desc


# Prints {link} is in {folder1} which is in {folder2} etc.
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
