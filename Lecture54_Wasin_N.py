def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1001":
        return True
    else:
        return False
def showMenu():
    print("Welcome toABC shop")
    print("1.Vat Calculator")
    print("2.Price Calculator")
def menuSelect():
    userSelect = int(input(">>"))
    return userSelect
def vatCalculate(totalprice):
    vat = 7
    result = totalprice+(totalprice*vat/100)
    return result
def priceCalculate():
    price1 = int(input("Please input price1:"))
    price2 = int(input("Please input price1:"))
    return vatCalculate(price1+price2)

if login():
    showMenu()
    if menuSelect()==1:
        vatcal = int(input("Price (THB) : "))
        print(vatCalculate(vatcal))
    else: print(priceCalculate())
else:print("login not success")


