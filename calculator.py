def calculate():
    print("------------------------")
    print("----BASIC CALCULATOR----")
    print("------------------------")
    print()

    num1 = float(input("Enter the 1st number: "))
    num2 = float(input("Enter the 2nd number: "))
    symbol = input("Enter a symbol (+ - * /): ")
    total = 0


    if symbol == "+":
        total = num1 + num2
    elif symbol == "-":
        total = num1 - num2
    elif symbol == "*":
        total = num1 * num2
    elif symbol == "/":
        total = num1 / num2
    else:
        print("You must enter a valid symbol.")
        symbol = input("Enter a symbol (+ - * /): ")
    print(f"Your total is {total:.2f}.")

calculate()

while True:
    restart = input("Would you like to calculate again? Y/N: ")
    if restart == "Y":
        calculate()
    if restart == "N":
        print("Thank you for using my calculator. Have a wonderful day!")
        break


