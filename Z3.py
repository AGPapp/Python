numbers = [0, 99, 100, 53, 44, 23, 4, 8, 16, 15, 77, 51]
def serch(num):
    if num > 50 and num % 2 != 0:
        return 1
    else:
        return 0

print(list(filter(serch, numbers)))