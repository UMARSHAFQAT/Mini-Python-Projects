import random

random_number=random.randint(1,100)

while True:
    number=(input("Guess a number between 1 to 100 or If you want to quit type Q:"))
    if number== ("Q".lower()):
        print(".........Game-over.........")
        break  
    
    number=int(number)
    if number==random_number:
        print("Congratulations you have guessed the correct number!")
        break
    
    elif number <= random_number:
        print("WRONG\nHint: guess a greater number")
    
    else:
        print("WRONG.\nHint: guess a lesser number")
    
