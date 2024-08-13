import bs4

# Defining a few frequently used types
bmbf_list = list[bs4.element.Tag]
bmlist = list[bs4.element.Tag | "bmdict"]
bmdict = dict[bs4.element.Tag, bmlist]
