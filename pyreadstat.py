#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""
CREATED    : 13JUL2019
AUTHOR     : HIBELLM
DESCRIPTION: Testing Pyreadstat module
             https://github.com/Roche/pyreadstat
"""

import pyreadstat


df, meta = pyreadstat.read_sas7bdat('./ref_code/static/data/mammals.sas7bdat')

# done! let's see what we got
print(df.head())
print(meta.column_names)
print(meta.column_labels)
print(meta.number_rows)
print(meta.number_columns)
print(meta.file_label)
print(meta.file_encoding)
# there are other metadata pieces extracted. See the documentation for more details.





