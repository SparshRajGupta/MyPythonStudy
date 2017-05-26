n = int(raw_input("Enter a num: "))         #Using list-comprehensions, set and sort function
input_list = []
if n >= 2 and n <= 10:
    input_list = [int(x) for x in raw_input("Enter an array of nos. seperated by space: ").split() if (int(x) >= -100 and int(x) <= 100)]
    new_list = list(set(input_list))
    new_list.sort()
    print ("New Sorted List:{}").format(new_list)
    print ("Second Largest No.: {}").format(new_list[-2])