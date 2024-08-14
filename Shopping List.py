import os
nm=[]
pr=[]
opr=[]
qu=[]
# *******************
def addpro():
    name=input("Enter Name of the Product:")
    if(name in nm):
        os.system('cls')
        print("Product is already added!\n")
    else:
        nm.append(name)
        qua=int(input("Enter Quatity:"))
        qu.append(qua)
        price=int(input("Enter Price of the Product:$"))
        opr.append(price)
        pr.append(price*qua)
        os.system('cls')
def editpro():
    i=int(input("Ener Index of the product:"))
    if(len(nm)>i and i>-1):
        w=int(input("What you want to edit:\n1. Name\n2. Price\n3. Quantity\n4. All\n-->"))
        if(w==1):
            nm[i]=input("Enter New Name:")
        elif(w==2):
            opr[i]=int(input("Enter New Price:"))
            pr[i]=opr[i]*qu[i]
        elif(w==3):
            qu[i]=int(input("Enter New Quantity:"))
            pr[i]=opr[i]*qu[i]
        elif(w==4):
            nm[i]=input("Enter New Name:")
            opr[i]=int(input("Enter New Price:"))
            qu[i]=int(input("Enter New Quantity:"))
            pr[i]=opr[i]*qu[i]
        os.system('cls')
        print("Changes were Successful!\n")
    else:
        os.system('cls')
        print("Invalid Index Number!\n")
def deletepro():
    i=int(input("Enter Index of the Product:"))
    nm.pop(i)
    pr.pop(i)
    qu.pop(i)
    opr.pop(i)
    os.system('cls')
    print("Product Remove Successfully!\n")
    print("********************")
def sumofpro():
    os.system('cls')
    print("\n\n********************\n\tShopping Amount")
    for i in range(0,len(nm)):
        print(i,". ",nm[i],opr[i],"X",qu[i],"->$",pr[i])
    print("Total Amount -->$",sum(pr))
    print("********************")
def clearpro():
    rp=input("Are you Sure?(y/n):")
    if rp=='y':
        nm.clear()
        pr.clear()
        opr.clear()
        qu.clear()
        os.system('cls')
        print("\nChanges Made Were Successful!!\n")
    elif rp=='n':
        os.system('cls')
        print("\nChanges Abort!\n")
###################
while True:
    print("\t\tShopping List")
    if(len(nm)>0):
        print("\nProduct:")
        for i in range(0,len(nm)):
            print(i,". ",nm[i],opr[i],"X",qu[i],"\n   Price-->$",pr[i])
        print("********************")
    op=int(input("1.Add Product\n2.Edit Product\n3.Remove Product\n4.Total Amount\n5.Clear All Products\n6.Exit Program\n-->"))
    if(op==1):
        addpro()
    if(op==2):
        editpro()
    elif(op==3):
        deletepro()
    elif(op==4):
        sumofpro()
    elif(op==5):
        clearpro()
    elif(op==6):
        exit(0)
