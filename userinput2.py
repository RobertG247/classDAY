def main():


 def numbers():
  numbers = [x, w, y, z]
i = 0
plus = numbers[0]
while i < len(numbers) - 1:
    i = i + 1
    if numbers[i] > plus:
        plus = numbers[i]
print("the maximum number in the list", plus)

minus = numbers[0]
while i > len(numbers) + 1:
    i = i - 1
    if numbers[i] < minus:
        minus = numbers[i]
print("the minimum number in the list", minus)
x = int(input("introduce a number from 1 to 100??"))
w = int(input("introduce another number from 1 to 100??"))
y = int(input("introduce another number from 1 to 100??"))
z = int(input("introduce another number from 1 to 100??"))



main()