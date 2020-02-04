filename = 'test_file.txt'

def file_count(filename):
    '''This function takes a filename as input and returns a tuple containing
the total number of lines, words, and characters in the file.'''
    try:
        f = open(filename,'r')             # open file read only
    except IOError:
        print('unable to open file')
            
    all_lines = f.read()               # read all lines of the file as a string
    f.close()                          # close file
    list_lines = all_lines.split('\n') # convert into list of lines, remove '\n'

   
    lines = len(list_lines)            # return length of list => num lines
    words = len(all_lines.split())     # split string by spaces => list num words
    newlines = all_lines.count('\n')   # count total number of nls in file str
    chars = len(all_lines) - newlines  # count all chars minus newlines
     
    x = (lines, words, chars)          # define tuple
    
    return x                           # return tuple
print('lines: %d, words: %d, characters: %d' % (file_count(filename)))
