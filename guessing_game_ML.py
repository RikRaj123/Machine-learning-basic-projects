import random
import math

lower = int(input("Enter Lower bound:- "))
upper = int(input("Enter Upper bound:- "))
num=[]

for i in range(lower,upper+1):
    num.append(i)
num2 = random.choice(num)
print(num)

print("you have 3 guesses")
for i in range(0,3):
    guess= int(input("guess a number : "))
    if(guess==num2):
        print("right you won")
    else:
        print("better luck next time")