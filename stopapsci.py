import random
options=['rock', 'paper', 'scissors']
user=input("Enter your choice (rock, paper, scissors): ")
system=random.choice(options)
print("My choice:", user)
print("System choice:", system)
if user==system:
    print("It's a tie!")
elif (user=='rock' and system=='scissors') or (user=='paper' and system=='rock') or (user=='scissors' and system=='paper'):
    print("You win!")
else:
    print("System wins!")