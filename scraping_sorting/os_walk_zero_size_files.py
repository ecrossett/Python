# Problem 1

# This script uses os.walk to find all the files in a given location
# and prints the filenames of all zero length files. It then prints
# the total count of all zero lenght files.
import os
location = '/Users/ed/Library/Mobile Documents/com~apple~CloudDocs/Certificates/'           # define dir location
total = 0
count = 0                                    # initialize count
for root, dirs, files in os.walk(location):  # iterate through dir tree
    for file in files:                       # iterate through files
        full_path = os.path.join(root, file) # create full path name
        size = os.path.getsize(full_path)    # pass as arg to get size
        if size == 0:                        # ident files 0 bytes
            count += 1                       # sum all 0 byte files
            print(file, ' %d bytes' % size)  # prints each 0 byte file
        else:
            total += size
print('total number of zero length files: %d' % count)  # total count
print('total size of all files: %d' % total)
