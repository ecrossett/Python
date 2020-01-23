def convertible_string(string_input):
    '''This function takes a string as an input and attempts to convert
to a number.  Uses try/except clause to handle exception.''' 
    try:
        # convert input string to floating point number
        num = float(string_input)
        
        # if successful we will print this message:
        print('the string: "%s", was successfully converted to the number %.2f' % (string_input, num))
        
    except ValueError:
        # if it fails we instead print this message: 
        print('sorry, could not convert the string: "%s" to a number' % string_input)
        

def string_test(string_input):
    '''This function takes a string as an input and will test if a string
input is a number or not.  No need for try/except clause in this case.'''
    
    # test to see if string input is an integer:
    if string_input.isdigit():
        # if successful we will convert to int and print this message:
        num = int(string_input)
        print('the string: "%s", was successfully converted to the integer %d' % (string_input, num))
    
    # test to see if string input is a real number:
    elif string_input.replace('.','',1).isdigit():
        # if successful we will convert to float and print this message:
        num = float(string_input)
        print('the string: "%s", was successfully converted to the real number %.2f' % (string_input, num))
    
    else:
        # if it fails we instead print this message:
        print('sorry, could not convert the string: "%s" to a number.' % string_input)
        
