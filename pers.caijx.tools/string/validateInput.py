#反复询问用户年龄和口令，直到他们提供有效的输入

while True:
    print('Enter your age:')
    age = input()
    if age.isdecimal():
        break
    print('Please enter a number for your age.')

while True:
    print('Select a new password(letters and numbers only):')
    password = input()
    if password.isalnum():
        break
    print('Password can only have letters and numbers')