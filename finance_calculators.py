import math

#this project showcase the use variables and control structure.
#this program will be use to calculate investment (ie. simple or compound) and bond repayment 
print("""investment - to calculate the amount of interest you'll earn on your investment""")
print("""bond - to calculate the amount you'll have to pay on a home loan""")

#the user will be asked to choose between investment or bond repayment calculator
finance_calculator = str(input("Enter either 'investment' or 'bond' from the menu above to proceed: "))

#to reduce error when filling in strings, all string entered by user will be converted to lower case
finance_calculator = finance_calculator.lower()

#using if statement, if user chooses 'investment', the program will be asked to input the following intergers for calculation
if finance_calculator == "investment":
    print("Please fill in the following amount for calculation.")
    p = int(input("Enter the amount of money you are depositing: "))
    r = float(input("Enter the interest rate: "))
    t= int(input("Enter the number of year/s: " ))
    interest = input("Enter your choice of interest component either 'simple' or 'compound' interest: ")
    interest = interest.lower()
    #before the calculation, user will then be asked whether they want a 'simple' or 'compound' calculation for the investment
    if interest == "simple":
        a = p*(1+ (r/100)*t)
        print("Your total investment is: ", a)
    elif interest == 'compound':
        a = p*math.pow(1+r/100,t)
        print("Your total investment is: ", a)
    else:
        print("Invalid input")
#the calculation will the be printed in the terminal whichever calculation the user chooses
#if user entered an invalid strings it will simply print "Invalid input"
                
#and user chooses 'bond' calculator, the program will be asked to input the following intergers for calculation   
elif finance_calculator == "bond":
    print("Please fill in the following amount for calculation.")
    value = float(input("Enter the present value of the house: "))
    i = float(input("Enter the interest rate: "))
    months = float(input("Enter the number of months which the bond will be repaid: "))
    interest = (i/100)/12
    repayment = (interest * value)/(1 -(1 + interest)**(-months))
    print("Your total payment each month is: ", repayment)
else:
    print("Invalid input")
#the calculation will the be printed in the terminal whichever calculation the user chooses
#if user entered an invalid strings it will simply print "Invalid input"        
