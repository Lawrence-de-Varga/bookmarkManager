import bs4
from bookmarkManager import bookmarksDict, base, line

# The bookmarksDict is not manipulated as that would mess with the index
# so a copy is made and then modified as we traverse down bmDict
bmDictCp = bookmarksDict.deepcopy()


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
            path.append(bmdict[root].index(item))
            return path
        elif isinstance(item, dict):
            possible_path = find_link_path(link, item)
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

    
# def process_link(link: bs4.element.Tag, current_location: dict, current_location_key: bs4.element.Tag) -> dict:
#     print_link(link)
#     action = input("Where would you like this bookmark to be stored? \n(Hit enter to leave it in the current location.)\n")
#     if action == '':
#         print("You hit enter to leave the link where it is.")
#         print(line)
#         return current_location
#     else:
#         print(f"You entererd: {action}.")
#         print(line)
#         return current_location


# def processBmDict(bmdict: dict, root: bs4.element.Tag) -> dict:
#     index = 0
#     for item in bmdict[root]:
#         print(type(item))
#         if isinstance(item, dict):
#             print(extract_key(item).text)
#             print(line)
#             bmdict[root][index] = processBmDict(item, extract_key(item))
#             index += 1
#         else:
#             bmdict[root][index] = process_link(item, bmdict, root)
#             index += 1


# processBmDict(bookmarksDict, base)
