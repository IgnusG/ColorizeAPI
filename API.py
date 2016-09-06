from lxml import html
import requests
import sys

class ColorizerAPI:

    colorizerURL = "https://alexbeals.com/projects/colorize/search.php?q="

    @staticmethod
    def query(query):
        page = requests.get(ColorizerAPI.colorizerURL + query)
        tree = html.fromstring(page.content)

        color_code = tree.xpath('//span[@class="hex"]/text()')[0]

        print(color_code)

if len(sys.argv) != 2:
    print "Please provide the query parameter"
else:
    ColorizerAPI.query(sys.argv[1])
