import re

pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
string = 'Amit'
Pattern2 = re.compile(r"([A-Za-z0-9$%#@]{7,}[0-9])")
# a = pattern.search(string)
password = 'bhbhkskked8962%$8'
a = pattern.search(string)
check = Pattern2.fullmatch(password)
print(check)
# [A-Za-z0-9$%  # @]{7,}[0-9]
