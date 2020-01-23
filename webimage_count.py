# This script will list and count all of the images in a given
# HTML web page or file.

import re, urllib.request, sys, string                 # import modules
url = 'https://www.berkeley.edu/'                      # initialize web page url
imagescrape = re.compile(r'<img.*?>')             # compile re: starting with <img, ending with >
try:                                                   # try/except clause to handle access error
    f = urllib.request.urlopen(url)
except IOError:
    sys.stderr.write('could not connect to %s ' % url)
    sys.exit(1)
contents = str(f.read())                               # read entire contents of page, conv to str
f.close()                                              # close file
images = imagescrape.findall(contents)                 # create list of all matches
count = len(images)                                    # length of list = image count

print('%d total images on page %s\n' % (count, url))   # display total count

for i in range(count):                                 # iterate though each list element 
    print('image %d: %s\n' % (i+1,images[i]))          # print url and image num for each one
