import random

asker=0
figure=random.randint(1,10)
print(figure)
print ("pick a number?")
while asker < 4:
    print("guess which number it is?")
    pick = input()
    pick =int(pick)
    asker = asker + 1

    if pick == figure +1 or pick== figure - 1:
       print("your guess is hot!")
    if pick == figure + 2 or pick == figure - 2:
       print("your guess is warm!")
    elif pick > figure + 3 or pick < figure - 3:
         print ("your guess is cold!")
    if pick == figure:
      print('you got it!!!')
      break

if pick != figure:
    print('tough luck you lost!!!')