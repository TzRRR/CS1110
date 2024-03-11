# Tianze Ren tr2bx
import re
time = re.compile(r"([0-9]|1[0-2]):([0-5][0-9]):([0-5][0-9]) (AM|PM)")
coursetitle = re.compile(re.compile(r'a(aa)*'))
for match in re.coursetifinditer("a"):
    print(match)