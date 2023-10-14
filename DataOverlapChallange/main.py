with open("file1.txt", "r") as data:
    file1 = data.read().splitlines()

with open("file2.txt", "r") as data:
    file2 = data.read().splitlines()


result = [int(num) for num in file1 if num in file2]


print(result)
