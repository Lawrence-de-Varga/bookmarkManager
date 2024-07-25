# This script takes the badly formatted bookmarks html file
# that is exported from the browser and adds the closing
# </DT> tag to the end of all lines which need it.
# This greatly eases the job of manipulating the bookmarks file.
# The resulting file is still readable by the browser (at least on chrome and brave)

with open('bookmarks_7_25_24.html', 'r') as f:
    f_contents = f.readlines()
    with open('rearranged_bookmarks.html', 'w') as nf:
        for line in f_contents:
            if '<DT>' in line:
                new_line = line.rstrip() + '</DT>\n'
                nf.write(new_line)
            else:
                nf.write(line)
                
