def main():
    listprogram()

def listprogram():
    nameList=[]
    colorList=[]
    exit=False
    while(exit==False):
        nameList.append(input("what is your name?"))
        colorList.append(input("what is your favorite color?"))
        decision=input("press Q to quit, all other input continues")
        if decision=="q" or decision=="Q":
         exit=True
    length=len(nameList)
    for a in range(0, length):
        print(nameList[a],"favorite color is", colorList[a])
main()


    #getname  =  input("what is your name")
    #getcolor =  input("what is your favorite color")
    #myTuple = (getname,getcolor)
    #myList = list (myTuple)
    #print (myList)
    #entry = input("if you would like to quit please type Q?")
#main()