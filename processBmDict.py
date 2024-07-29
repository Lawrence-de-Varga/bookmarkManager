import bs4
from bookmarkManager import bookmarksDict, line, base
import copy

# The bookmarksDict is not manipulated as that would mess with the index
# so a copy is made and then modified as we traverse down bmDict
bmDictCp = copy.deepcopy(bookmarksDict)


def print_link(link: bs4.element.Tag) -> None:
    print(link.a.get('href'))
    print(link.text)


def extract_key(bmdict: dict) -> bs4.element.Tag:
    return list(bmdict.keys())[0]


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


def delete_item(item: dict | bs4.element.Tag, path: list[bs4.element.Tag | int], bmdict: dict | list) -> dict:
    if len(path) == 1:
        bmdict.remove(item)
    else:
        delete_item(item, path[1:], bmdict[path[0]])


def add_item(item: dict | bs4.element.Tag, path: list[bs4.element.Tag | int], bmdict: dict | list) -> dict:
    if len(path) == 1:
        bmdict[path[0]][extract_key(bmdict[path[0]])].append(item)
    else:
        add_item(item, path[1:], bmdict[path[0]])
