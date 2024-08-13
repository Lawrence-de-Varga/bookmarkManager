from typeAliases import bmbf_list
from printing import get_link_href, get_folder_name


def make_links_presentable(links_list: bmbf_list) -> list[str]:
    return list(map(get_link_href, links_list))


def make_folders_presentable(folders_list: bmbf_list) -> list[str]:
    return list(map(get_folder_name, folders_list))
