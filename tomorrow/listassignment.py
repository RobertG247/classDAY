def main():
    iterations= getiterations()
    getaverage(iterations)


def getiterations():
    return int(input("how many numbers will you add?"))


def getaverage(y):
    firstlist=[]

    for a in range(0,y):
        testscore=int (input("what is your test score?"))
        firstlist.append(testscore)

    firstlist.append(100)
    lengthoflist= len(firstlist)
    sum=0
    for c in range(0, lengthoflist):
        sum=sum+firstlist[c]

    print(sum)


main()
