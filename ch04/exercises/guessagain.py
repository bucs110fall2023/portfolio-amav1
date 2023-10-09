import random
guess = int(input("Guess a number:"))
tries = 1 
answer = random.randint(1,1000) + 1
while guess != answer:
    tries+=1
    if guess < answer:
        print("Too low")
    elif guess > answer:  
        print("Too high!")
    guess = int(input("Again, what number, between 1-1000, do you want to guess?"))
print("Correct. It took you", tries, "guesses")
print("It should only take you, at most", 9, "guesses")