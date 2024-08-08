import bs4
from editBookmarks import extract_key
from printing import get_link_or_folder_from_tag


# Takes a folder_dict (which mnay be the whole bookmarks_dict) and returns a list
# containing only the contents of the folder in the first level. i.e. no recursion down the tree.
# It returns the items as bs4 tags which can then later be transformed.
def get_folder_contents(folder_dict: dict[bs4.element.Tag, list]) -> list[bs4.element.Tag]:
    items_list = []
    for item in list(folder_dict.values())[0]:
        if isinstance(item, dict):
            items_list.append(extract_key(item))
        else:
            items_list.append(item)
    return items_list


def simplify_folder_contents(folder_contents: list[bs4.element.Tag]) -> list[str]:
    return [get_link_or_folder_from_tag(item) for item in folder_contents]
