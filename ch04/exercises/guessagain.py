import random
input = int(input("Guess a number:"))
answer = random.randint(1,10)
while answer != input:
    if input < answer:
        print("Too low")
        input = int(input("Enter another number:"))
    elif input > answer:  
        print("Too high!")
        input = int(input("Enter number again:"))
    else:
        break
print("You guessed right!!")
