menuList=[]
def showbill():
    print("---My Shop---")
    total = 0
    for number in range(len(menuList)):
        print(menuList[number][0],":",menuList[number][1])
        total += menuList[number][1]
    print("Thank you for shopping with us".center(35,"-"))
    print("Total Price :",total, "THB")
while True:
    menuName = input("Please enter menu :")
    if (menuName.lower()=="exit"):
        break
    else:
        menuPrice = int(input("Price :"))
        menuList.append([menuName,menuPrice])
print(menuList)
showbill()

