bri = set(['brazil','russia','india'])
print 'india in set bri (True/False): ','india' in bri,'\n'

print 'us in set bri (True/False): ','usa' in bri,'\n'

bric = bri.copy()                               #copy bri into bric
bric.add('china'),'\n'                          #china added
print 'Contents of bric: ',bric,'\n'

print 'bric is a superset of bri (True/False): ', bric.issuperset(bri), '\n'

bri.remove('russia')                            #russia removed
print 'Contents of bri', bri, '\n'

print 'AND of bri & bric: ', bri & bric