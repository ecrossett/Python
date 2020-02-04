# This script substitutes file1, file2, file3, etc. with 
# file01, file02, file03, etc. without affecting names like
# file10, file20, file30, etc. Compiles first.
import re
names = 'file1, file2, file3, file10, file20, file30'
newnames = re.compile(r'file(\d{1}\D)')
newnames.sub(r'file0\1',names)

## Alternate solution ##

# This script substitutes file1, file2, file3, etc. with 
# file01, file02, file03, etc. without affecting names like
# file10, file20, file30, etc. 
import re
names = 'file1, file2, files3, files10, file20, file30'
re.sub(r'file(\d{1}\D)',r'file0\1',names)
