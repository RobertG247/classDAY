#def main():
 #   w = input("what is the value of A?")
  #  x = int(input("what is the value of B?"))
   # y = int(input("what is the value of C?"))
    #z = int(input("what is the value of D?"))
  #  formula = (A*D**2)+(B*D)+C
   # print ()

def main():
    try:
        w = int(input("what is the value of A?"))
        x = int(input("what is the value of B?"))
        y = int(input("what is the value of C?"))
        z = int(input("what is the value of D?"))
        formula = ((w*z**2)+(x*z)+y)
        print ("the following quadratic was entered:((w*z**2)+(x*z)+y)", "the value of the quadratic is", formula)
    except:
        print("e")



main()