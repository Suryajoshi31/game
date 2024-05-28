#  calculator

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error!division by zero"
    else:
        return x / y

def main():
    print("Select operation")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")

    while True:
        choice = input("enter your choice (1/2/3/4): ")

        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(num1, "+", num2, "=", add(num1, num2))
            elif choice == '2':
                print(num1, "-", num2, "=", subtract(num1, num2))
            elif choice == '3':
                print(num1, "*", num2, "=", multiplication(num1, num2))
            elif choice == '4':
                result = divide(num1, num2)

                if result == "Error!division by zero":
                    print(result)
                else:
                    print(num1, "/", num2, "=", result)

        else:
            print("invalid number")

        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break

if __name__ == "__main__":
    main()