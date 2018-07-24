import random

message = [
    'It is certain',
    'It is decidely so',
    'Yes defiitely',
    'Reply hazy try again',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful'
]

print(message[random.randint(0,len(message) - 1)])