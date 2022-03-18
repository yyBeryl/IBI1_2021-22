#p is the number of pieces
#n is the number of cuts
#p==(n**2+n+2)/2
#This formula was obtained from the practical 5 provided by my teacher
#the final line print(p pieces of pizza can be cut for n cuts)
#I had help from a fellow student in class to know how to use "str" to print figures and text together.
#repeat until p>=64

n=1
p=2
print(str(p)+' pieces of pizza can be cut for '+ str(n)+' cut')
while 1==1:
	p=(n**2+n+2)/2
	print(str(p)+' pieces of pizza can be cut for '+ str(n)+' cuts')
	n+=1
	if p>=64:
		break
