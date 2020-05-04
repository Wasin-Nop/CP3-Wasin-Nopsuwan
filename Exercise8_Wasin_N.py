usernameInput = input("Username : ")
passwordInput = input("Password : ")
if usernameInput == "admin" and passwordInput == "1001" :
    apple = 20
    banana = 30
    mango = 35
    print("Welcome toABC shop")
    print("1.Apple 20 THB")
    print("2.Banana 30 THB")
    print("3.Mango 35 THB")
    userSelect = int(input(">>"))
    if userSelect == 1:
        buyApple = int(input("How many do you want? "))
        resultApple = buyApple*apple
        print("Total Price :",resultApple,"THB")
    elif userSelect == 2:
        buyBanana = int(input("How many do you want? "))
        resultBanana = buyBanana*banana
        print("Total Price :",resultBanana,"THB")
    elif userSelect == 3:
        buyMango = int(input("How many do you want?" ))
        resultMango = buyMango*mango
        print("Total Price :",resultMango,"THB")
    else:
        print("Please login and choose the number 1-3 again")
else :
    print("Access Denie")
