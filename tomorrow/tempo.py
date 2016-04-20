def Temperature():



    entry="yes"
    while (entry=="yes" or  entry=="Yes" ):
        x = float(input("what temperature is it outside in grades fahrenheit??"))
        y=(x-32)/ 1.8
        print ("the temperature in celsius is", y)
        entry=input("continue yes or no?")
Temperature()









