import random
import csv
import string
file = open("students.csv", "r")
users = list(csv.DictReader(file, delimiter=",", quotechar='"'))
alph = string.ascii_lowercase + string.ascii_uppercase + string.digits
def gen_password():
    password = ""
    for i in range(8):
        rand = random.choice(alph)
        password += rand
    return password
def gen_login(name):
    login = f"{name[0]}_{name[1][0]}{name[2][0]}"
    return login
newFile = open("students_password.csv", "w")
newFile.write("id,Name,titleProject_id,class,score,login,password\n")
for user in users[1:]:
    password = gen_password()
    login = gen_login(user["Name"].split(" "))
    id = user["id"]
    name = user["Name"]
    title = user["titleProject_id"]
    class_ = user["class"]
    score = user["score"]
    newFile.write(f"{id},{name},{title},{class_}{score}, {login},{password}\n")