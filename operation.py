import math


def main():
    
    print("\n\nMenu of Operations:\n\tadd\n\tsubtract\n\tmultiply\n\tdivide\n\tfloored division\n\tmod\n\tpower\n\tsquare root")
    
    operationList = [ "add", "subtract", "multiply", "divide", "floored division", "mod", "power", "square root"]
    operatorList = ["plus", "minus", "times", "divided by", "divided then floored by", "modulo", "to the power of", "to the root of"]
    
    operation = input("What operation would you like to do?\n")


    if operation in operationList:
        num1 = int(input("First Number:"))
        num2 = int(input("Second Number:"))
        
        if operation == operationList[0]:
            print(f"{num1} {operatorList[0]} {num2} = {num1 + num2}")
        elif operation == operationList[1]:
            print(f"{num1} {operatorList[1]} {num2} = {num1 - num2}")
        elif operation == operationList[2]:
            print(f"{num1} {operatorList[2]} {num2} = {num1 * num2}")
        elif operation == operationList[3]:
            print(f"{num1} {operatorList[3]} {num2} = {num1 / num2}")
        elif operation == operationList[4]:
            print(f"{num1} {operatorList[4]} {num2} = {num1 // num2}")
        elif operation == operationList[5]:
            print(f"{num1} {operatorList[5]} {num2} = {num1 % num2}")
        elif operation == operationList[6]:
            print(f"{num1} {operatorList[6]} {num2} = {num1**num2}")
        elif operation == operationList[7]:
            print(f"{num1} {operatorList[7]} {num2} = {num1**(1/num2)}")
    else:
        print("Unknwon operation please try again.")

    input("Enter to Restart")
    main()

main()