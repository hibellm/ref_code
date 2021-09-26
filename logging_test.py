
# TEST BRING IN LOG INFO FROM ANOTHER FILE
from ref_code.logging_example import *


# Some demo codes
mylogs.debug("debug")
mylogs.info("info")
mylogs.warning("warn")
mylogs.critical("critical")
mylogs.error("error")


# CLEAN UP LOG FILES

import zipfile as zp
import os
import datetime as dt
import nltk

my_zipfile = zp.ZipFile(os.path.join(os.getcwd(), 'ref_code', f"logging_proc001_{dt.datetime.now().strftime('%y_%m_%d_%H_%M_%S')}.zip"), mode='w', compression=zp.ZIP_DEFLATED)

# WRITE TO ZIP FILE
my_zipfile.write(os.path.join(log_root, "logging_example.log"), arcname=(os.path.join(log_root, "logging_example.log")).split('\\')[-1])
my_zipfile.write(os.path.join(log_root, "logging_example_critical.log"), arcname=(os.path.join(log_root, "logging_example_critical.log")).split('\\')[-1])

my_zipfile.close()

# EXAMINE LOG TO SEE IF ERROR/WARNING
# Open the file in read mode
text = open(os.path.join(log_root, "logging_example.log"), "r")
  
# Create an empty dictionary
d = dict()
# Loop through each line of the file
for line in text:
    # Remove the leading spaces and newline character
    # Convert the characters in line to lowercase to avoid case mismatch
    line = (line.lower().strip()).replace(" ", "")
    # Split the line into words
    words = (line.split("-"))
    # Iterate over each word in line
    for word in words:
        # Check if the word is already in dictionary
        if word in d:
            # Increment count of word by 1
            d[word] = d[word] + 1
        else:
            # Add the word to dictionary with count 1
            d[word] = 1
  
# Print the contents of dictionary
for key in list(d.keys()):
    print(key, ":", d[key])

# ARCHIVE TO AWS



text = open(os.path.join(log_root, "logging_example.log"), "r")

all_msg = []  
for line in text:
    print( (line.lower().strip()).replace(" ", "").split('-')[3] )
    all_msg.append((line.lower().strip()).replace(" ", "").split('-')[3])

unique = set(all_msg)
for i in unique:
    print(i, all_msg.count(i))