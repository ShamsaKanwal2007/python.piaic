def addition(x,y):
    print(x+y)

def subtraction(x,y):
    print(x-y)

def multiply(x,y):
    print(x*y)    

def division(x,y):
    print(x/y)       

num1 = eval(input("ENTER YOUR FIRST NUMBER --->"))
num2 = eval(input("ENTER YOUR SECOND NUMBER --->"))

print("SELECT THE OPTION:")
print("1. addition")
print("2. subtraction")
print("3. multiply")
print("4. division")
print("5. exit")

while(True):
    choice=int(input("ENTER THE CHOICE FROM (1/2/3/4/5/6)-->"))
    if choice in (1,2,3,4,5):
        if choice==1:
            print("addition of two number", num1, "and",num2, "is-->", addition(num1,num2))
        elif choice==2:
            print("subtraction of two number", num1, "and",num2, "is-->", subtraction(num1,num2)) 
        elif choice==3:
            print("multiply of two number", num1, "and",num2, "is-->", multiply(num1,num2))       
        elif choice==4:
            print("division of two number", num1, "and",num2, "is-->", division(num1,num2)) 
        elif choice==5:
            print("THANK YOU :")
            exit()
    else:
        print("Invalid choice try again:")    