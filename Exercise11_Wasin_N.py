numberInput = int(input("Please enter a number : "))
for x in range(numberInput):
    numberInput -= 1
    print(" "*numberInput,"*"*((2*x)+1))
