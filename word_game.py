import random
import math

word=["rome","italy","india","bangladesh"]
a=0
pos=[]
guess_word=random.choice(word)


print("you have 12 guesses")
for i in range(0,12):
    guess= input("guess an alphabet : ")
    for j in range(0,len(guess_word)):
        if(guess==guess_word[j]):
            print("right. it is at",j+1)
            a=1
    if(a==0):
        print("wrong guess try again.")