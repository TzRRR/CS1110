# Tianze Ren (tr2bx)  Morgan Booth (mb2ej)
import urllib.request
import re

stream = urllib.request.urlopen('http://cs1110.cs.virginia.edu/emails.html')
email = re.compile(r"\s\b([a-zA-Z0-9]+[-])*[a-zA-Z0-9]+@[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)+")
for line in stream:
    decoded = line.decode('UTF-8').strip()
    matches = email.findall(decoded)
    print(matches)
