# Jeremiah Soyebo - 1902930 #

stringInput = str(input())

stringInputNoSpace = stringInput.replace(' ','')

if stringInput.replace(' ', '')[::-1] == stringInput.replace(' ', ''):
    print(stringInput, 'is a palindrome')
else:
    print(stringInput, 'is not a palindrome')
