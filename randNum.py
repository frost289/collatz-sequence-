import random

count = 1

number = random.randint(1,11)

userInput = int(input('enter a number between 1 and 10. you have 10 tries \n'))



while userInput != number:
    if userInput > number:
        print('the number is too high, try again \n')
        userInput = int(input('enter a number between 1 and 10 \n'))
    elif userInput < number:
        print('the number is too low, try again \n')
        userInput = int(input('enter a number between 1 and 10 \n'))
    elif userInput == number or count == 0:
        print('that correct')
        break
    count-=1
    