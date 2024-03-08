# https://docs.python.org/3.9/library/html.parser.html#HTMLParser.HTMLParser
from html.parser import HTMLParser


# HackerRank
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f"Start : {tag}")
        for attr in attrs:
            print(f"-> {attr[0]} > {attr[1] if attr[1] else None}")
        
    def handle_endtag(self, tag):
        print(f"End   : {tag}")
        
    def handle_startendtag(self, tag, attrs):
        print(f"Empty : {tag}")
        for attr in attrs:
            print(f"-> {attr[0]} > {attr[1] if attr[1] else None}")
    
    def handle_comment(self, data):
        data = data.split('\n')
        if len(data) == 1:
            print(">>> Single-line Comment")
            print(data[0])
        elif len(data) > 1:
            print(">>> Multi-line Comment")
            print("\n".join(data))
    
    def handle_data(self, data):
        if data != "\n":
            print(">>> Data")
            print(data)
  

html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()
    