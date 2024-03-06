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

parser = MyHTMLParser()
N = int(input())
for _ in range(N):
    S = input()
    parser.feed(S)
    