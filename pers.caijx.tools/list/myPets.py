myPets = ['Zophie','Pooka','Fat-tail']
print('Enter a per name:')
name = input()
if name not in myPets:
    print('I do not hava a pet named ' + name)
else:
    print(name + ' is my pet.')