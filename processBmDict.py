import bs4
from bookmarkManager import bookmarksDict, base, line


def print_link(link: bs4.element.Tag) -> None:
    print(link.a.get('href'))
    print(link.text)


def extract_key(bmdict: dict) -> bs4.element.Tag:
    return list(bmdict.keys())[0]


def process_link(link: bs4.element.Tag, current_location: dict, current_location_key: bs4.element.Tag) -> dict:
    print_link(link)
    action = input("Where would you like this bookmark to be stored? \n(Hit enter to leave it in the current location.)\n")
    if action == '':
        print("You hit enter to leave the link where it is.")
        print(line)
        return current_location
    else:
        print(f"You entererd: {action}.")
        print(line)
        return current_location


def processBmDict(bmdict: dict, root: bs4.element.Tag) -> dict:
    index = 0
    for item in bmdict[root]:
        print(type(item))
        if isinstance(item, dict):
            print(extract_key(item).text)
            print(line)
            bmdict[root][index] = processBmDict(item, extract_key(item))
        else:
            bmdict[root] = process_link(item, bmdict, root)


processBmDict(bookmarksDict, base)
