n = int(raw_input("Enter a no.: "))
c = 0
for x in range(1,n+1):
    if (n % x == 0):
        c = c +1

if (c <= 2):
    print ("{} is a prime no.").format(n)
else:
    print ("{} is a not a prime no.").format(n)