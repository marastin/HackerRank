import sys
import xml.etree.ElementTree as etree



# Example 1
def get_attr_number(node):
    # your code goes here
    num = 0
    for element in node.iter():
        num += len(element.attrib)
    return num

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))