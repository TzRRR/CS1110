# Tianze Ren (tr2bx)
character = input("Enter a character: ")
width = int(input("Width: "))
if width < 2:
    width = int(input("The width should be equal or greater than 2, please type again: "))
    print(character * width)
    print(character + " " * (width - 2) + character)
    print(character * width)
else:
    print(character * width)
    print(character + " " * (width - 2) + character)
    print(character * width)
print('"' + character + '"' + ' rectangle has a width of ' + str(width))