# This file contains functions used to edit the bookmarks dict.
# E.g adding, renaming, deleting, and moving bookmarks and folders


import bs4
import paths
import copy

# The bookmarksDict is not manipulated as that would mess with the index
# so a copy is made and then modified as we traverse down bmDict
# bmDictCp = copy.deepcopy(bookmarksDict)


def delete_item(item: dict | bs4.element.Tag, path: list[bs4.element.Tag | int], bmdict: dict | list) -> None:
    if len(path) == 1:
        bmdict.remove(item)
    else:
        delete_item(item, path[1:], bmdict[path[0]])


def add_item(item: dict | bs4.element.Tag, path: list[bs4.element.Tag | int], bmdict: dict | list) -> None:
    if len(path) == 1:
        bmdict[path[0]][paths.extract_key(bmdict[path[0]])].append(item)
    else:
        add_item(item, path[1:], bmdict[path[0]])


def replace_item(item: dict | bs4.element.Tag, new_item: dict | bs4.element.Tag,
                 path: list[bs4.element.Tag | int], bmdict: dict | list) -> None:
    if len(path) == 1:
        bmdict[path[0]] = new_item
    else:
        replace_item(item, new_item, path[1:], bmdict[path[0]])


# Repalce_for_deletion is used to maintain te validity of a given path while
# moving links or folders around. The item to be moved is first modifed
# by replace_for_deletion, the unmodified item is then moved to
# its new location, and the the modified item is found again
# as its path may have changed, it is then deleted.
def replace_for_deletion(item: dict | bs4.element.Tag, bmdict) -> bs4.element.Tag | dict:
    path = paths.find_item(item, bmdict)
    new_item = copy.deepcopy(item)
    if isinstance(item, dict):
        paths.extract_key(new_item).h3.string = "DELETE ME"
    else:
        new_item.a.string = "DELETE ME"
    replace_item(item, new_item, path, bmdict)
    return new_item


def move_item(item: dict | bs4.element.Tag, path: list[bs4.element.Tag | int], bmdict: dict | list) -> None:
    old_item = replace_for_deletion(item, bmdict)
    add_item(item, path, bmdict)
    delete_item(old_item, paths.find_item(old_item, bmdict), bmdict)


def rename_folder(folder: dict[bs4.element.Tag, list], new_name: str) -> None:
    paths.extract_key(folder).h3.string = new_name


# test_folder = bookmarksDict[base][5][extract_key(bookmarksDict[base][5])][1]
# test_link_2 = bookmarksDict[base][5][extract_key(bookmarksDict[base][5])][1][extract_key(test_folder)][1]
# test_link = bookmarksDict[base][1]
# tfp = paths.find_item(test_folder, bookmarksDict)
# tlp = paths.find_item(test_link, bookmarksDict)
