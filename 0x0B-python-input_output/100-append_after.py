#!/usr/bin/python3

"""
inserts line of text to file
after each line containing str

"""


def append_after(filename="", search_string="", new_string=""):
    with open(filename, "r+") as f:
        content = []
        for line in f:
            content.append(line)
            if search_string in line:
                content.append(new_string)

    with open(filename, "w") as f:
        st = ""
        f.write(st.join(content))
