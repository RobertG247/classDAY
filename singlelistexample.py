def main():
    listprogram()

def listprogram():
    newList=[]

exit=False
while (exit == False):
    newList.append(input("what is your name?"))
    newList.append(input("what is your favorite color?"))
    decision = input("press Q to quit, all other input continues")
    if decision == "q" or decision == "Q":
       exit = True
length = len(newList)
for a in range(0, length, 2):
    print(newList[a], "favorite color is", newList[a])
main()
