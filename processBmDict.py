import bs4
from bookmarkManager import bookmarksDict, base, line
import copy

# The bookmarksDict is not manipulated as that would mess with the index
# so a copy is made and then modified as we traverse down bmDict
bmDictCp = copy.deepcopy(bookmarksDict)


def print_link(link: bs4.element.Tag) -> None:
    print(link.a.get('href'))
    print(link.text)


def extract_key(bmdict: dict) -> bs4.element.Tag:
    return list(bmdict.keys())[0]


def find_link_path(link: bs4.element.Tag, bmdict: dict) -> list:
    root = extract_key(bmdict)
    path = [root]
    index = 0
    for item in bmdict[root]:
        if item == link:
            breakpoint()
            path.append(bmdict[root].index(item))
            return path
        elif isinstance(item, dict):
            possible_path = find_link_path(link, item)
            breakpoint()
            if isinstance(possible_path[-1], int):
                ind = bmdict[root].index(item)
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


def delete_link(link: bs4.element.Tag, path: list, bmdict: dict) -> dict:
    if len(path) == 1:
        bmdict.remove(link)
    else:
        delete_link(link, path[1:], bmdict[path[0]])


# processBmDict(bookmarksDict, base)
