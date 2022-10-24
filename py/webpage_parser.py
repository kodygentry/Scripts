
from SimpleWebpageParser import SimpleWebpageParser

swp = SimpleWebpageParser("https://github.com/kodygentry")
html = swp.getHTML()
print (html.find_all('a'))

## the html returned is an object of type BeatifulSoup, you can parse using BeautifulSoup syntax
## refer to its documentation for more functionalities