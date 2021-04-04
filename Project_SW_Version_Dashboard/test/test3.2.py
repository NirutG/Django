from typing import Text
from lxml import etree
tree = etree.parse("Project_SW_Version_Dashboard\src\web_page.html")

title_element = tree.find('head/title')
p_element = tree.find('body/p')

list_item = tree.findall("body/ul/li")
   
print(title_element.text)
print(p_element.text)

for li in list_item:
    a = li.find('a')
    if a is not None:
        print(f'{li.text.strip()} {a.text}')
    else:
        print(li.text)
