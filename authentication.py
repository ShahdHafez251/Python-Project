#!/bin/python3
from employee_data import  *
################################################3
def check_pass_id (passw ,id) :
    state= 0
    for x in data_empl :
        if x["password"] == passw and x["ID"] ==id :
            state =1
            return state 
        else :
            state =0
    return state 

        
############################################
def check_id(id) :
    for x in data_empl :
        if x["ID"] == id :
            state =1
            return state 
        else :
            state =0
    return state 

        
    

