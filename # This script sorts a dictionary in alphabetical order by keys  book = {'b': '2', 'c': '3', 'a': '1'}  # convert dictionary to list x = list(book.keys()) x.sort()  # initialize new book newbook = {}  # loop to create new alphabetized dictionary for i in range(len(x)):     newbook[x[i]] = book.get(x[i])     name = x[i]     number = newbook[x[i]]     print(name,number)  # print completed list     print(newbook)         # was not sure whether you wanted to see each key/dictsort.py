# This script sorts a dictionary in alphabetical order by keys

book = {'b': '2', 'c': '3', 'a': '1'}

# convert dictionary to list
x = list(book.keys())
x.sort()

# initialize new book
newbook = {}

# loop to create new alphabetized dictionary
for i in range(len(x)):
    newbook[x[i]] = book.get(x[i])
    name = x[i]
    number = newbook[x[i]]
    print(name,number)

# print completed list    
print(newbook)   
    
# was not sure whether you wanted to see each key/value pair printed during
# the loop or see the entire printed dictionary in one line
# so I did both. Also not sure why this prints book instead of newbook
# when run in the compiler even though newbook variable
# is correctly alphabetized.   
