# This script matches strings that are either all lowercase or
# all uppercase letters. Returns a numbered list of each match.
import re
case_match = re.compile(r'\b([a-z]+|[A-Z]+)\b')
txt = 'test Test TEST 1234.test am AM.Am 1234 parrot 9 #ab% niner wEl'
nextmatch = txt
mtch = case_match.search(nextmatch)

count = 1
while mtch:
    print('match %d: %s' % (count,mtch.group(0)))
    count = count + 1
    nextmatch = nextmatch[mtch.end(0) + 1:]
    mtch = case_match.search(nextmatch)

## Alternate Solution ##

# This script matches strings that are either all lowercase or
# all uppercase letters. Returns a single list with each match
# as an element of the list.

import re
case_match = re.compile(r'\b([a-z]+|[A-Z]+)\b')
txt = 'test Test TEST 1234.test am AM.Am 1234 parrot 9 #ab% niner wEl'
case_match.findall(txt)
