import csv
data = open("students.csv", "r")
users = list(csv.DictReader(data, delimiter=',', quotechar='"'))
def my_sort(mas):
    for i in range(len(mas)):
        j = i-1
        key = mas[i]
        while j >= 0 and float(mas[j]['score'] if mas[j]['score'] != 'None' 
                    else 0) < float(key['score'] if key['score'] != 'None' else 0):
            mas[j+1] = mas[j]
            j-=1
        mas[j+1] = key
    return mas
sortData = my_sort(users)
count = 1
print('10 класс:')
for element in sortData:
    if "10" in element["class"]:
        if count > 3: exit()
        name = element["Name"].split()
        print(f"{count} место: {name[1][0]}. {name[0]}")
        count += 1