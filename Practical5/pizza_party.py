#p is the number of pieces
#n is the number of cuts
#p==(n**2+n+2)/2
#print(p pieces of pizza can be cut for n cuts)
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
