import re


reg_ex = re.compile(r'(\d{3})-(\d{3}-\d{3})')
num = reg_ex.search('My num is 979-718-020')
c = num.group()
print(c)

d = reg_ex.sub(r'\2', 'My num is 979-718-020')
print(d)

# a, b = num.groups()
# print(b)
