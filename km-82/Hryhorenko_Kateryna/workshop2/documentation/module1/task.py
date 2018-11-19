"""
дано структуру даних знайти
"""
smth=[
    {
        "name":"Bob",
        "age":20,
        "marks":{
            "math":98,
            "python":100
        }
    },
    {
        "name":"Boba",
        "age":19,
        "marks":{
            "phisic":98
        }
    },
    {
        "name":"Boban",
        "age":22,
        "marks":{

        }
    }
]



#vik naistarshogo studenta
def age_max(smth,d,i):
    if len(d) >= 3:
        return d
    d.append(smth[i]["age"])
    return age_max(smth,d,i+1)

#dodaty ozinku s predmeta
def add_mark(smth,name,disc,mark):
    for student in smth:
        if student["name"] == name:
            student["marks"][disc] = mark
    return smth
#vvesty imena studentiv
def name_student(smth):
    for i in range (3):
        print(smth[i]["name"])


d=[]
print(max(age_max(smth,d,0)))
print(add_mark(smth,'Boban','Math',80))
name_student(smth)

