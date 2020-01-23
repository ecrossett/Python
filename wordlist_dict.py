def merge_dict(*words):
    '''This function takes a variable number of lists as input arguments
    and returns a dictionary where the words are the keys and the values
    are the total count of each word in all of the lists. Each list can 
    contain any number of words.'''
    
    words = list(words)    # convert agg tuple of lists into consolidated list
    keys = []              # initialize keys list as empty
    
    for i in words:        # iterate through each element of total words list
        
        keys = keys + i    # compile into list for counting keys

# use comprehension to return dictionary where keys are converted to set
# and the count of each key is the value.       
    return dict((x,keys.count(x)) for x in set(keys))        
