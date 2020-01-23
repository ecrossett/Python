# This program takes the name of a directory (folder) and finds the extension of each
# file. For each extension found, it prints the number of files with that extension
# and the minimum, average, and maximum size for files with that extension in the
# selected directory.

import os, sys                            

directory = '.'                     # specify directory (folder) you want to search

if os.path.isdir(directory):        # determine if directory name is valid
    print('searching in directory: "%s" ...\n' % directory)
else:
    print('%s is an invalid directory name' % directory)
    
dictionary = {}                                        # initialize dictionary
dir_size = 0                                           # initialize directory size
for root, dirs, files in os.walk(directory):           # iterate through dir tree
    for file in files:                                 # iterate through files
        full_path = os.path.join(root,file)            # create full path name
        size = os.path.getsize(full_path)              # pass as arg to get size
        dir_size += size                               # sum iteration to get dir size
        extension = os.path.splitext(file)             # get file extension
        extension = extension[1]
        #print(full_path,size)                         # for debug
        if not dictionary.get(extension):              # add new entries to dictionary
            dictionary[extension] = []
        dictionary[(extension)] += [(file, size)]      # filename and file size 
file_types = list(dictionary.keys())                   # convert dict to list 
print('File types found: ', file_types)                # display list of file types
print('Directory Size: ',dir_size,'\n')                # display directory size 

for extension in dictionary.keys():                    # iterate through each file type 
    count = 0                                          # initialize count, size, avg
    totalsize = 0
    average = 0
    for file in dictionary[extension]:                 # iterate through files
        count += 1                                     # sum iteration
        totalsize += file[1]                           # size iteration
        average = totalsize / len(dictionary[extension])               # avg iteration
    minimum = sorted(dictionary[extension],key=lambda sz:sz[1])[0][1]  # min
    maximum = sorted(dictionary[extension],key=lambda sz:sz[1])[-1][1] # max
    # define summary information to display                      
    summary = 'File Type: %s\n\tTotal Count: %d\n\tTotal Size: %d\n\t\
Average Size: %d\n\tMinimum Size: %d\n\tMaximum Size: %d' \
    % (extension,count, totalsize, average, minimum, maximum)
    
    print(summary)                                     # display results
    print()

## debug and additional optional displays below ##

    #print('total count of %s files: %d' % (extension, count))
    #print('total size of %s files: %d' % (extension, totalsize))
    #print('average size of %s files: %d' % (extension, average))
    #print('minimum size of %s files: %d' % (extension, minimum))
    #print('maximum size of %s files: %d' % (extension, maximum))
    
#print(dictionary.keys())
#print(dictionary)
