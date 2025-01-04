"""
Basic Calculator Program

This program allows users to perform basic arithmetic operations such as addition, subtraction, multiplication, and division.
It is designed for beginners to understand Python concepts.

Developer: Mohit Kolte
Date: January 4, 2025
PythonVersion: 3.12
"""

def add(number1, number2):
    return number1 + number2
    
def sub(number1, number2):
    return number1 - number2
    
def mul(number1, number2):
    return number1 * number2
    
def div(number1, number2):
    return float(number1) / float(number2)

def main():
    while True:
        print("\nOperation :- \n1) Addition \n2) Subtraction \n3) Multiplication \n4) Division \n5) Exit")
        operation = input("Enter Operation:- ").lower()

        if operation == "exit":
            print("Thank you...!")
            break
        elif operation in ("addition", "subtraction", "multiplication", "division", "add", "sub", "mul", "div"):
            global number1, number2
            number1 = int(input("Enter the first  number: "))
            number2 = int(input("Enter the second number: "))
            try:
                if operation == 'add' or operation == 'addition':
                    print(f"The Addition of {number1} and {number2} is {add(number1, number2)}")
                elif operation == 'sub' or operation == 'subtraction':
                    print(f"The Subtraction of {number1} and {number2} is {sub(number1, number2)}")
                elif operation == 'mul' or operation == 'multiplication':
                    print(f"The Multiplication of {number1} and {number2} is {mul(number1, number2)}")
                elif operation == 'div' or operation == 'division':
                    if (number1 or number2) != 0:
                        print(f"The Division of {number1} and {number2} is {div(number1, number2)}")
                    else:
                        print("Enter a valid number, Thank you.")
                continue
            except Exception:
                print("Invalid input! Please enter numeric values.")
                break
        else:
            print("Invalid input..!")
            break
    
if __name__ == "__main__":
    print("Developed by: Mohit Kolte.")
    main()
       