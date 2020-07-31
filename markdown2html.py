#!/usr/bin/python3
"""Write a script markdown2html.py that takes an argument 2 strings:
* First argument is the name of the Markdown file
*Second argument is the output file name
"""

import sys
import os.path as path

if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)

    if not path.exists(sys.argv[1]):
        sys.stderr.write("Missing {}\n".format(sys.argv[1]))
        sys.exit(1)
    with open(sys.argv[1], "r") as readme:
        text, tmp = "", ""
        text_ant = "\n"
        my_list = []
        simbols = ["-", "*", " ", "#"]
        for line in readme.readlines():

            count = 0
            for caracter in line:
                if caracter not in simbols:
                    my_list = []
                    if caracter == "\n":
                        text_ant = caracter
                        break
                    if text_ant == "\n":
                        tmp = text
                        text += "<p>\n{}</p>\n".format(line)
                    else:
                        text = tmp
                        text += "<p>\n{}<br>\n{}</p>\n".format(
                            text_ant, line)
                    text_ant = line
                    break
                if caracter == "#":
                    count += 1
                    continue
                elif count:
                    word = (line[count + 1:-1])
                    text += "<h{}>{}</h{}>\n".format(count, word, count)
                    tmp = text
                    break
                if caracter == "-" or caracter == "*":
                    if my_list:
                        text = tmp
                    li_list = ""
                    word = (line[2:-1])
                    my_list.append(word)
                    for li in my_list:
                        li_list += "<li>{}</li>\n".format(li)
                    tmp = text
                    if caracter == "-":
                        text += "<ul>\n{}</ul>\n".format(li_list)
                    else:
                        text += "<ol>\n{}</ol>\n".format(li_list)
                    break

    with open(sys.argv[2], "w") as html:
        html.write(text)
    sys.exit(0)
