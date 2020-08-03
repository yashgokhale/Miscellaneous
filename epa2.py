from tkinter import *
from tkhtmlview import HTMLLabel
import requests
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from collections import OrderedDict

%matplotlib qt
key='khakiwolf72'
email='yashgokhale19972@gmail.com'

def get_states(email,key):
    rr=requests.get(f'https://aqs.epa.gov/data/api/list/states?email={email}&key={key}')
    d=rr.json()['Data']
    states={}
    for i,s in enumerate(d):
        states.update({s['value_represented']:s['code']})   
    return states

def get_counties(email,key,states,s):
    c=requests.get(f'https://aqs.epa.gov/data/api/list/countiesByState?email={email}&key={key}&state={states[s]}')
    cc=c.json()['Data']
    counties={}
    for i,x in enumerate(cc):
        counties.update({x['value_represented']:x['code']})
    return counties

crit=requests.get(f'https://aqs.epa.gov/data/api/list/classes?email={email}&key={key}')
cr=crit.json()['Data']
pars={}
for x in cr:
    pars.update({x['value_represented']:x['code']})  
cr2=pars['Pollutants that have an AQI Defined']

pp=requests.get(f'https://aqs.epa.gov/data/api/list/parametersByClass?email={email}&key={key}&pc={cr2}')
pp2=pp.json()['Data']
param_codes={}
for x in pp2:
    param_codes.update({x['value_represented']:x['code']}) 
    
def countydata(email, key, param, bdate, edate, state, county):
    r=requests.get(f'https://aqs.epa.gov/data/api/sampleData/byCounty?email={email}&key={key}&param={param}&bdate={bdate}&edate={edate}&state={state}&county={county}')
    d=r.json()['Data']
    dat=[]
    tim=[]
    mes=[]
    sit=[]
    for i,x in enumerate(d):
        a,b=x['time_local'].split(':')
        tim.append(float(a)+float(b)/60)
        m=(x['sample_measurement'])
        if m:
            mes.append(float(x['sample_measurement']))
        else:
            mes.append(0)
        dat.append(x['date_local'])
        sit.append(x['site_number'])
    df={'Site':sit,'Date':dat,'Time':tim,'Value':mes}
    return pd.DataFrame(df)

def press():
    st=sta.get()
    co=cou.get()
    bdate=star.get()
    edate=str(int(bdate)+1)
    poll=polu.get()
    states=get_states(email,key)
    cp=get_counties(email,key,states,st)
    sc=states[st]
    cc=cp[co]
    par=param_codes[poll]
    dt=countydata(email,key,par,bdate,edate,sc,cc)
    un_sit=dt['Site'].unique()
    for m in un_sit:
        day=dt['Date'].unique()[0]
        dt.groupby('Site').get_group(m).groupby('Time').mean().plot(style='.-')
    #    print(data)
    #    plt.plot(data['Time']/60,data['Value'])
        plt.xlabel('Time(hr)')
        plt.ylabel('Measurement')
        plt.title(f'{poll} for site {m} for {bdate} in {co} county, {st}')
        plt.show()


root=Tk()
root.title('US EPA Pollution Trends')  
mainframe = Frame(root)
mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
Label(root, text="Pollutant visualization",font=('bold')).grid(row = 0, column = 0)
Label(root, text="Enter the state").grid(row = 1, column = 0)
Label(root, text="Enter the county").grid(row = 3, column = 0)
Label(root, text="Enter the date(yyyymmdd)").grid(row = 5, column = 0)
Label(root, text="Choose the pollutant").grid(row = 7, column = 0)
sta=Entry(root)
cou=Entry(root)
star=Entry(root)
polu=Entry(root)
sta.grid(row=2,column=0)
cou.grid(row=4,column=0)
star.grid(row=6,column=0)
polu.grid(row=8,column=0)
choices=OrderedDict([(cc,i) for i,cc in enumerate(list(param_codes.keys()))])
k=sorted(choices.keys())
#tkvar = StringVar(root)
#tkvar.set(k[0])
#popupMenu = OptionMenu(mainframe, tkvar, *k)
#popupMenu.grid(row=10,column=0)
b=Button(root,text='Plot',command=press).grid(row=12,column=0)
Rules='Options of pollutants \n'
for x in k:
    Rules=Rules+str(x)+'\n'
w = Label(root, text=Rules,font=("Times New Roman", 10)).grid(row =13, column = 0)
root.mainloop()
