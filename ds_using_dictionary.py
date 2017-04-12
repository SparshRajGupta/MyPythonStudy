ab = {'Swaroop': 'swaroop@gmail.com',
      'Larry': 'larry@gmail.com',
     'Sparsh': 'sparsh@gmail.com'}

print "Swaroop's address is: ",ab['Swaroop']

del ab['Larry']

ab ['kshitiz'] = 'kshitiz@gmail.com'

print '\n There are {} contacts in the address-book \n'.format(len(ab))

for name, address in ab.items():
    print 'Contact {} at {}'.format(name, address)



if 'kshitiz' in ab:
    print "\n Kshitiz's address is", ab['kshitiz']