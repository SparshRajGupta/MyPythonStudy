number = 25
guess = int(raw_input('Enter a number: '))

if guess == number:
    print 'You guessed it right'

elif guess < number:
    print 'Guess a higher number'

elif guess > number:
    print 'Guess a lower number'

print 'Done'

