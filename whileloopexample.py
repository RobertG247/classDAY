#def listprogram():
    #nameList=[]
#    colorList=[]
 #   exit=flase
  #  while(exit==False):
   #     nameList.append(input("what is your name?"))
    #    colorList.append(input("waht is your favorite color?"))
     #   decision=input("press Q to quit, all other input continues")
        #if decision=="q" or decision=="Q"
   # exit=True
    #length=len(nameList)
    #for a in range(0, length):
     #   print(nameList[a],"favorite color is", colorList[a])
# main()

#myTuple = (1,2,3)
#myList = list (myTuple)
#myList.append(4)
#print (myList)

#def main():
 #   getname  =  input("what is your name")
  #  getcolor =  input("what is your favorite color")
   # print(getname,getcolor)
   # entry = input("if you would like to quit please type Q?")
# main()

#def listprogram():
    #nameList=[]
    #colorList=[]
    #exit=flase
    #while(exit==False):
        #nameList.append(input("what is your name?"))
        #colorList.append(input("waht is your favorite color?"))
        #decision=input("press Q to quit, all other input continues")
        #if decision=="q" or decision=="Q"
    #exit=True
    #length=len(nameList)
    #for a in range(0, length):
        #print(nameList[a],"favorite color is", colorList[a])

def main():
    listprogram()


def listprogram():
    nameList = []
    colorList = []
    exit = False
    while (exit == False):
        nameList.append(input("what is your name?"))
        colorList.append(input("what is your favorite color?"))
        decision = input("press Q to quit, all other input continues")
        if decision == "q" or decision == "Q":
            exit = True
    length = len(nameList)
    for a in range(0, length):
        print(nameList[a], "favorite color is", colorList[a])


main()
