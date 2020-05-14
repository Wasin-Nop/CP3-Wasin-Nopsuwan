menuList=[]
priceList=[]
def showbill():
    print("---My Shop---")
    for number in range(len(menuList)):
        print(menuList[number],priceList[number])
        total = 0
        for price in priceList:
            total += price
    print("Thank you for shopping with us".center(35,"-"))
    print("Total Price :",total, "THB")
while True:
    menuName = input("Please enter menu :")
    if (menuName.lower()=="exit"):
        break
    else:
        menuPrice = int(input("Price :"))
        menuList.append(menuName)
        priceList.append(menuPrice)
showbill()
