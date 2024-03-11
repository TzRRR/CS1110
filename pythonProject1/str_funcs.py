# Reilly Tiltmann xbr8up
# Tianze Ren tr2bx

#ellipsis
def ellipsis(s):
    return s[:2] + "..." + s[-2:]


#eighteen
def eigteen(s):
    number = str(len(s) - 2)
    return s[0] + number + s[-1:]


#alliterative
def allit(s, t):
    s = s.lower()
    t = t.lower()
    s_letter = s[0] != "a" or s[0] != "e" or s[0] != "i" or s[0] != "o" or s[0] != "u"
    t_letter = t[0] != "a" or t[0] != "e" or t[0] != "i" or t[0] != "o" or t[0] != "u"
    output = s[0] == t[0]
    return s_letter and t_letter and output

