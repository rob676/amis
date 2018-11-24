smth=[
    {'bob@kpi.ua':{
                    'person':{
                    "name": "Bob",
                    "email":"bob@kpi.ua"},
                    "foods":{
                        "apple":[1.3,12.1],
                        "milk":[45]}}},
        
         {'boba@kpi.ua':{
                    'person':{
                    "name": "Boba",
                    "email":"boba@kpi.ua"
                    },
                    "foods":{
                        "milk":[45]}}}
    ]
        




def product(smth,spysokEmail,c=0):
    if len(spysokEmail) == 0:
        return
    print(smth[0][spysokEmail[0]]['person']['name'])#виводить ім'я людини
    listt=smth[0][spysokEmail[0]]['foods'].copy()
    rax=0
    print('vkluchenya product')
    for i in listt:
        kilk=0
        for j in range(len(listt[i])):
            kilk+=1
            c+=listt[i][j]
            d=list(listt.keys())
        print(d[rax],kilk)
        rax+=1
    print('skilki vytratyv',c)
    return product(smth[1:],spysokEmail[1:])

spysokEmail=[]
for i in range(len(smth)):
    spysokEmail=spysokEmail + list(smth[i].keys())



product(smth,spysokEmail)

    

