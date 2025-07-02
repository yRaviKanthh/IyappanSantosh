def count_multiples(input_list):
    result = {}
    for i in range(1, 10):
        count = sum(1 for num in input_list if num % i == 0)
        result[i] = count
    return result
numbers = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
output = count_multiples(numbers)
print("Output:")
print(output)
