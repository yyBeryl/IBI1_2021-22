seq = 'ATGCAATCGACTACGATCAATCGAGGGCC'
n=seq.find('GAATTC')
m=n+1
if n >= 0:
    print('The sequence would be cut to '+m+' fragments')
else:
    print('This sequence would not be cut and the number of fragments is 1.')