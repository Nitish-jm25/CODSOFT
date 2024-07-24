print("SIMPLE CALCULATOR")
print("1.Addition")
print("2.Subraction")
print("3.Multiplication")
print("4.Division")
choice=int(input("enter an option{1-4} :"))
a=int(input("enter number 1:"))
b=int(input("enter number 2:"))
if choice==1:
           c=a+b
           print("solution=",c)
elif choice==2:
          c=a-b
          print("solution=",c)
elif choice==3:
         c=a*b
         print("solution=",c)
elif choice==4:
        if  b==0:
            print("Infinity")
        else:
            print("solution:",a//b)
else:
    print("Invalid option")

    
