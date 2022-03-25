import matplotlib.pyplot as plt
import numpy as np
#input my data
#x is marks
x=[45,36,86,57,53,92,65,45]
#set parameters
bp=plt.boxplot(x,
	notch=False,
	#show in Non-concave form
	whis=1.5,
	#1.5 times quartile difference
	medianprops={'color':'blue'},
	vert=False,
	#Lay out my chart horizontally
	showmeans=True,
	whiskerprops={'color':'blue'},
	boxprops={'color':'green'}
	#Outliers are shown in red
	)
#name the title and x axis
plt.title('List manipulation')
plt.xlabel('marks')
plt.show()
#to print the sorted values of marks
#save these sorted values in "y"
y=sorted(x)
print("Rob's marks across the semester are "+str(y))
#to calculate whether Rob passes IBI
#caculate the mean of marks
m=sum(x)/len(x)
print("Rob's average mark of the IBI course in this semester is "+str(m))
#I learned this way from this website https://www.jb51.net/article/176500.htm
if m>=60:
	print("With a score of 60 or more, Rob passed the IBI course!")
else:
	print("With a score lower than 60, Rob didn't pass the IBI course.")


