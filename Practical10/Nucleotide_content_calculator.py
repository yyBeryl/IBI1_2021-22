sequence=input("Please enter the sequence:")#input a DNA sequence
def s(x):
    x=list(x.upper())#Converting lower case letters to upper case
#xalculate the percentage of A,C,G and T
    pA=x.count("A")/len(x)
    print("The percentage of A in this sequence is " + str(pA) +".")
    pT=x.count("T")/len(x)
    print("The percentage of T in this sequence is " + str(pT) +".")
    pG=x.count("G")/len(x)
    print("The percentage of G in this sequence is " + str(pG) +".")
    pC=x.count("C")/len(x)
    print("The percentage of C in this sequence is " + str(pC) +".")
    return x
s(sequence)
#example
e="aaTTgcatG"
s(e)
