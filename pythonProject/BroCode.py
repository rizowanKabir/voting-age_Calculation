import random
options = ("rock","paper","pen","scissors","sharp_ner")

player = None
computer = random.choice(options)
player = input("Enter a choice (rock,paper,pen,scissors,sharp_ner) :")
print(f"player : {player}")
print(f"Computer :{computer}")