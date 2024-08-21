import bs4
from typeAliases import bmbf_list
from printing import get_link_href, folder_name
# from paths import describe_path


def make_links_presentable(links_list: bmbf_list) -> list[str]:
    """Takes a list of link bs4 tags and returns a list containing just the
    url of the tag."""
    return [get_link_href(link) for link in links_list]


def make_folders_presentable(folders_list: bmbf_list) -> list[str]:
    """Takes a list of folderr bs4 tags and returns a list
    containing just the folder titles."""
    return [folder_name(folder) for folder in folders_list]


def map_links_to_tags(links_list: list[str], link_tag_list: bmbf_list) -> dict[str, bs4.element.Tag]:
    return dict(zip(links_list, link_tag_list))


def map_folders_to_tags(folders_list: list[str], folder_tag_list: bmbf_list) -> dict[str, bs4.element.Tag]:
    return dict(zip(folders_list, folder_tag_list))
    

def find_longest(item_list: list[str]) -> int:
    return len(sorted(item_list, key=len)[-1])


def present_folders_h(folders_list: list[str], num_per_line: int, start: int, stop: int, index: int) -> None:
    """Presents all of the bookmark folder titles in an indexed grid."""
    length_of_longest = find_longest(folders_list) + len(str(len(folders_list))) + 5
    if start >= len(folders_list):
        return
    for folder in folders_list[start:stop]:
        print(f" | {index}: {folder}".ljust(length_of_longest), end='')
        index += 1
    print(' |', end='')
    print()

    present_folders_h(folders_list, num_per_line, stop, (stop + num_per_line), index)


def present_folders(folders_list: list[str]) -> None:
    present_folders_h(folders_list, 5, 0, 5, 1)


