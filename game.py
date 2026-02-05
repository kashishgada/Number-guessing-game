# generate a random number
import random

number_to_guess = random.randint(1 ,100)

# loop
#     ask the user to makea guess
guess = int(input('please guess any mumber between 1 to 100:  '))

#     if the number is not valid
#         print error not a valid number
#     if number < guess
#         print too low
#     if number > guess
#         print too high
#     else
#             print well done you found the number