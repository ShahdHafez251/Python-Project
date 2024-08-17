#!/bin/python3

m = {
    "ID" : 101 , 
    "Name" : "mohamed hazem mohamed" , 
    "Department" : "IOT" , 
    "salary" : "$5000" , 
    "password" : 1234 ,
    "Days of Absence" : 2
}

s = {
    "ID" : 102 , 
    "Name" : "shahd mohamed hafez" , 
    "Department" : "Embedded Systems" , 
    "salary" : "$10000" , 
    "password" : 1111 ,
    "Days of Absence" : 0
}

a = {
    "ID" : 103 , 
    "Name" : "ahmed abdel-Fattah" , 
    "Department" : "DevOps" , 
    "salary" : "$7000" , 
    "password" : 2222 ,
    "Days of Absence" : 5
}

data_empl = [m , s ,a]

###################################
def display(id) :
    k= False
    for j in data_empl :
        if id == j["ID"] :
            k = True
            for key, value in j.items():
                print(f"{key}: {value}")
    return k

#####################################
def bonus(id) :
    k = False
    for j in data_empl :
        if id == j["ID"] :
            k = True
            bonus = 0.1 * int(j["salary"].replace('$' , ' '))
            print("Bonus Calculation:\n Bonus :$" ,bonus)
    return k

######################################
def discount(id) :
    k = False
    for j in data_empl :
        if id == j["ID"] :
            k= True 
            disc = 0.05 * int(j["salary"].replace('$' , ' '))
            print("Discount Calculation:\n Discount :$" ,disc) 
    return k

#######################################
def legal_hol (id) :
    k = False
    for j in data_empl :
        if id == j["ID"] :
            k = True
            i= 10-j["Days of Absence"]
            print("Remind Legal Holidays : ",i)
    return k
###################################


