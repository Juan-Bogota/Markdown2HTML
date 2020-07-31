#!/usr/bin/python3
"""Write a script markdown2html.py that takes an argument 2 strings:
* First argument is the name of the Markdown file
*Second argument is the output file name
"""

import sys
import os.path as path

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)

    if not path.exists(sys.argv[1]):
        sys.stderr.write("Missing {}\n".format(sys.argv[1]))
        sys.exit(1)
    sys.exit(0)
