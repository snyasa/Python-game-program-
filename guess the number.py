import random
m=int(input("enter lower limit"))
n=int(input("enter upper limit"))
flag=0
while (flag==0):
    you=int(input("Enter your number;="))
    x=random.randrange(m,n)
    if x==you:
        print("You guessed it right")
        flag==1
        break
    else:
        if x>you:
            print("Hint::Number is greater than your input....Guess again")
        elif x<you:
            print("Hint:: Number is less than your input...Guess again")
        elif x >((n-m)//2):
            print("Hint :: Number is greater than ",(n-m//2),"....Guess again")
        elif x<((n-m)//2):
            print("Hint :: Number is less than",(n-m//2),"....Guess again")
else:
    print("Game ends")
