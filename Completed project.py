#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import PySimpleGUI as sg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg#

suiciderate=pd.read_csv("/Users/senth/Downloads/Suicide Rate.csv")
lifeex=pd.read_csv("/Users/senth/Downloads/Life expectancy.csv")
sui=pd.DataFrame(suiciderate)
life=pd.DataFrame(lifeex)
print(sui.head())
print(sui.info())
sui["GDP per capita"] = sui["GDP per capita"].str.replace(',','')
sui["GDP per capita"]= sui["GDP per capita"].astype(int)
#sui["Suicide rate"]= sui["Suicide rate"].astype(float)
print(sui)
print(sui.info())

sui['Suicide rate'] = sui['Suicide rate'].apply(np.float64)
sui['GDP per capita'] = sui['GDP per capita'].apply(np.int64)
sui.info()
print("Any missing data:",sui.isnull().values.any()) 
print("Number of missing data:",sui.isnull().values.sum())
g=sui.duplicated()
print("Number of duplicates:",g.sum())


# In[2]:


life.info()
print("Any missing data ",life.isnull().values.any()) 
print("Number of missing data:",life.isnull().values.sum())
h=life.duplicated()
print("Number of duplicates:",h.sum())


# In[3]:


newdf = sui.merge(life, how='outer')

newdf.info()
print("Any missing data for life expectancy:",newdf.isnull().values.any()) 
print("Number of missing data:",newdf.isnull().values.sum())
i=newdf.duplicated()
print("Number of duplicates:",i.sum())
newdf2=newdf.dropna()
print("Number of missing data after cleaning:",newdf2.isnull().values.sum())
newdf3 = newdf[~newdf.index.isin(newdf2.index)]
newdf3.info()


# In[4]:


newdf2.head()


# In[5]:


import matplotlib.pyplot as plt
col=['GDP per capita', 'Suicide rate','Life Expectancy (years) - Men','Life Expectancy (years) - Women', 'Happiness Score','Fertility Rate (births per woman)']
fig = plt.figure(figsize=(10,10))

for i in range(len(col)):
    plt.subplot(2,3,i+1)
    plt.title(col[i])
    sns.boxplot(data=newdf2,y=newdf2[col[i]])

plt.tight_layout()
plt.show()


# In[6]:


fig = plt.figure(figsize=(10,10))

for i in range(len(col)):
    plt.subplot(2,3,i+1)
    plt.title(col[i])
    sns.histplot(data=newdf2,x=newdf2[col[i]])

plt.tight_layout()
plt.show()


# In[7]:


sns.heatmap(newdf2.corr(),annot=True, cbar=False, cmap='Blues', fmt='.1f');


# In[8]:


sns.pairplot(newdf2);


# In[9]:


import seaborn as sns

headings = sui.columns.tolist()
data = sui.values.tolist()
headings2 = life.columns.tolist()
data2 = life.values.tolist()

headings7 = newdf2.columns.tolist()
data7 = newdf2.values.tolist()

headings8 = newdf3.columns.tolist()
data8 = newdf3.values.tolist()

headings3 = newdf.columns.tolist()
data3 = newdf.values.tolist()#



cor=sui.corr()
corr=pd.DataFrame(cor)
adress=["GDP per capita","Suicide rate"]
corr[""]=adress
corrr=corr.iloc[:,[2,0,1]]
headings4 = corrr.columns.tolist()
data4 = corrr.values.tolist()#

cor1=life.corr()
corr1=pd.DataFrame(cor1)
adress1=["Life Expectancy (years) - Men","Life Expectancy (years) - Women","Happiness Score","Fertility Rate (births per woman)"]
corr1[""]=adress1
corrr1=corr1.iloc[:,[4,0,1,2,3]]
headings5 = corrr1.columns.tolist()
data5 = corrr1.values.tolist()#

cor2=newdf2.corr()
corr2=pd.DataFrame(cor2)
adress2=["GDP per capita","Suicide rate","Life Expectancy (years) - Men","Life Expectancy (years) - Women","Happiness Score","Fertility Rate (births per woman)"]
corr2[""]=adress2
corrr2=corr2.iloc[:,[6,0,1,2,3,4,5]]
headings6 = corrr2.columns.tolist()
data6 = corrr2.values.tolist()#



# In[10]:


cor


# In[11]:


cor1


# In[12]:


cor2


# In[13]:


#interface code

import PySimpleGUI as sg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def bargraph():
    def create_bargraph():
        fig = plt.figure(figsize=(10,10))

        for i in range(len(col)):
            plt.subplot(2,3,i+1)
            plt.title(col[i])
            sns.histplot(data=newdf2,x=newdf2[col[i]])
             
        return plt.gcf()
    def draw2(canvas, figure):
        figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
                    
        figure_canvas_agg.draw()
        
        figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=True)
        return figure_canvas_agg
    
    layout7= [[sg.Text("Bar Graph", key="new",size=(100,1))],[sg.Canvas(key='-CANVAS2-',size=(1000, 1000))]]
    window = sg.Window("", layout7, modal=True,size=(700,500),finalize=True,element_justification='center',resizable=True)
    draw2(window['-CANVAS2-'].TKCanvas, create_bargraph())
    
    choice = None
  
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
    window.close()

def scattergraph(x,y):
    def create_scatter(x, y):
        plt.scatter(x, y, color='red', marker='o')
        plt.title(a, fontsize=14)
        plt.xlabel(b, fontsize=14)
        plt.ylabel(c, fontsize=14)
        plt.grid(True)     
        return plt.gcf()
    def draw(canvas, figure):
        figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)                    
        figure_canvas_agg.draw()        
        figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=True)
        return figure_canvas_agg    
    layout5= [[sg.Text("Graph", key="new",size=(100,1))],[sg.Canvas(key='-CANVAS-',size=(100, 100))]]
    window = sg.Window("", layout5, modal=True,size=(500,400),finalize=True,element_justification='center',resizable=True)
    draw(window['-CANVAS-'].TKCanvas, create_scatter(x, y))    
    choice = None  
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
    window.close()

def pairplot():
    def create_pairplot():
        sns.pairplot(newdf2);
             
        return plt.gcf()
    def draw1(canvas, figure):
        figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
                    
        figure_canvas_agg.draw()
        
        figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=True)
        return figure_canvas_agg
    
    layout6= [[sg.Text("Graph", key="new",size=(100,1))],[sg.Canvas(key='-CANVAS1-',size=(1000, 1000))]]
    window = sg.Window("", layout6, modal=True,size=(700,500),finalize=True,element_justification='center',resizable=True)
    draw1(window['-CANVAS1-'].TKCanvas, create_pairplot())
    
    choice = None
  
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
    window.close()



    
table= sg.Table(data, headings=headings,justification='left', key='-table-',size=(200,200))
table2=sg.Table(data2, headings=headings2,justification='left', key='-table2-',size=(200,300))
table3=sg.Table(data3, headings=headings3,justification='left', key='-table3-',size=(200,100))
table4=sg.Table(data4,headings=headings4,justification='left', key='-table4-',size=(5,5))
table5=sg.Table(data5,headings=headings5,justification='right', key='-table5-',size=(100,100))
table6=sg.Table(data6,headings=headings6,justification='right', key='-table6-',size=(100,100))
table7=sg.Table(data7,headings=headings7,justification='right', key='-table7-',size=(100,100))
table8=sg.Table(data8,headings=headings8,justification='right', key='-table8-',size=(100,100))


sg.theme('DarkTeal2')  #sg.theme_list(),sg.theme_previewer()
layout1=[[sg.Text('Suicide Rate and Life Expectancy Data',size=(700,1),justification='c')],
         [sg.Button("Suicide Rate Data"),sg.Button("Life Expectancy Data"),sg.Button("Combined Raw Data"),sg.Button("Cleaned Data"),sg.Button("Removed Data")],
         [sg.Column([[table]], scrollable=False,visible=False, key='-COL-'),sg.Column([[table2]], scrollable=True,visible=False, key='-COL2-'),
          sg.Column([[table3]], scrollable=True,visible=False, key='-COL3-'),sg.Column([[table7]], scrollable=True,visible=False, key='-COL7-'),
          sg.Column([[table8]], scrollable=True,visible=False, key='-COL8-')]]

layout2=[[sg.Text('Suicide Rate Analysis',size=(700,1),justification='c')],
         [sg.Button("Correlation Table1"),sg.Button("GDP per capita vs Suicide rate")],[sg.Column([[table4]], scrollable=False,visible=False, key='-COL4-')]]

layout3=[[sg.Text('Life Expectancy Rate Analysis',size=(700,1),justification='c')],
         [sg.Button("Correlation Table2"),sg.Button("Life Expectancy of Men vs Women"),
          sg.Button("Life Expectancy of Women vs Happiness Score")],
         [sg.Button("Life Expectancy of Men vs Happiness Score"),
          sg.Button("Happiness Score vs Fertility Rate")],
         [sg.Column([[table5]], scrollable=True,visible=False, key='-COL5-')]]
        
layout4=[[sg.Text('Suicide and Life Expectancy Rate Analysis',size=(700,1),justification='c')],
         [sg.Button("Correlation Table3"),sg.Button("pair plot"),sg.Button("Bar Graph")],
         [sg.Column([[table6]], scrollable=True,visible=False, key='-COL6-')]]
        

tabgrp = [[sg.TabGroup([[sg.Tab('Given Data', layout1),
                         sg.Tab('Sucide Rate', layout2),
                         sg.Tab('Life Expectancy', layout3),
                         sg.Tab('Combined Analysis', layout4)]])]]
window=sg.Window("Python Project",tabgrp, size=(700,500),resizable=True)
#event,values= window.read()
while True:
    x=0
    y=0
    event,values= window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
            break
    if event=="Suicide Rate Data":
        window['-COL2-'].Update(visible=False)
        window['-COL-'].Update(visible=True)
        window['-COL3-'].Update(visible=False)
        window['-COL7-'].Update(visible=False)
        window['-COL8-'].Update(visible=False)
    elif event=="Life Expectancy Data":
        window['-COL-'].Update(visible=False)
        window['-COL2-'].Update(visible=True)
        window['-COL3-'].Update(visible=False)
        window['-COL7-'].Update(visible=False)
        window['-COL8-'].Update(visible=False)
    elif event=="Combined Raw Data":
        window['-COL-'].Update(visible=False)
        window['-COL2-'].Update(visible=False)
        window['-COL3-'].Update(visible=True)
        window['-COL7-'].Update(visible=False)
        window['-COL8-'].Update(visible=False)
    elif event=="Cleaned Data":
        window['-COL-'].Update(visible=False)
        window['-COL2-'].Update(visible=False)
        window['-COL3-'].Update(visible=False)
        window['-COL7-'].Update(visible=True)
        window['-COL8-'].Update(visible=False)
    elif event=="Removed Data":
        window['-COL-'].Update(visible=False)
        window['-COL2-'].Update(visible=False)
        window['-COL3-'].Update(visible=False)
        window['-COL7-'].Update(visible=False)
        window['-COL8-'].Update(visible=True)
    elif event=="Correlation Table1":
        window['-COL4-'].Update(visible=True)
    elif event=="Correlation Table2":
        window['-COL5-'].Update(visible=True)
    elif event=="GDP per capita vs Suicide rate":
        plt.clf()
        x= sui[['GDP per capita']].values.tolist()
        y= sui[['Suicide rate']].values.tolist()
        a='GDP per capita vs Suicide rate'
        b='GDP per capita '
        c='suicide rate'  
        layout5= [[sg.Text("Graph", key="new",size=(100,1))],[sg.Canvas(key='-CANVAS-',size=(100, 100))]]
        scattergraph(x,y)
    elif event=="Life Expectancy of Men vs Women":
        plt.clf()
        x= life[['Life Expectancy (years) - Men']].values.tolist()
        y= life[['Life Expectancy (years) - Women']].values.tolist()
        a='Life Expectancy of Men vs Women'
        b='Life Expectancy (years) - Men'
        c='Life Expectancy (years) - Women'        
        scattergraph(x,y)
    elif event=="Life Expectancy of Women vs Happiness Score":
        plt.clf()
        x= life[['Happiness Score']].values.tolist()
        y= life[['Life Expectancy (years) - Women']].values.tolist()
        a='Life Expectancy of Women vs Happiness Score'
        b='Happiness Score'
        c='Life Expectancy (years) - Women'
        scattergraph(x,y)
    elif event=="Life Expectancy of Men vs Happiness Score":
        plt.clf()
        x= life[['Happiness Score']].values.tolist()
        y= life[['Life Expectancy (years) - Men']].values.tolist()
        a='Life Expectancy of Men vs Happiness Score'
        b='Happiness Score'
        c='Life Expectancy (years) - Men'        
        scattergraph(x,y)
    elif event=="Happiness Score vs Fertility Rate":
        plt.clf()
        x= life[['Happiness Score']].values.tolist()
        y= life[['Fertility Rate (births per woman)']].values.tolist()
        a='Happiness Score vs Fertility Rate (births per woman)'
        b='Happiness Score'
        c='Fertility Rate (births per woman)'       
        scattergraph(x,y)
    elif event=="Correlation Table3":
        window['-COL6-'].Update(visible=True)         
    elif event=="pair plot":
        pairplot()
        
    elif event=="Bar Graph":
        bargraph()            
window.close()


# In[17]:


sort=newdf.sort_values(by=['Suicide rate'],ascending=False)
sort.head()


# In[15]:


titanic = sns.load_dataset("titanic")
sns.catplot(data=titanic, x="sex", y="survived", hue="class", kind="bar")


# In[ ]:




