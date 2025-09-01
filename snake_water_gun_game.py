import random

def game(computer, you):
    if computer == you:
        return None
    
    # Snake rules
    elif computer == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    
    # Water rules
    elif computer == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
    
    # Gun rules
    elif computer == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True

print("Computer's Turn: Snake(s), Water(w), or Gun(g)?")
randNo = random.randint(1, 3)  
if randNo == 1:
    computer = 's'
elif randNo == 2:
    computer = 'w'
else:
    computer = 'g'

you = input("Your Turn: Snake(s), Water(w), or Gun(g)? ")

print(f"Computer chose {computer}")
print(f"You chose {you}")

result = game(computer, you)

if result is None:
    print("It's a Draw!")
elif result:
    print("You Win 🎉")
else:
    print("You Lose 😢")
