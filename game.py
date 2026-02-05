# generate a random number
import random
number_to_guess = random.randint(1 ,100)

# While loop so that it deosnt end afetr one cycle
while True:

    # try for if the number is not valid
    try:
        # ask the user to makea guess
        guess = int(input('please guess any mumber between 1 to 100:  '))

        # if-elif-else loop for conditional stmts
        if guess < number_to_guess:
            print('number is too low')

        elif guess > number_to_guess:
            print('number is too high')

        else:
            print('you guessed it right!')

        # break to end while loop
        break
    
    except ValueError:
        print('pls enter a valid number')