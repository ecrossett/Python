# This script extracts the names of URLs embedded in a string

import re
URLstring = 'the website names are https://yahoo.com or www.msnbc.org as well.'
check = re.compile(r'www.\w+.\w+|http\w?://\w+.\w+')
check.findall(URLstring)
