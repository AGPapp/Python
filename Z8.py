#Необходимо считать любой текстовый файл на вашем ПК (можно создать новый) и создать на его основе
# новый файл, где содержимое будет записано в обратном порядке.
# В конце программы вывести на экран оба файла - старый в неизменном виде и новый в обратном порядке.


a = []
with open('test.txt', 'r', encoding='utf-8') as file:
    for text in file:
        revers = text[::-1]
        a.insert(0, revers)

with open('tset.txt', 'w', encoding='utf-8') as file2:
    file2.writelines(a)

with open('test.txt', 'r', encoding='utf-8') as file:
    print(file.read())

with open('tset.txt', 'r', encoding='utf-8') as file2:
    print(file2.read())