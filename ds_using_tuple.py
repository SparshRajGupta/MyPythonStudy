zoo =('pytyon','tiger','elephant','parrot','crocodile')

print ('No. of animals in the zoo: '),len(zoo)

new_zoo = ('penguin','monkey',zoo)

print 'All animals in the new zoo are: ', new_zoo

print 'No .of cages in the new zoo are: ',len(new_zoo)

print 'Animals brought from old zoo are: ', new_zoo[2]

print 'Last animal brought from old zoo is: ',new_zoo[2][4]

print 'Number of animals in the new zoo are: ',len(new_zoo)-1+len(new_zoo[2])