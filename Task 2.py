print("Select a Pattern:")
print("1. Number Pyramid")
print("2. Inverted Number Pyramid")
print("3. Centered Pyramid")
print("4. Floyd’s Triangle")
print("5. Number Diamond")

choice = int(input("Enter your choice (1–5): "))
rows = int(input("Enter number of rows: "))

print("\nGenerated Pattern:\n")

if choice == 1:
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

elif choice == 2:
    for i in range(rows, 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

elif choice == 3:
    for i in range(1, rows + 1):
        for s in range(rows - i):
            print(" ", end=" ")
        for n in range(1, i + 1):
            print(n, end=" ")
        print()

elif choice == 4:
    num = 1
    for i in range(1, rows + 1):
        for j in range(i):
            print(num, end=" ")
            num += 1
        print()

elif choice == 5:
    for i in range(1, rows + 1):
        for s in range(rows - i):
            print(" ", end=" ")
        for n in range(1, i + 1):
            print(n, end=" ")
        print()
    for i in range(rows - 1, 0, -1):
        for s in range(rows - i):
            print(" ", end=" ")
        for n in range(1, i + 1):
            print(n, end=" ")
        print()

else:
    print("Invalid choice!")

print("\n✔ Pattern generated successfully!")
