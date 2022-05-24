#create a dictionary containing the info of the parental age and CHD
PC={30:1.03,35:1.07,40:1.11,45:1.17,50:1.23,55:1.32,60:1.42,65:1.55,70:1.72,75:1.94}
import random
#x is parental age
x=[30,35,40,45,50,55,60,65,70,75]
#input one value from the parental age to simulate an imput from the user
#display the frequency table
dict={a:PC[a]}
#I searched the Internet to learn how to do this
#the website is https://www.jb51.net/article/199816.htm
print('The risk for CHD in the offspring is '+str(PC[a])+' of a father of '+str(a)+'.')
print(dict)
#take 30 as an example
example=30
dict={example:PC[example]}
print('The risk for CHD in the offspring is '+str(PC[a])+' of a father of '+str(example)+'.')
print(dict)

import matplotlib.pyplot as plt
import numpy as np
#create the data I need
x=[30,35,40,45,50,55,60,65,70,75]
#x is parental age
y=[1.03,1.07,1.11,1.17,1.23,1.32,1.42,1.55,1.72,1.94]
#y is  the relative risk for congenital heart disease in the offspring 
#create a figure
fig=plt.figure(1)
plt.scatter(x,y,marker='o')
#name the figure,x axis and y axis
plt.title('parental age vs offspring health')
plt.xlabel('parental_age')
plt.ylabel('chd')
#show the figure
plt.show()
