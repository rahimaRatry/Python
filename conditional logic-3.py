#take an character from user and check if the alphabet is in upper case/ lower case or nothing.

print("Please, Enter the character:")
character = input()

if character>='a' and character<='z':
    print("Lower case")
elif character>='A' and character<='Z':
    print("Upper case")
else:
    print("Nothing")