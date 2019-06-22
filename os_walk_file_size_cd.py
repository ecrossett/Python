import os
location = '/Users/ed/Library/Mobile Documents/com~apple~CloudDocs/Certificates/'
count = 0
for root, dirs, files in os.walk(location):
    for file in files:
        full_path = os.path.join(root, file)
        size = os.path.getsize(full_path)
        if size == 0:
            count += 1
            print(file,size)
        #else:
            #count += 1
            #print(dirs)
            #print(full_path,size)
print('total number of zero length files: %d' % count)