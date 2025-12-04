import functionalities as func

print("Unit Conversion Tool")

while True:
    print("Select Conversion Type: \n1. Length Conversion \n2. Area Conversion \n3. Weight Conversion \n0. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        func.length_conversion()
    elif choice == "2":
        func.area_conversion()
    elif choice == "3":
        func.weight_conversion()
    elif choice == "0":
        print("Exiting the program.\nGoodbye!")
        break
    else:
        print("Invalid choice. Please try again.\n")

