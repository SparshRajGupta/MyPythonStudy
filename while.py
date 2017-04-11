n = 23
r = True

while r:
    guess = int(raw_input('Enter a number: '))

    if guess == n:
        print 'You are correct'
        r = False

    elif guess > n:
        print 'Guess a lower number'

    elif guess < n:
        print 'Guess a higher number'

else:
    print 'Loop is over'

print 'Done'
