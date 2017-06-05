A program which maps an optional web page.
Input file: url.txt  (In this file you can find an url for any web page you would like to map and in the next line you can set a depth)
Output file : links.txt (Here you can find all links from the map )

The program maps a web page which is given by a user in the input file(url.txt). It is implemented in Python and uses Selenium.
The webdriver opens the given page and looks up all links on it. It continues until the driver finds all the links on the given depth. 