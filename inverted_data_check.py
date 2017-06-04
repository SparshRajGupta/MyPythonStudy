s = raw_input("Enter a string/nos: ")           #check if revered data is same as original
list = []
rlist = s[::-1]                 #reversed string
for val in s:
    list.append(val)

print list
print ("Revered Data:{} ").format(rlist)

if (s == rlist):
    print ("Inverted data is same as original")
else:
    print ("Inverted data is different")

