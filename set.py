bri = set(['brazil', 'russia', 'india'])
print(bri)

if 'usa' in bri :
    print("True")
else:
    print("False")

bric = bri.copy()
print(bric)
bric . add('usa')
bri . remove('russia')
print(bri & bric)  #OR bri.intersection(bric)

print('Simple Assignment')
shoplist = ['apple', 'mango', 'carrot', 'banana']
mylist = shoplist
del shoplist[0]
print('shoplist is', shoplist)
print('mylist is', mylist)
x = "__*__".join(mylist)
print(x)
# x = [0,1,2,3,4]
# temp = x
# print(x)
# print(temp)
# x.remove(3)
# print(x)
# print(temp)


name = 'Swaroop'
if name.startswith('Swa'):
    print('Yes, the string starts with "Swa"')
if 'a' in name:
    print('Yes, it contains the string "a"')
if name.find('war') != 2:
    print('Yes, it contains the string "war"')
else:
    print("Noo")
print(name.find('roop'))
