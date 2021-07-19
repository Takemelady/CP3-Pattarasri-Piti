usernameInput = input("Username :")
passwordInput = input("Password :")
if usernameInput  == "admin" and passwordInput == "1234":
    print("Done !")
    if True :
        print("====Welcome to Vegetables Mall====")
        print("1. Carrot           ","Price/Unit:","10")
        print("2. Cucumber         ","Price/Unit:","5")
        print("3. Basil            ","Price/Unit:","5")
        priceCarrot = 10
        priceCucum = 5
        priceBasil = 5
        totalPriceCarrot = 0
        totalPriceCucum = 0
        totalPriceBasil = 0
        userSelectInput = int(input("Select Product:"))

        while userSelectInput != 0:
            if userSelectInput == 1 :
                userAmountInput = int(input("Carrot Amount:"))
                totalPriceCarrot = userAmountInput * priceCarrot
                print("Product in Your Cart")
                print("1. Carrot","Amount: ",userAmountInput,"Total Price: ",totalPriceCarrot)
                userSelectInput = int(input("เลือกสินค้าอื่นๆเพิ่มเติมหรือไม่ ไม่รับกด 0:"))
            elif userSelectInput == 2 :
                userAmountInput = int(input("Cucumber Amount:"))
                totalPriceCucum = userAmountInput * priceCucum
                print("Product in Your Cart")
                print("2. Cucumber","Amount: ",userAmountInput,"Total Price: ",totalPriceCucum)
                userSelectInput = int(input("เลือกสินค้าอื่นๆเพิ่มเติมหรือไม่ ไม่รับกด 0:"))
            elif userSelectInput == 3 :
                userAmountInput = int(input("Basil Amount:"))
                totalPriceBasil = userAmountInput * priceBasil
                print("Product in Your Cart")
                print("3. Basil","Amount: ",userAmountInput,"Total Price: ",totalPriceBasil)
                userSelectInput = int(input("เลือกสินค้าอื่นๆเพิ่มเติมหรือไม่ ไม่รับกด 0:"))
        else:
            totalOrderPrice = totalPriceCarrot + totalPriceCucum + totalPriceBasil
            print("Total Price :", totalOrderPrice, "THB")
else:
    print("รหัสผ่านผิดพลาด")