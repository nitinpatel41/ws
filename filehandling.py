# # 1
# f = open('poem' , 'w')
# f.write('How r u...?')
# f.close()
# # 2
# f = open('poem')
# while True:
#
#     line = f.readline()
#     if len(line) == 0:
#         break
#     print(line,end ="")
# f.close()

# 3
# with open("poem") as f:
#     for line in f:
#         print(line, end='')
#



import pickle

shoplistfile = 'shoplist.data'
shoplist = ['apple', 'mango', 'carrot']
f = open(shoplistfile, 'wb')
pickle.dump(shoplist, f)
f.close()


print(9)