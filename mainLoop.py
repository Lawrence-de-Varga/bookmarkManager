from processBmDict import *


def get_folder_name(folder: dict[bs4.element.Tag, dict[bs4.element.Tag | dict]]) -> str:
    return extract_key(folder).h3.string


def print_folder_name(folder: dict[bs4.element.Tag, dict[bs4.element.Tag | dict]]) -> None:
    print(get_folder_name(folder))


def get_link_href(link: bs4.element.Tag) -> str:
    return link.a.get('href')

def get_link_text(link: bs4.element.Tag) -> str:
    return link.a.string

def print_link(link: bs4.element.Tag) -> None:
    print(get_link_href(link))

def print_link_text(link: bs4.element.Tag) -> None:
    print(get_link_text(link))


def main_loop(bmdict: dict[bs4.element.Tag, list[bs4.element.Tag | dict]]) -> dict:
    pass
