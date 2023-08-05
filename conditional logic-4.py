#Take an input from user and check if it is a vowel/ consonant or not an alphabet.
print("please, Enter a character:")
character = input()

if character >='a' and character<='z' or character >='A' and character <='Z':
    if character in 'aeiouAEIOU':
        print("The character is  Vowel")
    else:
        print("The character is consonant")
else:
    print("the character is not an alphabet")