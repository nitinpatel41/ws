# This is my shopping list
shoplist = ['apple', 'mango', 'carrot', 'banana']
print('I have', len(shoplist), 'items to purchase.')
print('These items are:', end=' ')
for item in shoplist:
    print(item, end=' ')
print('\nI also have to buy rice.')
shoplist.append('rice')
print('My shopping list is now', shoplist)
print('I will sort my list now')
shoplist.sort()
print('Sorted shopping list is', shoplist)
print('The first item I will buy is', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('I bought the', olditem)
print('My shopping list is now', shoplist)


x = [0, 5 , 9 , 8 , 2 , 3]
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
print(x[1:])
print(x[2::2])
=======
print("Hello Nitin")
print(x[1:])
>>>>>>> 378c475c56cca21585684f94b17f304b3023ab5e
=======
print("Hello Nitin")
print(x[1:])
>>>>>>> 378c475c56cca21585684f94b17f304b3023ab5e
=======
print(x[1:])
print(x[2::2])


>>>>>>> nitin
