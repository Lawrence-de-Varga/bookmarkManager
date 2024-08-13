import bs4
from paths import extract_key
# from htmlToDict import bookmarksDict
from typeAliases import bmbf_list, bmdict


def collect_folders_h(bmsdict: bmdict, folders_list: bmbf_list) -> bmbf_list:
    root = extract_key(bmsdict)
    folders_list.append(root)
    for item in bmsdict[root]:
        if isinstance(item, dict): 
            folders_list.extend(collect_folders_h(item, []))
    return folders_list


def collect_folders(bmsdict: bmdict) -> bmbf_list:
    return collect_folders_h(bmsdict, [])


def collect_links_h(bmsdict: bmdict, links_list: bmbf_list) -> bmbf_list:
    root = extract_key(bmsdict)
    for item in bmsdict[root]:
        if isinstance(item, dict):
            links_list.extend(collect_links_h(item, []))
        else:
            links_list.append(item)
    return links_list


def collect_links(bmsdict: bmdict) -> bmbf_list:
    return collect_links_h(bmsdict, [])
