def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9


while True:
    print("\n--- Temperature Converter ---")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        temp = float(input("Enter temperature in Celsius: "))
        result = celsius_to_fahrenheit(temp)
        print(f"{temp}°C = {result:.2f}°F")

    elif choice == "2":
        temp = float(input("Enter temperature in Fahrenheit: "))
        result = fahrenheit_to_celsius(temp)
        print(f"{temp}°F = {result:.2f}°C")

    elif choice == "3":
        print("Exiting Temperature Converter...")
        break

    else:
        print("Invalid choice! Please try again.")
