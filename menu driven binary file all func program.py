"""menu driven program to
add,modify,delete,update and search in binary file
"""
import os #operating system func
import pickle
#Accepting data for dictionary
def InsertRec() :
    r=int(input("enter roll no."))
    n=input("enter name")
    m=int(input("enter marks"))
    data={"Rollno":r,"Name":n,"Marks":m}
    f=open("D:\\Program Files\\bi_student.dat","ab")
    pickle.dump(data,f)
    f.close()
    print("---------------------------------------------------------------")

    
#displaying record from file
def ReadRec():
    f=open("D:\\Program Files\\bi_student.dat","rb")
    while True :
        try :
            data=pickle.load(f)
            print("RollNo",data["Rollno"])
            print("Name",data["Name"])
            print("Marks",data["Marks"])
        except EOFError :#end of file
            break
    f.close()
    print("---------------------------------------------------------------")


#searching record base on rollno from file
def SearchRollno(r):
    f=open("D:\\Program Files\\bi_student.dat","rb")
    flag=False
    while True :
        try :
            data=pickle.load(f)
            if data["Rollno"]==r :
                print("RollNo",data["Rollno"])
                print("Name",data["Name"])
                print("Marks",data["Marks"])
                flag=True
        except EOFError :
             break
    if flag==False:
        print("data not found")
    f.close()
    print("---------------------------------------------------------------")


#Marks modificattion based on rollno no from file
def UpdateMarks(r,m):
    f=open("D:\\Program Files\\bi_student.dat","rb")
    reclst=[]
    while True:
        try:
            data=pickle.load(f)
            reclst.append(data)
        except EOFError :
             break
    f.close()
    for i in range(len(reclst)):
        if reclst[i]["Rollno"]==r:
            reclst[i]["Marks"]=m
    f=open("D:\\Program Files\\bi_student.dat","wb")
    for x in reclst:
        pickle.dump(x,f)
    f.close()
    print("---------------------------------------------------------------")

#Removing/Deleting records based on rollno from file
def DelRec(r):
    f=open("D:\\Program Files\\bi_student.dat","rb")
    reclst=[]
    newlst=[]
    while True:
        try:
            data=pickle.load(f)
            reclst.append(data)
        except EOFError:
             break
    f.close()
    f=open("D:\\Program Files\\bi_student.dat","wb")
    for i in range(len(reclst)):
        if reclst[i]["Rollno"]==r:
            continue
        newlst.append(reclst[i])
    for x in newlst:
        pickle.dump(x,f)
    f.close()
    print("---------------------------------------------------------------")
while True:
    print("1. Add Record")
    print("2. Display Record")
    print("3. Search Record")
    print("4. Change Record")
    print("5. Remove Record")
    print("0. To EXIT ")
    choise=eval(input("enter your choise"))
    if choise==0:
        break
    elif choise==1:
        InsertRec()
    elif choise==2:
        ReadRec()
    elif choise==3:
        a=eval(input("enter Rollno to search"))
        SearchRollno(a)
    elif choise==4:
        a=eval(input("enter Rollno "))
        b=eval(input("enter Marks to Change"))
        UpdateMarks(a,b)
    elif choise==5:
        a=eval(input("enter Rollno to remove"))
        DelRec(a)
