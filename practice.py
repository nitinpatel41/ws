# name = "Nitin"
# age = 21
# print('{0} was {1} years old'.format(name,age))


name = "Nitin"
age = 21
print(f"{name} is {age} years old")
print('This is the first line\nThis is the second line')
i = 5
print('Value is', i)
print('I repeat, the value is', i)



length = 5
breadth = 2
area = length * breadth
print('Area is', area)
print('Perimeter is', 2 * (length + breadth))





number = 23
running = True
while running:
    guess = int(input('Enter an integer : '))
    if guess == number:
         print('Congratulations, you guessed it.')
# this causes the while loop to stop
         running = False
    elif guess < number:
        print('No, it is a little higher than that.')
    else:
        print('No, it is a little lower than that.')

else:
    print('The while loop is over.')
# Do anything else you want to do he




while True:
    s = input('Enter something : ')
    if s == 'quit':
        break
    print('Length of the string is', len(s))
print('Done')