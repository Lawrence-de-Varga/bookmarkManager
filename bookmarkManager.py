import bs4
from bs4 import BeautifulSoup
import pprint

with open('smallbookmarks.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')


# base is the only key in the first level of
# the bookmarks dict. It's value is a list 
# containg all the top level folders and bookmarks 
base = soup.dl.dt

sl = soup.dl.dl

folders = []


for item in sl.find_all('dl', recursive=False):
    folders.append(item.text)

bookmarks_dict = {}
for item in sl.find_all('dl', recursive=False):
    bookmarks_dict[item.previous_sibling.text.rstrip()] = item


def links_list(bs_result: bs4.element.ResultSet) -> list[bs4.element.ResultSet]:
    return [item.find_all('a') for item in bs_result if item.a]
    
def printBookmarks(bookmark_dict: dict) -> None:
    for key, value in bookmark_dict.items():
        print(key)
        print()
        print(value)
        print()
        print()
        print('-----------------------------------------------------------------------------------')

# printBookmarks(bookmarks_dict)

q = links_list(sl.find_all('dt', recursive=False))
 

for item in q:
    print(item)
