import random
m=int(input())
n=input()
a="Rock"
b="Scissors"
c="Paper"
while(m!=0):
    x=random.randrange(a,c)
    if x==1 and n == "Scissors":
        print("You lose")
    else:
        print("You win")
    if x==2 and n=="Paper":
        print("You lose")
    else:
        print("You win")
    if x==3 and n=="Rock":
        print("You win")
    else:
        print("You lose")
    m=m-1

