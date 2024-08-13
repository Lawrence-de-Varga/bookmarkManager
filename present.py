import bs4
from typeAliases import bmbf_list
from printing import get_link_href, folder_name


def make_links_presentable(links_list: bmbf_list) -> list[str]:
    return list(map(get_link_href, links_list))


def make_folders_presentable(folders_list: bmbf_list) -> list[str]:
    return list(map(folder_name, folders_list))


def map_links_to_tags(links_list: list[str], link_tag_list: bmbf_list) -> dict[str, bs4.element.Tag]:
    return dict(zip(links_list, link_tag_list))


def map_folders_to_tags(folders_list: list[str], folder_tag_list: bmbf_list) -> dict[str, bs4.element.Tag]:
    return dict(zip(folders_list, folder_tag_list))
    
