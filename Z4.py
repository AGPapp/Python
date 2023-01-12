dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4, 'five': 5}
newDict = {}

for k, v in dict.items():
    if v >= 3:
        newDict[k] = v

print(newDict)
