"""
# Створити dataset та працювати з ним

# Які продукти купляли усі покупці?

# Як змінювалась ціна на яблука? (графік)

# Скільки грошей витрачає кожний покупець на покупки? (графік)

# Який найпопулярніший товар?

# Якого товару було куплено найменше?

# Який найдорожчий товар?

# Якого товару, скільки покупців купляє? (графік)

# Написати функціонал для додавання нових даних
"""
#import plotly
#import plotly.graph_objs as go
def appending(c,itera):
    list1=[]
    list1.append(float(c[itera][3]))
    list1.append(float(c[itera][4][:5]))
    return list1
def new_data():
    new=[]
    for i in range(4):
        new.append()
    return new
def dicty(c,itera,dict1=dict()):
    if itera == len(c):
        return dict1
    else:
        dict2=dict()

        if c[itera][0] in dict1:
            if c[itera][1] in dict1[c[itera][0]]:
                if c[itera][2] in dict1[c[itera][0]][c[itera][1]]:
                            print(dict1[c[itera][0]][c[itera][1]])
                            dict1[c[itera][0]][c[itera][1]][c[itera][2]]=appending(c,itera)
                
            dict1[c[itera][0]][c[itera][1]]={c[itera][2]:appending(c,itera)}
            
        else:
            dict2[c[itera][1]]={c[itera][2]:[float(c[itera][3]),float(c[itera][4][:5])]}
            dict1[c[itera][0]]=dict2

    return  dicty(c,itera+1,dict1)
def product(c,itera,dict1):
    list1=[]
    list1.append(dict1[c[itera][0]][c[itera][1]])
    return list1
def apples(dict1,c):
    result=[]
    list1=[]
    for i in range(2,7):
        if 'apple' in list(dict1[c[i][0]][c[i][1]].keys())[0]:
            list1=dict1[c[i][0]][c[i][1]][c[i][2]]
            result.append(list1[0]*list1[1])
    
    #diagram= go.Scatter(x=result,y=dict1[c[i][0]][c[i][1]].keys())
    #fig = go.Figure(data=[diagram])
    #plotly.offline.plot(fig, filename='apples.html')

def the_biggest_price(dict1,c):
    result=[]
    list1=[]
    for i in range(2,7):
        list1=dict1[c[i][0]][c[i][1]][c[i][2]]
        result.append(list1[1])
    return max(result)

def popular_product(dict1,c):
    list1=[]
    list2=[]
    for i in range(2,7):
        list1.append(list(dict1[c[i][0]][c[i][1]].keys()))
    for i in range(len(list1)):
        list2.append(list1.count([list1[i][0]]))
    answer=list1[list2.index(max(list2))]
    return answer
def min_product(dict1,c):

    return 

def how_what(dict1,c):
    list1=set()
    result=[0,0,0]
    for i in range(2,7):
        list1.add(str(dict1[c[i][0]][c[i][1]].keys())[9:])
    list2=list(list1)
    for i in range(2,7):
        print(dict1[c[i][0]][c[i][1]].keys())
        if list2[0] in str(dict1[c[i][0]][c[i][1]].keys()):
            result[0]=result[0]+1
        elif list2[1] in str(dict1[c[i][0]][c[i][1]].keys()):
            result[1]=result[1]+1
        elif list2[2] in str(dict1[c[i][0]][c[i][1]].keys()):
            result[2]=result[2]+1

    #diagram= go.Scatter(x=result,y=list1)
    #fig = go.Figure(data=[diagram])
    #plotly.offline.plot(fig, filename='how_who.html')
        
f=open("orders.csv",encoding ='utf', newline= "")
spys=f.readlines()
g=[]
for i in range (len(spys)):
    g.append(spys[i].split(','))

empty_dict=[]
list1=[]
g.append(new_data())
empty_dict=dicty(g,1)
list1=(product(g,1,empty_dict))
apples(empty_dict,g)
popular_product(empty_dict,g)
the_biggest_price(empty_dict,g)
min_product(empty_dict,g)
how_what(empty_dict,g)


