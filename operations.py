#!/bin/python3

from employee_data import *
######################################################
def add_emplo(name , ID ,Department , salary , passw ,d_o_abd):
    new_member = {
        "ID" : ID , 
        "Name" : name , 
        "Department" : Department , 
        "salary" : salary , 
        "password" : passw ,
        "Days of Absence" : d_o_abd 
    }
    data_empl.append(new_member)

########################################################

def remove_emplo(ID) :
    for n in data_empl :
        if n["ID"] == ID :
            data_empl.remove(n)
            break
    
    print("employee is removed !\n")

######################################################


