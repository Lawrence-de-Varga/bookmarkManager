# This file generates paths to bookmark folders and bookmarks

import bs4
import printing
from typeAliases import bmdict, bmlist 


# Takes a full folder dict and extracts just the folder
# dt.h3 tag
def extract_key(bmsdict: bmdict) -> bs4.element.Tag:
    return list(bmsdict.keys())[0]


# This takes a link or a folder and returns the path
# of keys and indexs necessary to access it.
# It currently returns [extract_key(bmdict)] when link is not in
# the bmdict.
def find_item(item: dict | bs4.element.Tag, bmdict: dict) -> list:
    root = extract_key(bmdict)
    path = [root]
    index = 0
    for obj in bmdict[root]:
        if obj == item:
            path.append(bmdict[root].index(obj))
            return path
        elif isinstance(obj, dict):
            possible_path = find_item(item, obj)
            if isinstance(possible_path[-1], int):
                ind = bmdict[root].index(obj)
                path.append(ind)
                path = path + possible_path
                return path
            else:
                possible_path = []
                index += 1
        elif index >= len(bmdict[root]):
            possible_path = []
            index += 1
    return path


# returns a link or folder at the end of a given path
def find_item_from_path(path: list[bs4.element.Tag | dict], bmdict: dict[bs4.element.Tag, list]) -> bs4.element.Tag | dict:
    if len(path) == 0:
        return bmdict
    else:
        return find_item_from_path(path[1:], bmdict[path[0]])


# def print_item_from_path(path: list[bs4.element.Tag | dict], bmdict: dict[bs4.element.Tag, list]) -> None:
#     item = find_item_from_path(path, bmdict)
#     if isinstance(item, dict):
#         print_folder_name(item)
#     else:
#         print_link(item)


# Grabs either the folder name or url from a given path
def extract_name_from_path(path: list[bs4.element.Tag | dict], bmdict: dict[bs4.element.Tag, list]) -> str:
    item = find_item_from_path(path, bmdict)
    if isinstance(item, dict):
        return printing.get_folder_name(item)
    else:
        return printing.get_link_href(item)


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
    # The last item in the path is treated differently for grammatical reasons
    path_desc[-1] = f"is in {path_desc[-1]}."
    return path_desc


# Returns {link} is in {folder1} which is in {folder2} etc.
def describe_path(link: bs4.element.Tag, bmdict: dict) -> str:
    path = find_item(link, bmdict)
    path_desc = detail_path_description(path_desc_components(path))

    description = f"{printing.get_link_href(link)}"
    for item in path_desc[::-1]:
        description = description + ' ' + item

    return description
