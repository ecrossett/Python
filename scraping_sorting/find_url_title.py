import re, urllib, sys

def get_webtitle(url):
    '''This Python function returns the title of a webpage,
        given a user input url.'''
    
    # Define and compile parameters for scraping title
    titleFind = re.compile('<title>(.*)</title>',re.I)
    
    # Throw exception if unable to connect to the url
    try:
        f = urllib.request.urlopen(url)
    except IOError:
        sys.stderr.write("could not connect to %s " % url)
        sys.exit(1)
    
    # Read contents from the site into a string
    website_contents = str(f.read())
    f.close()

    # Store contents and print results
    titlePrint = titleFind.findall(website_contents)
    return titlePrint[0]
