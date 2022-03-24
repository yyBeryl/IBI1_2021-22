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
