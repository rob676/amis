'''
завдання вивести гафік вильоту і прильоту для кожного термінала
х-кількість пасажирів
у-дата
'''
import plotly
import plotly.graph_objs as go
def add_dct(dct,lst):
    if len(lst) == 2:
        dct[lst[0]] = int(str(lst[1]).strip())
        return dct
    key = lst[0]
    if key not in dct:
            dct[key] = {}
    add_dct(dct[key],lst[1:])
    return dct

def convert_str(s):
    return list(map(str.strip, s.split(',')))

from functools import reduce
#writting file for working
with open('los-angeles-international-airport-passenger-traffic-by-terminal.csv', encoding='utf-8') as f:
    spys=f.readlines()
    g=[]
    for i in range (len(spys)):
        g.append(spys[i].split(','))
    print(g[5640:])
    #result = reduce(add_dct,g[1000:], {})
    #result2 = reduce(add_dct,g[1000:2000], {})
    #result3 = reduce(add_dct,g[2000:3000], {})
    #result4 = reduce(add_dct,g[3000:4000], {})
    #result5 = reduce(add_dct,g[4000:5000], {})
    #result6 = reduce(add_dct,g[5000:5600], {})
    dct = reduce(add_dct,g[5600:5643], {})


    

terminals=[]
lst_depurture=dict()
lst_arrival=dict()
#find terminals in dictionary
for data in dct.keys():
    for report in dct[data].keys():
        for terminal in dct[data][report].keys():
            terminals.append(terminal)
        #writting all terminals
        for terminal in set(terminals):
            sum_arrival=0
            sum_depurture=0
            if terminal not in lst_arrival:
                lst_arrival[terminal]=[]
            #sum of passengers
            if  'Arrival'  in dct[data][report][terminal] :
                if 'Domestic' in dct[data][report][terminal]['Arrival']:
                    sum_arrival += dct[data][report][terminal]['Arrival']['Domestic']
                if 'International' in dct[data][report][terminal]['Arrival']:
                    sum_arrival += dct[data][report][terminal]['Arrival']['International']
                lst_arrival[terminal].append(sum_arrival)


            if terminal not in lst_depurture:
                lst_depurture[terminal]=[]

            if  'Departure'  in dct[data][report][terminal] :
                if 'Domestic' in dct[data][report][terminal]['Departure']:
                    sum_depurture += dct[data][report][terminal]['Departure']['Domestic']
                if 'International' in dct[data][report][terminal]['Departure']:
                    sum_depurture += dct[data][report][terminal]['Departure']['International']
            lst_depurture[terminal].append(sum_depurture)
# make scatter     
files=['1.html','2.html','3.html','4.html','5.html','6.html','7.html','8.html','9.html','10.html']
def scatter(terminal):
    diagram=go.Scatter(x=list(dct.keys()),y=lst_depurture[terminal])
    diagram2=go.Scatter(x=list(dct.keys()),y=lst_arrival[terminal])
    return go.Figure(data=[diagram,diagram2])
terminals=list(set(terminals))
def draw(terminals,files):
    if len(files) == 0:
        return
    plotly.offline.plot(scatter(terminals[0]), filename=files[0])
    return draw(terminals[1:],files[1:])




        
draw(terminals,files)
