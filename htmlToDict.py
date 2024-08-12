# This file takes the cleaned up html bookmarks file and returns the 
# contents of that file is a dict whose keys are bs4 tags of folders
# and whose values are lists of urls and nested folders
# as bs4 tags



import bs4
from bs4 import BeautifulSoup
from cleanBookmarkFile import cleanfile

# just here for testing to seperate various print statements
line = '----------------------------------------------------------------------'

# The bookmarks.html file produced by chrome 
# does not have closing </DT> tags.
# This makes parsing the file extremely clumsy
# so the file is first modified to add the </DT> tags
with open(cleanfile('sampleBookmarks/smallbookmarks.html')) as html_file:
    soup = BeautifulSoup(html_file, 'lxml')


# base is the only key in the first level of
# the bookmarks dict. It's value is a list
# containg all the top level folders and bookmarks
base: bs4.element.Tag = soup.dl.dt

# soup.dl.dl skips past the header which is not needed
sl: bs4.element.Tag = soup.dl.dl


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


bookmarksDict: dict[bs4.element.Tag, list] = {}
bookmarksDict[base] = []


# Takes the bookmarks htmk file from the browser once modified by cleanBookmarksFile
# and puts the links into lists as a value of a dict the key of which is the bookmark folder
def collectItems(bms: bs4.element.ResultSet, root: bs4.element.Tag, bmsDict: dict) -> dict[bs4.element.Tag, dict]:
    previous_tag = ''
    index = 0

    for tag in bms:
        # if the tag is just a link we simply put it in the list
        if isLink(tag):
            bmsDict[root].append(tag)
            previous_tag = tag
            index += 1

        # if the tag is a folder title we construct an empty dict which will be
        # subsequently filled with more links and titles and folders
        elif isFolderTitle(tag):
            bmsDict[root].append({tag: []})
            previous_tag = tag
            index += 1

        # collectItems calls itself to contrusct a tree out of the bookmark folders
        elif isFolderList(tag):
            newResultSet = tag.find_all(['a', 'dt', 'dl'], recursive=False)
            bmsDict[root][index - 1][previous_tag] = collectItems(newResultSet, previous_tag, bmsDict[root][index - 1])
            previous_tag = tag
    return bmsDict[root]


# This takes the sl tag and strips out the <p> and \n components which litter
# the file.
bmResultSet: bs4.element.ResultSet = sl.find_all(['a', 'dt', 'dl'], recursive=False)

bookmarksDict[base] = collectItems(bmResultSet, base, bookmarksDict)

# Just for testing
# for item in bookmarksDict[base]:
#     if item is dict:
#         for key, value in item.items():
#             print(key)
#             print(value)
#             print(line)
