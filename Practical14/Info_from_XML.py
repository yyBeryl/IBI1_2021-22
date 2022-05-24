#calculate the total number of terms
import matplotlib.pyplot as plt
from xml.dom.minidom import parse as xml_parse
document=xml_parse('go_obo.xml')#import the xml file
root=document.documentElement
terms=root.getElementsByTagName('term')#get all terms
print('The total number of terms currently recorded in the Gene Ontology is '+str(len(terms))+'.')#calculate the total number of 'term'
#calculate the number of childNodes for each term
    #generate a dictionary storing the correspondence of all terms and their childNodes
dict={}#create a dictionary to store all terms and their childNodes
for term in terms:
    PN=[]#create a list to store all parentNodes
    for i in term.getElementsByTagName('is_a'):#check all terms
        PN.append(i.childNodes[0].data)#append the parentNode in the loop to PN
    Terms=term.getElementsByTagName('id')[0].childNodes[0].data#Terms is the id of the term in the loop
    for is_a in PN:#check all parentNodes
        if is_a in dict:#add terms to its parentNodes
            dict[is_a].append(Terms)
        else:#add the new parenNodes and its childNodes
            dict[is_a]=[Terms]
    #a function to calculate the number of childNodes of each term
def c(L):#L is a later entered list
    for e in L:#check every group of term and its childNodes
        #get all elements in lists which are in lists out to count
        if e not in listL:#listL is the list of all childNodes of a term
            listL.append(e)
            if e in dict:#this means i still has childNodes
                c(dict[e])#this move will add all childNodes (reach the bottom)
    return len(listL)#length of listL is the number of childNodes of one term
#get the total number of childNodes across all terms
total=[]#create a list to store total childNodes
for term in terms:#check every term
    childnodes=0#define the number of childNodes
    listL=[]
    Terms=term.getElementsByTagName('id')[0].childNodes[0].data#Terms is the id of the term in the loop
    if Terms in dict:
        childnodes=c(dict[Terms])#count the number of childNodes of the term in the loop
    else:
        childnodes=0#means the term in the loop not in the dictionary
    total.append(childnodes)#store the number in the total list
#make a boxplot to show the distribution of childNodes across all terms
plt.boxplot(total,
            labels= ['Gene Ontology'],#label the x axis
            )
plt.title('The distribution of childnodes across terms')#title the figure
plt.ylabel('childNodes')#label the y axis
plt.show()
#get the translated number of childNodes across all terms
translated=[]#create a list to store childNodes of terms associated with translation
for term in terms:#check every term
    if 'translation' in term.getElementsByTagName('defstr')[0].childNodes[0].data:#get terms associated with translation
        Terms=term.getElementsByTagName('id')[0].childNodes[0].data#Terms is the id of the term in the loop
        if Terms in dict:
            childnodes=c(dict[Terms])#count the number of childNodes of the term in the loop
        translated.append(childnodes)
#make a boxplot to show the distribution of childNodes across terms associated with translation
plt.boxplot(translated,
            labels= ['Translation Gene Ontology'],#label the x axis
            )
plt.title('The distribution of childnodes across translation terms')#title the figure
plt.ylabel('childNodes')#label the y axis
plt.show()
#calculate the average
a_total=sum(total)/len(total)#calculate the average of total
a_translated=sum(translated)/len(translated)#calculate the average of translated
print('The childNodes of total terms on average is '+str(a_total)+'.')
print('The childNodes of translation terms on average is '+str(a_translated)+'.')
if a_translated>a_total:
    print('The ‘translation’ terms contain, on average, a greater number of child nodes than the overall Gene Ontology.')
else:
    print('The ‘translation’ terms contain, on average, a smaller number of child nodes than the overall Gene Ontology.')



