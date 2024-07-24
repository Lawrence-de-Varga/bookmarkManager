from bs4 import BeautifulSoup
import pprint

with open('smallbookmarks.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')


sl = soup.dl.dl

folders = []

for item in sl.find_all('h3'):
    folders.append(item.text)

for folder in folders:
    if sl.find(string=folder).parent.parent.next_sibling:
        pprint.pprint(sl.find(string=folder).parent.parent.next_sibling.find_all('a'))
    print()

# links = soup.find_all('a')
# folders = soup.find_all('h3')

# bookmarkDict = {}



# main_list = soup.find('dl')
# # personal_toolbar_folder = main_list.find('h3')

# secondary_list = main_list.find('dl')
# for item in secondary_list.find_all(last_modified=True):
#     # print(str(item))
#     bookmarkDict[item] = []

# pprint.pp(bookmarkDict)

# # for child in secondary_list.contents:
# #     print(child.dt)
