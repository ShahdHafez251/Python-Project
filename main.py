#!/bin/python3

from employee_data import *
from operations import *
from authentication import *
import getpass
##################################################
print("##################################################\n")
print("welcome to the Employee Management System\n please login to continue\n")
#enter the id and password
em_id = int(input("enter your employee ID : "))
x = int(getpass.getpass("enter pass\n"))
#check if id and passwors are correct
result = check_pass_id(x ,em_id)
#if true the login succesful
if result == 1 :
    print("Enter Successful !")
#else then you have 3 trials
else : 
    for trial in range(3) :
        print("wrong password! please try again")
        em_id = int(input("enter your employee ID : "))
        x = int(getpass.getpass("enter pass\n"))
        result = check_pass_id(x ,em_id)
        if result ==1 :
            print("Enter Successful !")
            break 
        else :
            continue 
    if result == 0 : 
        print("You have exceeded the allowed number of times!")
#############################################
#now after entring the correct paswword
if (result != 0) :
    t = True
    while t :
        print("###############################################################")
        print("Select an option:\n 1. Display Employee Information\n 2. Calculate Bonus\n 3. calculate Discount\n 4. Remind Legal Holidays\n 5. Exit")
        y= int(input("enter your choice :"))
        em_id = int(input("enter your employee ID : "))
        if (y ==1) :
            k=display(em_id)
            if (k == True) :
                z=input("press enter to return to the main menu  ")
                if (z == "\n") :
                    break
            else :
                print(" worng ID ! please try again\n")
        elif y==2 :
            k=bonus(em_id)
            if (k == True) :
                z=input("press enter to return to the main menu  ")
                if (z == "\n") :
                    break
            else :
                print(" worng ID ! please try again\n")
        elif y==3 :
            k=discount(em_id)
            if (k == True) :
                z=input("press enter to return to the main menu  ")
                if (z == "\n") :
                    break
            else :
                print(" worng ID ! please try again\n")
        elif y==4 : 
            k=legal_hol(em_id)
            if (k == True) :
                z=input("press enter to return to the main menu  ")
                if (z == "\n") :
                    break
            else :
                print(" worng ID ! please try again\n")
        elif y ==5 :
            print("Thank you for using the Employee Management System. GoodBye!\n")
            t = False

        

            
        
        





