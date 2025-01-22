class calculator:
    ## Constructor to initialize numbers
    def __init__(self ,n1,n2):
        self.n1=n1
        self.n2=n2
    def add(self):
        return self.n1+self.n2
    def sub(self):
        return self.n1-self.n2
    def mul(self):
        return self.n1*self.n2
    def div(self):
        if self.n2!=0:
            return self.n1/self.n2
        else:
            return "Error: Division by zero is not allowed!"
        
    ##Input taken by user

n1=float(input("enter a no:"))
n2=float(input("enter another no:"))

    #object creation   
cal1=calculator(n1,n2)
    
    #user choise to perform an operation
print("choose an operation")
print("1.add")
print("2.substract")
print("3.multiplication")
print("4.division")


choose=int(input("enter a no from 1-4: "))

    # Performing the operation based on the user's choic
if choose==1:
    print(f"addition is {cal1.add()}")
elif choose==2:
    print(f"substraction is {cal1.sub()}")
elif choose==3:
    print(f"multiplication is {cal1.mul()}")
elif choose==4:
    print(f"division is {cal1.div()}")
else:
 print("invalid choice")







        





        
