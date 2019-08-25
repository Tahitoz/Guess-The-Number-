import random

print('Hello! What is your name?')
name = input()
print('Well,', name, ', I am thinking of a number between 1 and 20.')

answer = random.randint(1,20)
counter = 0

while True:
    print('Take a guess.')
    guess = input()
    counter = counter + 1
    if int(guess) > int(answer):
        print('Your guess is too high.')
        continue
    elif int(guess) < int(answer):
        print('Your guess is too low.')
        continue
    elif int(guess) == int(answer):
        print('Good job,', name, '! You guessed my number in', counter, 'guesses!')
        break
