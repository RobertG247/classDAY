def main():
        A = [4, 7, 3, 9, 8]
        i = 0
        max = A[0]
        while i < len(A)-1:
                i = i + 1
                if A[i] > max:
                        max = A[i]
        print ("the maximum positive", max)

main()


# i = 1
# while i <= 1:
#      print ("minimum number in the list")
