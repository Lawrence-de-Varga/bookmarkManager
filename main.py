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


# Lists of links and folder bs4 tags
links = collect.collect_links(bookmarksDict)
folders = collect.collect_folders(bookmarksDict)

# Lists of urls and folder name strings
presentable_links = present.make_links_presentable(links)
presentable_folders = present.make_folders_presentable(folders)

# Dicts of urls and link bs4 tags, and folder name and folder bs4 tags
link_dict = present.map_links_to_tags(presentable_links, links)
folder_dict = present.map_folders_to_tags(presentable_folders, folders)


def move_link(link: bs4.element.Tag, bmsdict: bmdict) -> None:
    print("Which folder would you like to move it to?")
    print("Type the number corresponding to the folder from the grid above.")
    print("Or type ENTER to leave it.")
    fldr_no = input()
    folders_index = dict(zip(range(1, (len(presentable_folders) + 1)), presentable_folders))
    print(presentable_folders)
    print(folders_index)
    if fldr_no == '':
        return
    elif int(fldr_no) in folders_index.keys():
        print(f"Moving {link} to {folders_index[int(fldr_no)]}.")
        editBookmarks.move_item(link, paths.find_item(link, bmsdict), bmsdict)
        return
    else:
        print(f"Sorry {fldr_no} does not correspond to any known folder.")
        move_link(link, bmsdict, flders)
    return
            
            
    
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
            move_link(link, bmsdict)
            sleep(1)
        case _:
            print(f"Sorry {action} is not an option.")
            print()
            take_action_on_link(link, bmsdict)


def main_loop(bookmarks: bmdict, folders: dict, links: dict) -> None:
    for item in folders:
        print(item)
    for link in links.values():
        system('clear -x')
        present.present_folders(list(folders.keys()))
        print()
        # print(paths.describe_path(link, bookmarks))
        # print()
        take_action_on_link(link, bookmarks)
                
                
                
        # sleep(2)


main_loop(bookmarksDict, folder_dict, link_dict)
