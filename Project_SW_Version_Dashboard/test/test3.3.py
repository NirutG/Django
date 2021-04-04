from lxml import etree
tree = etree.parse("Project_SW_Version_Dashboard\src\web_page.html")

# lxml
title_element = tree.find('head/title')
print(f'lxml_1= {title_element}')
print(f'lxml_2= {title_element.text}')

p_element = tree.find('body/p')
print(f'lxml_3= {p_element.text}')

# xpath
title_element = tree.find('//title')
print(f'xpath_1= {title_element}')
print(f'xpath_2= {title_element.text}')

a_element = tree.find('//a')
print(f'xpath_3= {a_element}')
print(f'xpath_4= {a_element.text}')

list1_element = tree.find('//li[1]')
list2_element = tree.find('//li[2]')
print(f'xpath_5= {list1_element}')
print(f'xpath_6= {list1_element.text}')
print(f'xpath_7= {list2_element}')
print(f'xpath_8= {list2_element.text.strip()}')

print(f'xpath_9= {list2_element.text.strip()} {a_element.text}')

p_element = tree.find('//p')
print(f'xpath_10= {p_element.text}')
p_element = tree.xpath('//p/text()')[0]
print(f'xpath_11= {p_element}')
li_item = tree.xpath('//li/text()')
print(f'xpath_12= {li_item}')