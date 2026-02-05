import random
number_to_guess = random.randint(1 ,100)

while True:
    try:
        guess = int(input('please guess any mumber between 1 to 100:  '))

        if guess < number_to_guess:
            print('number is too low')

        elif guess > number_to_guess:
            print('number is too high')

        else:
            print('you guessed it right!')
            break
    except ValueError:
        print('pls enter a valid number')