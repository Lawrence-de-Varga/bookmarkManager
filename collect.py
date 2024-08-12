import bs4
from htmlToDict import bmdict, bmlist

bmbf_list = list[bs4.element.Tag]


def collect_folders_h(bmsdict: bmdict, folders_list: bmbf_list) -> bmbf_list:
    for item in bmsdict:
        if isinstance(item, dict): 


def collect_folders(bmsdict: bmdict) -> bmbf_list:
    return collect_folders_h(bmsdict, [])


