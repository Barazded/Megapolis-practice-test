import csv
file = open("students.csv", "r")
def gen_hash(st: str):
    alpha = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ "
    slov = {i: letter for letter,i in enumerate(alpha, 1)}
    p = 67
    m = 10**9 + 9
    hashVal = 0
    step = 1
    for e in st:
        hashVal = (hashVal + slov[e]*step) % m
        step = (step*p)%m
    return int(hashVal)
fileNew = open("students_with_hash.csv", "w")
fileNew.write("id,Name,titleProject_id,class,score\n")
students = csv.DictReader(file, delimiter=",", quotechar='"')
for student in students:
    id = gen_hash(student["Name"])
    name = student["Name"]
    pj_id = student["titleProject_id"]
    class_ = student["class"]
    score = student["score"]
    fileNew.write(f"{id},{name},{pj_id},{class_},{score}\n")