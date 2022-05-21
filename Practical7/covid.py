#code for importing the .csv file
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
covid_data=pd.read_csv("full_data.csv")

#code for showing the first and third columns from rows 10-20
my_columns=[True,False,True,False,False,False]#Choose needed colums
print(covid_data.iloc[10:20,my_columns])

#use Boolean to show total_cases for all rows corresponding to Afghanistan
my_column=[False,True,False,False,True,False]
print(covid_data.loc[(covid_data["location"]=="Afghanistan"),my_column])#Choose Afghanistan

#the mean number of new cases and new deaths in China
my_columns=[True,False,True,True,False,False]
china_new_data=covid_data.loc[(covid_data["location"]=="China"),my_columns]
a=np.mean(china_new_data["new_cases"])#a is the mean of new cases in China
b=np.mean(china_new_data["new_deaths"])#b is the mean of new deaths in China
print(str(a)+" is the mean of new cases in China.")
print(str(b)+" is the mean of new deaths in China.")

#a boxplot of new cases and new deaths in China
data=[(china_new_data["new_cases"]),(china_new_data["new_deaths"])]
plt.boxplot(data, positions=[1, 2], widths=0.5, patch_artist=True,
                showmeans=False, showfliers=False,
                medianprops={"color": "yellow", "linewidth": 0.5},
                boxprops={"facecolor": "lightskyblue", "edgecolor": "white",
                          "linewidth": 0.5},
                whiskerprops={"color": "lightblue", "linewidth": 1},
                capprops={"color": "C0", "linewidth": 1},labels=("new_cases","new_deaths"))#Change some parameters of the figure
plt.title('china new cases and deaths')#Title this graph
plt.ylabel('people')#Title the y axis
plt.show()

#plot both new cases and new deaths in China over time
x=list(china_new_data["date"])#x is the date
y1=list(china_new_data["new_cases"])#y1 is new cases in China
y2=list(china_new_data["new_deaths"])#y2 is new deaths in China
plt.plot(x,y1,'b+')#Choose blue +
plt.plot(x,y2,'r+')#Choose red +
plt.title('china new cases and deaths')#TItle this graph
plt.xticks(china_new_data["date"].iloc[0:len(china_new_data["date"]):4],rotation=-90)
plt.xlabel('date')
plt.ylabel('people')
plt.show()

#code to answer the question stated in file question.txt
my_columns=[True,False,True,False,True,False]
spain_data=covid_data.loc[(covid_data["location"]=="Spain"),my_columns]
x=list(spain_data["date"])#x is the date
y1=list(spain_data["new_cases"])#y1 is new cases in Spain
y2=list(spain_data["total_cases"])#y2 is total cases in Spain
plt.plot(x,y1,'b+')#Choose blue +
plt.plot(x,y2,'r+')#Choose red +
plt.title('new cases and total cases of spain')#Title this graph
plt.xticks(spain_data["date"].iloc[0:len(spain_data["date"]):4],rotation=-90)#Make appropriate and readable horizontal coordinate labels
plt.xlabel('date')#Title the x axis
plt.ylabel('people')#Title the y axis
plt.show()
