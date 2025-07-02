
try:
    a = int(input("Enter a number (a): "))

    if a <= 0:
        print("Please enter a positive integer.")
    else:
        result = []
        for i in range(a):
            result.append(2 * i + 1)

        print("Output:", ", ".join(map(str, result)))

except ValueError:
    print("Invalid input. Please enter an integer.")
