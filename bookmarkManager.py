from bs4 import BeautifulSoup

with open('testbookmarks.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

links = soup.find_all('a')
folders = soup.find_all('h3')
for item in folders:
        print(item)
