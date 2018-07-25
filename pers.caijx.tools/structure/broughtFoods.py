# 用于记录谁为野餐带来了什么食物
allGuest = {
    'ALice':{
        'apples':5,'pretzels':12
    },
    'Bob':{
        'ham sandwiches':3,'apples':2
    },
    'Carol':{
        'cups':3,
        'apple pies':1
    }
}

def totalBrought(guests,item):
    numBrought = 0
    for k,v in guests.items():
        numBrought = numBrought + v.get(item,0)
    return numBrought

print('Number of things being brought:')
print(' - Apples ' + str(totalBrought(allGuest,'apples')))
print(' - Cups ' + str(totalBrought(allGuest,'cups')))
print(' - Cakes ' + str(totalBrought(allGuest,'cakes')))
print(' - Ham Sandwiches ' + str(totalBrought(allGuest,'ham sandwiches')))
print(' - Apple Pies ' + str(totalBrought(allGuest,'apple pies')))