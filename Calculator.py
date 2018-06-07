def help_screen():
    print("Add : Adds two numbers")
    print("Subtract : Subtract two numbers")
    print("Print : Display the result of the latest operation")
    print("Help : Display this help screen")
    print("Quit : Exits the program")

def menu():
    return input("----- A) Add S) Subtract P) Print H) Help Q) Quit -----")

def main():
    result = 0.0
    done = False;
    while not done:
        choice = menu()
        if choice == "A" or choice == "a":
            n1 = float(input (" Enter the First Number : "))
            n2 = float(input (" Enter the Second Number : "))
            result = n1 + n2
            print("Addtion =", result)
        elif choice == "S" or choice == "s":
            n1 = float(input (" Enter the First Number : "))
            n2 = float(input (" Enter the Second Number : "))
            result = n1 - n2
            print("Subtraction ",result)
        elif choice == "P" or choice == "p":
            print(result)
        elif choice == "H" or choice == "h":
            help_screen()
        elif choice == "Q" or choice == "q":
            done = True
main()
