import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
n = print("What do you want to choose: 1 for Rock or 2 for Paper or 3 for Scissors? ")
n = int(input())
if n==1:
  print(rock)
elif n==2:
  print(paper)
elif n==3:
  print(scissors)
print("Computer Chose:")
m = random.randint(1, 3)
if m==1:
  print(rock)
elif m==2:
  print(paper)
elif m==3:
  print(scissors)

if n==m:
  print("Its a tie 🤝")
elif n==1 and m==2:
  print("Losser 👎")
elif n==1 and m==3:
  print("You win 👍🏻")
  
elif n==2 and m==3:
  print("Losser 👎")
elif n==2 and m==1:
  print("You win 👍🏻")
  
elif n==3 and m==1:
  print("Losser 👎")
elif n==3 and m==2:
  print("You win 👍🏻")

  