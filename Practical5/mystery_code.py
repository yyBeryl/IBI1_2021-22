# What does this piece of code do?
# Answer:print the 10th random number between 1 and 100

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

progress=0
#assign 0 to progress
while progress<10:
#run until progress>=10
	progress+=1
#assign the value of progress+1 to progress
	n = randint(1,100)
#assign a random number between 1 and  100 to n

print(n)
