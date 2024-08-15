import paths
from htmlToDict import isLink
from typeAliases import bmdict
import bs4

link_options = ['Move', 'Delete']
folder_options = ['Move', 'Delete', 'Add', 'Rename']


def print_options(options: list[str]) -> None:
    index = 1
    for option in options:
        print(f"{index}: {option}.")
        index += 1


def get_folder_name(folder: bmdict) -> str:
    return paths.extract_key(folder).h3.string


def folder_name(folder: bs4.element.Tag) -> str:
    return folder.h3.string


def print_folder_name(folder: bmdict) -> None:
    print(get_folder_name(folder))


# Gets a url
def get_link_href(link: bs4.element.Tag) -> str:
    return link.a.get('href')


# Gets the title of a folder or the url of the href
def get_link_or_folder_from_tag(item: bs4.element.Tag) -> str:
    if isLink(item):
        return get_link_href(item)
    else:
        return item.h3.string


# Gets the bookmarks description
def get_link_text(link: bs4.element.Tag) -> str:
    return link.a.string


def print_link(link: bs4.element.Tag) -> None:
    print(get_link_href(link))


def print_link_text(link: bs4.element.Tag) -> None:
    print(get_link_text(link))
