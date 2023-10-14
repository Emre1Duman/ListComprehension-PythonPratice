list_of_strings = input().split(',')


list_of_numbers = [int(string) for string in list_of_strings]


result = [num for num in list_of_numbers if num % 2 == 0]


print(result)