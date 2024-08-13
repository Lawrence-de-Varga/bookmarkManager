import bs4
from typing import Union

# Defining a few frequently used types
bmbf_list = list[bs4.element.Tag]
bmlist = list[Union[bs4.element.Tag, "bmdict"]]
bmdict = dict[bs4.element.Tag, bmlist]
