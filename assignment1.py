

choice = int(input("Choose Conversion:\n1. Fahrenheit to Celsius\n2. Celsius to Fahrenheit\nEnter your choice: "))


if choice == 1:
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    convert = (fahrenheit - 32) / 1.8
    print(f"Temperature in Celsius: {convert:.2f}")  

elif choice == 2:
    celsius = float(input("Enter temperature in Celsius: "))
    convert = (celsius * 1.8) + 32
    print(f"Temperature in Fahrenheit: {convert:.2f}") 

else:
    print("Invalid choice. Please enter 1 or 2.")