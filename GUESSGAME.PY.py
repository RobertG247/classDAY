#def main():


 #   guess=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#    x = int(input("guess a number from 1 to 10?"))
 #   y = int(input("guess again for a number from 1 to 10?"))
  #  z = int(input("guess again for a number from 1 to 10?"))
    #while our number: 5
  #  if (x, y, z) is right print: ("congratulations you win")
   # elif (x, y, z) is wrong print ("sorry youre cold")


#main()


def main():


    validinput=False
    while(validinput==False):
        try:
            a = float(input("enter a number from 1 to 10?"))
            b = float(input("enter another number from 1 to 10?"))
            c = float(input("enter even another number from 1 to 10?"))

            validinput = True
        except:
           print("invalid input")

    print("congratulations", a * 2 + b + c)


main()


def main():
    listprogram()


def listprogram():
    newList=[] #Will contain all the names and colors

    exit=False
    while(exit==False): # runs until user wants to quit
        newList.append(input("What is your name?")) # appends to even indexes
        newList.append(input("What is your favorite color?")) # appends to odd indexes
        decision=input("press q to quit, all other input continues")
        if decision=="q" or decision=="Q": # quits when input is q or W
            exit=True
    length=len(newList)
    for a in range(0,length,2 ):
        print(newList[a],"Favorite Color is ", end="") # prints names
        print(newList[a+1]) # prints colors
main()


def main():
    listprogram()


def listprogram():
    nameList=[]
    colorList=[]
    exit=False
    while(exit==False):
        nameList.append(input("What is your name?"))
        colorList.append(input("What is your favorite color?"))
        decision=input("press q to quit, all other input continues")
        if decision=="q" or decision=="Q":
            exit=True
    length=len(nameList)
    for a in range(0,length ):
        print(nameList[a],"Favorite Color is ", colorList[a])
main()



import sys

# the following prints one system argument
def arg1():
    print(sys.argv[1])



#The following prints 2 system arguments
def arg2():
    print(sys.argv[1],sys.argv[2])

# the following reads 3 arguments and assigns them to variables.
def arg3():
    first=sys.argv[1]
    second=sys.argv[2]
    third=sys.argv[3]
    print("First argument is",first,"! The second argument is", second, " ! The third argument is", third)



# the following reads a file as an argument
def readfilearg():
    ValidFile=False
    while ValidFile==False:
        try:
            file = sys.argv[1]  # get the file from the argument
            f = open(file, "r")  # opens the file essay.txt
            print(f.read())
            ValidFile=True
        except:
            print("File not found")
            break

#uncomment whichever function call you want to run
#arg1()
#arg2()
#arg3()
readfilearg()




import sys

# the following prints one system argument
def arg1():
    print(sys.argv[1])



#The following prints 2 system arguments
def arg2():
    print(sys.argv[1],sys.argv[2])

# the following reads 3 arguments and assigns them to variables.
def arg3():
    first=sys.argv[1]
    second=sys.argv[2]
    third=sys.argv[3]
    print("First argument is",first,"! The second argument is", second, " ! The third argument is", third)



# the following reads a file as an argument
def readfilearg():
    ValidFile=False
    while ValidFile==False:
        try:
            file = sys.argv[1]  # get the file from the argument
            f = open(file, "r")  # opens the file essay.txt
            print(f.read())
            ValidFile=True
        except:
            print("File not found")
            break

#uncomment whichever function call you want to run
#arg1()
#arg2()
#arg3()
readfilearg()

def main():
    x=GrabIterations()
    GetAverage(x)
    GetAverage()

def GrabIterations():
    return int(input("How many numbers are in your set"))

def GetAverage(a):
    sum=0;
    for i in range(0,a):
        y=int(input("Enter a number"))
        print("Number",i+1,"is",y)
        sum=sum+y
    print("The average of all the numbers is",sum/a)
    if(sum/a>=75):
        print("Huzzah!")
    else:
        print("Bad News Everyone!")


main()


