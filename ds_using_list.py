shoplist = ['apple','mango','banana','orange']

print 'I have', len(shoplist),'items to purchase'

print 'These items are: '
for item in shoplist:
    print item

print 'I have to buy rice'
shoplist.append('rice')                         #append item to shopping cart
print 'My shopping list is now: ',shoplist

print 'I will sort my list now'
shoplist.sort()                                 #sorting shopping cart
print 'Sorted shopping list is: ',shoplist

print 'The first item I will buy is ', shoplist[0]

olditem = shoplist[0]

del shoplist[0]                                 #deleting first item in the shopping cart
print 'I bought the ', olditem

print 'My shopping list is now: ',shoplist