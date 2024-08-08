import py_cui
from bookmarkManager import bookmarksDict
from mainLoop import get_folder_contents, simplify_folder_contents

base_bms = simplify_folder_contents(get_folder_contents(bookmarksDict))

title = "PLACEHOLDER"

class BookmarkManager:

    def __init__(self, master: py_cui.PyCUI):

        self.master = master

        self.color = py_cui.YELLOW_ON_BLACK

        self.current_folder_contents = self.master.add_scroll_menu(f"EDITING: {title}", 0, 0, row_span=8, column_span=2)
        self.current_folder_contents.add_item_list(base_bms)
        self.selected_item_contents = self.master.add_scroll_menu(f"CONTENTS: {title}", 0, 2, row_span=8, column_span=2)
        

root = py_cui.PyCUI(8,8)
root.toggle_unicode_borders()
wrapper = BookmarkManager(root)

root.start()
