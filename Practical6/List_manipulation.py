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
