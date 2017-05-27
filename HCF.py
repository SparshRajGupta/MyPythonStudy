a = int(raw_input('Enter 1st no. : '))       #Input 2 nos from thue user
b = int(raw_input('Enter 2nd no. : '))

factor_of_a = [x for x in range(1,a) if a % x == 0]         #Finding factors using list comprehensions
factor_of_b = [y for y in range(1,b) if b % y == 0]

print ("Factors of 1st no.:{} ").format(factor_of_a)
print ("Factors of 2nd no.:{} ").format(factor_of_b)

intersection = [val for val in factor_of_a if val in factor_of_b]
print ("List of common factors:{} ").format(intersection)

length = len(intersection)
print ("Highest Common Factor:{} ").format(intersection[length-1])