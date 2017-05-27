a = int(raw_input('Enter 1st no. : '))       #Input 2 nos from thue user
b = int(raw_input('Enter 2nd no. : '))

if a > b:
    greater = a
else:
    greater = b

    while(True):
        if ((greater % a == 0) and (greater % b ==0)):
            lcm =greater
            break
        greater+=1

print ("LCM of entered nos.:{} ").format(lcm)