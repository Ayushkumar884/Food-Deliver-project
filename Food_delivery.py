def registeration():
    import json
    import datetime
    try:
        file=open("fooddeliveryuser.json","r+")
        content=json.load(file)
    except JSONDecodeError:
        content={}
    while True:
        phn=input("Enter you mobile number- ")
        if len(phn)==10:
            if phn in content.keys():
                file.seek(0)
                file.truncate()
                json.dump(content,file,indent=4)
                file.close()
                return("User already registerd, Please login to place order for food." )
                break

            else:
                paswrd=input("Enter the password- ")
                nam=input("Enter your Name- ")
                email=input("Enter your E-mail- ")
                ad=input("Enter your Address- ")
                content[phn]={"Name":nam,"Phone Number":phn,"E-mail":email,"Address":ad,"Password":paswrd,"Order-History":[]}
                file.seek(0)
                file.truncate()
                json.dump(content,file,indent=4)
                file.close()
                return("User Successfully registered.")
                break
        else:
            print("Please enter 10 digits mobile number only.")


def login():
    import json
    import datetime
    try:
        file=open("fooddeliveryuser.json","r+")
        content=json.load(file)
    except JSONDecodeError:
        content={}
        
    try:
        fp=open("fooddeliveryfood.json","r+")
        opt=json.load(fp)
    except JSONDecodeError:
        opt={}
        
    phn=input("Enter you mobile number- ")
    if len(phn)== 10:
        if phn in content.keys():
            paswrd=input("Enter your password- ")
            if content[phn]["Password"]==paswrd:
                while True:
                    print("1.) Admin")
                    print("2.) User")
                    print("3.) Exit")
                    option= input("Enter the choice- ")
                    if option=="1":
                        while True:
                            print("1.) Add new food item")
                            print("2.) Display all food item")
                            print("3.) Delete food item")
                            print("4.) Edit food item quantity")
                            print("5.) Exit")
                            re=input("Enter the option number- ")
                            if re=="1":
                                food_nm=input("Enter the Food name- ")
                                for i in opt.keys():
                                    if opt[i]["Food_Name"]==food_nm:
                                        print("This Food item already there.")
                                        break

                                else:
                                    if len(opt)==0:
                                        food_id=len(opt)+1
                                    else:
                                        maxi=max(opt.keys())
                                        food_id= int(maxi) +1
                                        
                                    quant=int(input("Please enter the food quantity- "))
                                    price=int(input("Please enter the price(per kg/piece)-"))
                                    opt[int(food_id)]={"Food_Name":food_nm, "Food_id":food_id,"Quantity":quant,"Price_per_bowl/peice":price}
                                    fp.seek(0)
                                    fp.truncate()
                                    json.dump(opt,fp,indent=4)
                                    fp.close()
                                    return("Added food item Successfully")

                            
                            elif re=="2":
                                if len(opt)==0:
                                    print("Nothing is there in  food-menu")
                                    print(opt)
                                else:
                                    print(opt)
                                
                            elif re=="3":
                                while True:
                                    t=input("Enter the food id- ")
                                    if t in opt.keys():
                                        opt.pop(t)
                                        fp.seek(0)
                                        fp.truncate()
                                        json.dump(opt,fp,indent=4)
                                        fp.close()
                                        return("The item got successfully deleted.")
                                        
                                    else:
                                        print("The Food id entered is not there in menu,Please try correct id.")
                                
                            elif re=="4":
                                while True:
                                    xc=input("Enter the food Item id- ")
                                    if xc in opt.keys():
                                        yu=int(input("Enter the Quantity of food want to add- "))
                                        opt[xc]["Quantity"]+=yu
                                        fp.seek(0)
                                        fp.truncate()
                                        json.dump(opt,fp,indent=4)
                                        fp.close()
                                        return("The quantity is successfully added to desired food item.")
                                        
                                    else:
                                        print("Enter the right food id.")

                            elif re=="5":
                                fp.seek(0)
                                fp.truncate()
                                json.dump(opt,fp,indent=4)
                                fp.close()
                                return("Exiting user...!")
                                
                            else:
                                print("Please enter right option.")
                                
                        
                    elif option=="2":
                        date=datetime.date.today().strftime('%m/%d/%y')
                        while True:
                            print("Welcome User...!")
                            print("1.) Place New Order")
                            print("2.) Order History")
                            print("3.) Update profile")
                            print("4.) Exit")
                            choice=input("Enter the option number- ")
                            if choice=="1":
                                def kot():
                                    for i in content[phn]["Order-History"]:
                                        if date in i:
                                            if i[date]["Food Name"]==food:
                                                i[date]["Quantity"]+=we
                                                opt[az]["Quantity"]-=we
                                                return("Order successful Placed")
                                                

                                        else:
                                            hj={date:{"Food Name":food,"Quantity":we}}
                                            content[phn]["Order-History"].append(hj)
                                            opt[az]["Quantity"]-=we
                                            return("Order Successfully Placed.")
                                            

                                    else:
                                        hj={date:{"Food Name":food,"Quantity":we}}
                                        content[phn]["Order-History"].append(hj)
                                        opt[az]["Quantity"]-=we
                                        return("Order Successfully Placed.")
                                        
                                        
                                for i in opt.keys():
                                    print(f"FOOD_ID- {opt[i]['Food_id']}   FOOD_ITEM- {opt[i]['Food_Name']}   INR- {opt[i]['Price_per_bowl/peice']}")
                                while True:
                                    az=input("Please Enter food id-")
                                    if az in opt.keys():
                                        food=opt[az]["Food_Name"]
                                        we=int(input("Please Enter the Quantity- "))
                                        if we<opt[az]["Quantity"]:
                                            print(kot())
                                            break
                                        else:
                                            print("Please Enter less Quantity.")
                                               
                                    else:
                                        print("Please Enter right food id")
                                
                            elif choice=="2":
                                if len(content[phn]["Order-History"])==0:
                                    print("Order History of- ",phn)
                                    print("None items present in Order History")
                                    
                                else:
                                    print("Order History of- ",phn)               
                                    print(content[phn]["Order-History"])
                                
                            elif choice=="3":
                                while True:
                                    print("1.) Change Name")
                                    print("2.) Change Mobile Number")
                                    print("3.) Change E-mail")
                                    print("4.) Change Address")
                                    print("5.) Change password")
                                    option=input("Enter the option number- ")
                                    if option=="1":
                                        new_n=input("Enter the name- ")
                                        content[phn]["Name"]=new_n
                                        print("Successfully changed Name.")
                                        break
                                    elif option=="2":
                                        while True:
                                            new_phn=input("Enter the phone number- ")
                                            if len(new_phn)== 10:
                                                k=content[phn]
                                                content.pop(phn)
                                                content[new_phn]=k
                                                content[new_phn]["Phone Number"]=new_phn
                                                file.seek(0)
                                                file.truncate()
                                                json.dump(content,file,indent=4)
                                                file.close()
                                                return("Sucessfuly changed phone number")
                                                break
                                                
                                            else:
                                                print("Please enter 10 digits mobile number only")
                                            
                                    elif option=="3":
                                        n_email=input("Enter the E-mail- ")
                                        content[phn]["E-mail"]=n_email
                                        print("Successfully changed E-mail.")
                                        break
                                        
                                    elif option=="4":
                                        n_ad=input("Enter the Address- ")
                                        content[phn]["Address"]=n_ad
                                        print("Successfully changed Address.")
                                        break
                                        
                                    elif option=="5":
                                        n_paswrd=input("Enter the Password- ")
                                        content[phn]["Password"]=n_paswrd
                                        file.seek(0)
                                        file.truncate()
                                        json.dump(content,file,indent=4)
                                        file.close()
                                        return ("Successfully changed password.")
                                        break
                                    else:
                                        print("Please enter the right option.")
                                                  
                            elif choice=="4":
                                print("Come back soon for the next meal...!")
                                break
                            
                            else:
                                print("Please enter correct option.")
                        
                    elif option=="3":
                        file.seek(0)
                        file.truncate()
                        json.dump(content,file,indent=4)
                        file.close()
                        fp.seek(0)
                        fp.truncate()
                        json.dump(opt,fp,indent=4)
                        fp.close()
                        return("Please order fast, Don't let your cravings die !")
                        break
                    
                    else:
                        print("Enter the right option.")
            
            else:
                return("Incorrect combination of mobile number and password.")
            
        else:
            return ("First Registered Yourself !")
        
    else:
        return("Please type 10 digits mobile number only.")
    

y=input("Want to the place order for food (Y/N)- ")
if y.lower()== "y":
    while True:
        print("1.) Regiseration ")
        print("2.) Login ")
        print("3.) Exit ")
        opt=input("Enter the option number- ")
        if opt=="1":
            print(registeration())
        elif opt=="2":
            print(login())
            
        elif opt=="3":
            print("Don't let your cravings die ....Bye !")
            break
            
        else:
            print("Please enter correct option number.")
    
else:
    print("See you again champ...!")
