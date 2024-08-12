# This file contains functions used to edit the bookmarks dict.
# E.g adding, renaming, deleting, and moving bookmarks and folders


import bs4
import paths
import copy
from htmlToDict import bmdict, bmlist


# defining the type path for convenience
path = list[bs4.element.Tag | int]

# The bookmarksDict is not manipulated as that would mess with the index
# so a copy is made and then modified as we traverse down bmDict
# bmDictCp = copy.deepcopy(bookmarksDict)


def delete_item(item: bmdict | bs4.element.Tag, Apath: path, bmsdict: [bmdict | bmlist]) -> None:
    if len(Apath) == 1:
        bmsdict.remove(item)
    else:
        delete_item(item, Apath[1:], bmsdict[Apath[0]])


def add_item(item: bmdict | bs4.element.Tag, Apath: path, bmsdict: [bmdict | bmlist]) -> None:
    if len(Apath) == 1:
        bmsdict[Apath[0]][paths.extract_key(bmsdict[Apath[0]])].append(item)
    else:
        add_item(item, Apath[1:], bmsdict[Apath[0]])


def replace_item(item: bmdict | bs4.element.Tag, new_item: bmdict | bs4.element.Tag,
                 Apath: path, bmsdict: [bmdict | bmlist]) -> None:
    if len(Apath) == 1:
        bmsdict[Apath[0]] = new_item
    else:
        replace_item(item, new_item, Apath[1:], bmsdict[Apath[0]])


# Repalce_for_deletion is used to maintain te validity of a given path while
# moving links or folders around. The item to be moved is first modifed
# by replace_for_deletion, the unmodified item is then moved to
# its new location, and the the modified item is found again
# as its path may have changed, it is then deleted.
def replace_for_deletion(item: [bmdict | bs4.element.Tag], bmsdict) -> bs4.element.Tag | bmdict:
    Apath: path = paths.find_item(item, bmsdict)
    new_item = copy.deepcopy(item)
    if isinstance(item, dict):
        paths.extract_key(new_item).h3.string = "DELETE ME"
    else:
        new_item.a.string = "DELETE ME"
    replace_item(item, new_item, Apath, bmsdict)
    return new_item


def move_item(item: bmdict | bs4.element.Tag, Apath: path, bmsdict: bmdict | list) -> None:
    old_item = replace_for_deletion(item, bmsdict)
    add_item(item, Apath, bmsdict)
    delete_item(old_item, paths.find_item(old_item, bmsdict), bmsdict)


def rename_folder(folder: bmdict, new_name: str) -> None:
    paths.extract_key(folder).h3.string = new_name


# test_folder = bookmarksDict[base][5][extract_key(bookmarksDict[base][5])][1]
# test_link_2 = bookmarksDict[base][5][extract_key(bookmarksDict[base][5])][1][extract_key(test_folder)][1]
# test_link = bookmarksDict[base][1]
# tfp = paths.find_item(test_folder, bookmarksDict)
# tlp = paths.find_item(test_link, bookmarksDict)
