def merge_lists(*lists):
    '''This function takes unspecified num of lists and merges all elements
into a single list.'''
    final_list = []                  # initialize final list
    
    for i in lists:                  # iterate over each element of each list
        final_list = final_list + i  # add each element to final list  
     
    return list(set(final_list))     # set function removes duplicates
    
