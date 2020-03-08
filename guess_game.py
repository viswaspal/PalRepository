import random
count=1
def guess(N,a):
    if(N==a):
        print("You win")
        print("Game Over")
    elif(N<a):
        print("less")
    elif(N>a):
        print("more")
    else:
        pass
print("This is number guessing game")
print("You win if you guess a correct number")
N=int(input("Please enter a no.in range 0 to 100 -->"))
a=random.randint(0,100)
guess(N,a)
while(N!=a):
    N=int(input("Guess another number->"))
    count+=1
    guess(N,a)
print(f'You use {count} attempts')
print('Thank You')
