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
import plotly
import plotly.graph_objs as go
from functools import reduce
# Написати функціонал для додавання нових даних
def new_data(dct,lst):
    return dicty(dct,lst)
def dicty(dct,lst):
    if len(lst) == 3:
        dct[lst[0]] = [float(lst[1]),float(lst[2])]
        return dct
    key = lst[0]
    if key not in dct:
        dct[key] = {}
    dicty(dct[key], lst[1:])
    return dct
#Які продукти купляли усі покупці?
def product(dct):
    products=set()
    for name in dct.keys():
        for date in dct[name]:
             for product in dct[name][date]:
                products= products.union(set(dct[name][date].keys()))

    return products
# Як змінювалась ціна на яблука? (графік)
def apples(dct):
    apples = {}
    for _, dates in dct.items():
        for date, products in dates.items():
            for prod, prices in products.items():
                if prod == 'apple':
                    apples[date] = prices[1]
    
    diagram= go.Scatter(x=sorted(list(apples.keys())), y = [apples[key] for key in sorted(list(apples.keys())) ])
    fig = go.Figure(data=[diagram])
    plotly.offline.plot(fig, filename='apples.html')
# Який найдорожчий товар?
def the_biggest_price(dct):
    lst1=[]
    lst2=[]
    for name in dct:
        for date in dct[name]:
            for product in dct[name][date]:
                lst1.append(dct[name][date][product][1])
                lst2.append(product)
            
    return lst2[lst1.index(max(lst1))]
# Якого товару було куплено найменше?
def min_product(result):
    lst1=[]
    lst2=[]
    for name in result:
        for date in result[name]:
            for product in result[name][date]:
                lst1.append(result[name][date][product][0])
                lst2.append(product)
            
    return lst2[lst1.index(min(lst1))]

# Який найпопулярніший товар?
def popular_product(dct):
    lst1=[]
    products=[]
    list_product=[]
    for name in dct:
        for date in dct[name]:
            for product in dct[name][date]:
                products.append(list(dct[name][date][product]))
    
    products_set=set()
    for name in dct.keys():
        for date in dct[name]:
             for product in dct[name][date]:
                products_set= products_set.union(set(dct[name][date].keys()))
    products_set=list(products_set)
    for elem in products_set:
        lst1.append(products.count(elem))
    
    return products_set[lst1.index(max(lst1))]

# Якого товару, скільки покупців купляє? (графік)

def how_what(dct):
    person = dict()
    for name in dct:
        for date in dct[name]:
            for product in dct[name][date]:
                if product not in person:
                    person[product] = 0
                person[product] += 1

    diagram= go.Scatter(x=list(person.keys()),y=list(person.values()))
    fig = go.Figure(data=[diagram])
    plotly.offline.plot(fig, filename='who_what.html')

# Скільки грошей витрачає кожний покупець на покупки? (графік)
def spending(dct):
    spending = {}
    for name in dct:
        spending[name] = 0
        for date in dct[name]:
            for product in dct[name][date]:
                lst=dct[name][date][product]
                spending[name] += float(dct[name][date][product][0])*float(lst[1])

    diagram= go.Scatter(x=list(spending.keys()),y=list(spending.values()))
    fig = go.Figure(data=[diagram])
    plotly.offline.plot(fig, filename='spending.html')


with open('orders.csv', encoding='utf-8') as f:
    f.readline()
    file = [[el.strip() for el in line.split(',')] for line in f]






our_dict= reduce(dicty,file, {})

#new=[input() for i in range(5)]
#our_dict=new_data(our_dict,new)
print(our_dict)

print(product(our_dict))

apples(our_dict)

print(popular_product(our_dict))

print(the_biggest_price(our_dict))

print(min_product(our_dict))

how_what(our_dict)

spending(our_dict)

