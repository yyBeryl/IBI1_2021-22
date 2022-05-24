seq = 'ATGCAATCGACTACGATCAATCGAGGGCC'#Input a sequence
n=seq.find('GAATTC')#n is the number of GAATTC in seq
m=n+1#m is the number of fragments generated
#Check whether the script contains the variable seq
if n >= 0:
    print('The sequence would be cut to '+m+' fragments')
else:
    print('This sequence would not be cut and the number of fragments is 1.')#the result is this situationgiy
