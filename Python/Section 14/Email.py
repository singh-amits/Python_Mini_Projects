import re

pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
string = 'b@b.com'
#a = re.search('this', string)
# print(a.span())
a = pattern.search(string)
print(a)
