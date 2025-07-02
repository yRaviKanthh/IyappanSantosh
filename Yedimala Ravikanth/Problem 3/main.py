try:
    a = int(input("Enter a number (a): "))

    if a <= 0:
        print("Please enter a positive integer.")
    else:
        count = a if a % 2 != 0 else a - 1
        result = [2 * i + 1 for i in range(count)]
        print("Output:", ", ".join(map(str, result)))

except ValueError:
    print("Invalid input. Please enter an integer.")
