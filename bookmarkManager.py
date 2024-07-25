from bs4 import BeautifulSoup
import pprint

with open('smallbookmarks.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')


sl = soup.dl.dl

folders = []

for item in sl.find_all('dl', recursive=False):
    folders.append(item.text)

bookmarks_dict = {}
for item in sl.find_all('dl', recursive=False):
    bookmarks_dict[item.previous_sibling.text.rstrip()] = item

def printBookmarks(bookmark_dict: dict) -> None:
    for key, value in bookmark_dict.items():
        print(key)
        print()
        print(value)
        print()
        print()
        print('-----------------------------------------------------------------------------------')

printBookmarks(bookmarks_dict)
