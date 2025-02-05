

choice = int(input("Choose Conversion:\n1. Pounds to Kilograms\n2. Kilograms to Pounds\nEnter your choice: "))


if choice == 1:
    pounds = float(input("Enter Pounds: "))
    convert = pounds * 0.453592
    print(f"{pounds} lbs in Kilograms: {convert:.2f} kg")  

elif choice == 2:
    kilograms = float(input("Enter Kilograms: "))
    convert = kilograms * 2.20462
    print(f"{kilograms} kg in Kilograms: {convert:.2f} lbs")  

else:
    print("Invalid choice. Please enter 1 or 2.")