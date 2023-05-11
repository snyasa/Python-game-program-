#Roll the dice
import random
n=int(input("Enter how many times you want to roll the dice="))
z=0
while(z<n):
    print("Roll the dice",u'\U0001F3B2')
    x=random.randint(1,6)
    print(x)
    z=z+1
    
