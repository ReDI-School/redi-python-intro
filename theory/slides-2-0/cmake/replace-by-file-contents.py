#!/usr/bin/python3

import sys
import os

KEYWORD = '_PLEASE_REPLACE_BY_FILE_CONTENTS:'

source_path = os.path.dirname(sys.argv[1])

with open(sys.argv[1], 'r') as input_file:
    with open(sys.argv[2], 'w') as output_file:
        for line in input_file:
            if line.lstrip()[:len(KEYWORD)] == KEYWORD:
                with open(os.path.join(source_path, line[len(KEYWORD):].rstrip()), 'r') as contents_file:
                    contents = contents_file.read()
                    output_file.write(contents + '\n')
            else:
                output_file.write(line)