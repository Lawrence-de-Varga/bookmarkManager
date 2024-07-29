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


def delete_item(item: dict | bs4.element.Tag, path: list[bs4.element.Tag | int], bmdict: dict | list) -> None:
    if len(path) == 1:
        bmdict.remove(item)
    else:
        delete_item(item, path[1:], bmdict[path[0]])


def add_item(item: dict | bs4.element.Tag, path: list[bs4.element.Tag | int], bmdict: dict | list) -> None:
    if len(path) == 1:
        bmdict[path[0]][extract_key(bmdict[path[0]])].append(item)
    else:
        add_item(item, path[1:], bmdict[path[0]])


def replace_item(item: dict | bs4.element.Tag, new_item: dict | bs4.element.Tag,
                 path: list[bs4.element.Tag | int], bmdict: dict | list) -> None:
    if len(path) == 1:
        bmdict[path[0]] = new_item
    else:
        replace_item(item, new_item, path[1:], bmdict[path[0]])


def replace_for_deletion(item: dict | bs4.element.Tag, bmdict) -> None:
    path = find_item(item, bmdict)
    new_item = copy.deepcopy(item)
    if isinstance(item, dict):
        extract_key(new_item).h3.string = "DELETE ME"
    else:
        new_item.a.string = "DELETE ME"
    replace_item(item, new_item, path, bmdict)


def move_item(item: dict | bs4.element.Tag, path: list[bs4.element.Tag | int], bmdict: dict | list) -> dict:
    delete_item(item, find_item(item, bmdict), bmdict)
    add_item(item, path, bmdict)
    return bmdict


test_folder = bookmarksDict[base][5][extract_key(bookmarksDict[base][5])][1]
test_link = bookmarksDict[base][1]
tfp = find_item(test_folder, bookmarksDict)
tlp = find_item(test_link, bookmarksDict)
