from sys import exit

numstring = input("> ")
for i in numstring:
    if i not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        print("is not a num")
        exit(0)
print("is a num")
