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


def isLink(tag: bs4.element.tag) -> bool:
    if tag.find('a', recursive=False):
        return True
    else:
        return False


def isFolderTitle(tag: bs4.element.tag) -> bool:
    if tag.find('h3', recursive=False):
        return True
    else:
        return False

def printsl() -> None:
    for item in sl.find_all(['a', 'dt', 'dl'], recursive=False):
        print(type(item))
        print(item.prettify())
        print(line)


printsl()
