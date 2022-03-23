import matplotlib.pyplot as plt
import numpy as np
#input my data
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
plt.title('List manipulation')
plt.xlabel('marks')
plt.show()
#write sth. to calculate whether Rob passes IBI
s=sum(x)
m=s/8
if m>=60:
	print("With a score of 60 or more, Rob passed the IBI course.")
else:
	print("With a score lower than 60, Rob didn't pass the IBI course.")


