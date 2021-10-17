import re

pattern = re.compile('this')
string = 'search inside of this text this please'
#a = re.search('this', string)
# print(a.span())
a = pattern.search(string)
b = pattern.findall(string)
print(b)
