import csv
data = open("students.csv", "r")
users = list(csv.DictReader(data, delimiter=",", quotechar='"'))
userInput = ""
def findItemById(mas, id):
    for element in mas:
        if element["titleProject_id"] == id:
            return element
    return None
while True:
    userInput = input("Ввод: ")
    if userInput == "СТОП": exit()
    find = findItemById(users, userInput)
    if not find is None:
        id_proj = find["titleProject_id"]
        score = find["score"]
        name = find["Name"].split(" ")
        print(f"Вывод: Проект № {id_proj} делал: {name[1][0]}. {name[0]} он(а) "
              + f"получил(а) оценку - {score}.")
    else:
        print("Ничего не найдено")