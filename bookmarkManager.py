import bs4
from bs4 import BeautifulSoup
from cleanBookmarkFile import cleanfile

line = '----------------------------------------------------------------------'

with open(cleanfile('testbookmarks.html')) as html_file:
    soup = BeautifulSoup(html_file, 'lxml')


# base is the only key in the first level of
# the bookmarks dict. It's value is a list
# containg all the top level folders and bookmarks
base = soup.dl.dt

sl = soup.dl.dl


def isLink(item: bs4.element.Tag) -> bool:
    if item.find('a', recursive=False):
        return True
    else:
        return False


def isFolderTitle(item: bs4.element.Tag) -> bool:
    if item.find('h3', recursive=False):
        return True
    else:
        return False


def isFolderList(item: bs4.element.Tag) -> bool:
    if (not isLink(item) and not isFolderTitle(item)):
        return True
    else:
        return False


bookmarksDict = {}
bookmarksDict[base] = []


def collectItens(bms: bs4.element.ResultSet) -> dict:
    previous_tag = ''
    index = 0

    for tag in bms:
        if isLink(tag):
            bookmarksDict[base].append(tag)
            previous_tag = tag
            index += 1
        elif isFolderTitle(tag):
            bookmarksDict[base].append({tag: ['testing']})
            previous_tag = tag
            index += 1
        else:
            previous_tag = tag
            index += 1
    return bookmarksDict


bms = sl.find_all(['a', 'dt', 'dl'], recursive=False)

collectItens(bms)

for item in bookmarksDict[base]:
    print(item)
    print(line)

# def printsl() -> None:
#     for item in sl.find_all(['a', 'dt', 'dl'], recursive=False):
#         print(type(item))
#         print(item.prettify())
#         print(line)


# printsl()
