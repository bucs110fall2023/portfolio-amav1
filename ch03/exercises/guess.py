import random
answer = random.randint(1,10)

for i in range(3):
    guess = int(input("Guess a number:"))
    if guess < answer:
        print("Too low")
    elif guess > answer:  
        print("Too high!")
    else:
        print("You guessed right!! The number was", answer)
        break







# import pygame
# import random
# pygame.init()
# screen = pygame.display.set_mode()

# colors = ["red", "green" ,"blue", "yellow"]
# random.shuffle(colors)
# print(colors)

# msg = """ 
#     use your arrow keys:
#     UP: red
#     DOWN: green
#     LEFT: blue
#     RIGHT: yellow
#     press any key when ready
# """

# input(msg)

# # # talking to OS
# # ```py

# # events = pygame.event.get() #events that happen since last call

# # ```

# # #the event loop - where you respond to events, you can have multiple event loops, but only running per frame
# # ###event objects - containers with data about the event

# # pygame.event_name
# for color in colors:
#     screen.fill(color)
#     pygame.display.flip()
#     pygame.time.wait(500)

# input(msg)
# user_guess = []
# for event in pygame.event.get():
#     if event.type == pygame.KEYDOWN:
#         if event.key == pygame.K_UP
#             user_guess.append("red")
#         elif event.key == pygame.K_DOWN
#             user_guess.append("green")
#         elif event.key == pygame.K_LEFT
#             user_guess.append("blue")
#         elif event.key == pygame.K_RIGHT
#             user_guess.append("yellow")

#     elif event.type == pygame.MOUSEBUTTONDOWN:
#         print(event.pos)

# print(user_guess, colors)
# if user_guess == colors:
#     print("you won")
# else:
#     print("pay attention, do better!")