# Jeremiah Soyebo - 1902930 #
passwordInput = str(input())

for character in passwordInput:
    if character == 'i':
        passwordInput = passwordInput.replace('i', '!')   # change i to ! #
    if character == 'a':
        passwordInput = passwordInput.replace('a', '@')  # change a to @ #
    if character == 'm':
        passwordInput = passwordInput.replace('m', 'M')  # change m to M #
    if character == 'B':
        passwordInput = passwordInput.replace('B', '8')  # change B to 8 #
    if character == 'o':
        passwordInput = passwordInput.replace('o', '.')

passwordInput = (passwordInput + 'q*s')

print(passwordInput)
