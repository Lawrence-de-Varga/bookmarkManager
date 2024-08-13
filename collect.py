import bs4
from paths import extract_key
from htmlToDict import bmdict, bmlist, bookmarksDict

bmbf_list = list[bs4.element.Tag]


def collect_folders_h(bmsdict: bmdict, folders_list: bmlist) -> bmlist:
    root = extract_key(bmsdict)
    folders_list.append(root)
    for item in bmsdict[root]:
        if isinstance(item, dict): 
            folders_list.extend(collect_folders_h(item, []))
    return folders_list


def collect_folders(bmsdict: bmdict) -> bmbf_list:
    return collect_folders_h(bmsdict, [])


