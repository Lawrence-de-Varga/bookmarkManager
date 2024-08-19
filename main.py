import bs4
from htmlToDict import line, bookmarksDict
import printing
import paths
import collect
import present
from typeAliases import bmbf_list, bmdict
from os import system
from time import sleep
import editBookmarks

# def n_tabs(n: int) -> str:
#     tabs_string = ''
#     for num in range(n):
#         tabs_string+= '\t'
#     return tabs_string

# def main_loop(bmdict: dict[bs4.element.Tag, list[bs4.element.Tag | dict]], tabs) -> None:
#     print()
#     print( n_tabs(tabs) + printing.get_folder_name(bmdict))
#     root = paths.extract_key(bmdict)
    
#     for item in bmdict[root]:
#         if isinstance(item, dict):
#             tabs += 1
#             main_loop(item, tabs)
#             tabs -= 1
#         else:
#             print(n_tabs(tabs + 1) + printing.get_link_href(item))
#             print(n_tabs(tabs + 2) + printing.get_link_text(item))
#             print()
#     print(line)


links = collect.collect_links(bookmarksDict)
folders = collect.collect_folders(bookmarksDict)

print(present.make_folders_presentable(folders))
links = present.map_links_to_tags(present.make_links_presentable(links), links)
folders = present.map_folders_to_tags(present.make_folders_presentable(folders), folders)
# print(folders)

def take_action_on_link(link: bs4.element.Tag, bmsdict: bmdict) -> None:
    print(paths.describe_path(link, bmsdict))
    print("What would you like to do with it?\n")
    print("Hit ENTER to leave it alone.")
    print("Type 'd' to delete it.")
    print("Or type 'm' to move it.")

    action = input("> ")
    match action:
        case '':
            print("Leaving it alone")
            sleep(1)
        case 'd':
            print("deleting it.")
            sleep(1)
            editBookmarks.delete_item(link, paths.find_item(link, bmsdict), bmsdict)
        case 'm':
            print("Moving it.")
            sleep(1)
        case _:
            print(f"Sorry {action} is not an option.")
            print()
            take_action_on_link(link, bmsdict)


def main_loop(bookmarks: bmdict, folders: dict, links: dict) -> None:
    for link in links.values():
        system('clear -x')
        present.present_folders(list(folders.keys()))
        print()
        # print(paths.describe_path(link, bookmarks))
        # print()
        take_action_on_link(link, bookmarks)
                
                
                
        # sleep(2)


main_loop(bookmarksDict, folders, links)
