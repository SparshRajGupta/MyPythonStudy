n = int(raw_input("Enter a no.: "))
length = len(str(n))                    #Length of entered no

sum =0
d = n

for x in range (length):
    a = d%10
    c = 1
    for b in range(length):
        c = c*a
    sum = sum + c
    d = d/10


if (sum == n):
    print ("{} is an armstrong no.").format(n)
else:
    print ("{} is not an armstrong no.").format(n)
