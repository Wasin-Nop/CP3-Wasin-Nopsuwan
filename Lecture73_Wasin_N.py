systemMenu={"ข้าวหมกไก่":45,"ข้าวมันไก่ตอน":40,"ข้าวขาหมู":50,"ข้าวมันไก่ทอด":40}
menuList=[]
def showbill():
    print("---My Shop---".center(35,"-"))
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
        menuList.append([menuName,systemMenu[menuName]])
print(menuList)
showbill()