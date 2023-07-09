#CALCULATION OF DECIMAL AND EXPONENTIAL 
while True:
    print("1. DECIMAL CALCULATOR")
    print("2. EXPONENTIAL CALCULATOR")
    print("0. EXIT")
    choice = input("Enter your Choice \n")
    if choice == "1":
        operation = "DECIMAL"
        while operation == "DECIMAL":
            decimal_num = float(input("Input your decimal number below \n"))
            decimal_place = int(input("To how many decimal place? \n"))
            result = str(round(decimal_num, decimal_place))
            print(result + " is the answer")
            switch_choice = input("Enter 2 to switch to MENU or 1 to continue \n")
            if switch_choice =="2":
                operation = "EXPONENTIAL"
                
    elif choice =="2":
        operation = "EXPONENTIAL"
        while operation =="EXPONENTIAL":
            base_num = int(input("Enter your base number \n"))
            exponent = int(input("Enter your power \n"))
            result = str(pow(base_num, exponent))
            print(result + " is your answer")
            switch_choice = input("Enter '1' to switch to MENU or 2 to continue ")
            if switch_choice == "1":
                operation = "DECIMAL"
                
    elif choice == "0":
        break
    else:
        print("Invalid choice. Please try again.")

print("Program ended.")
    
        

        