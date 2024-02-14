data = open("students.csv", "r")
users = [list(map(str, e.split(","))) for e in data]
usersHelp = [u for u in users]
allScore = 0
#Хадаров Владимир
for id,Name,titleProject_id,class_,score in users[1:]:
    if score[:-1] == "None": continue
    else: allScore += int(score[:-1])
    if Name.split(" ")[0] == "Хадаров":
        print(f"Ты получил: {score[:-1]}, за проект - {titleProject_id}")
srZnach = round(allScore/(len(users)-1), 3)
dataNew = open("student_new.csv", "w")
for id,Name,titleProject_id,class_,score in usersHelp:
    if score[:-1] == "None": score = str(srZnach)+"\n"
    dataNew.write(f"{id},{Name},{titleProject_id},{class_},{score}")