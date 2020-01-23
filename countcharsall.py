# This script reads each line of a file and counts the number of
# characters in each line.  It keeps track of the total number of 
# characters read up to 1,000.

filename = 'test_file.txt'
f = open(filename,'r')              # open file read only
all_lines = f.read().splitlines()   # read all lines of the file, remove '\n'
f.close()                           # close file

# initialize variables
lengths = []
total_length = 0

for single_line in all_lines:       # loop through each line and count chars
    if total_length >= 1000:        # stop once total is 1000
        break
    else:
        lengths.append(len(single_line))   # add each line count to vector
        total_length = total_length + len(single_line)  # tally total count
    
# print the char length vector of all lines and total char count
print('number of characters for each line: ',lengths)                      
print('total characters in file, without comments: ', total_length)
