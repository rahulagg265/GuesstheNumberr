import random
n=random.randint(1,20)
ctr=0
while ctr<5:
    guess=int(input("guess a number between 1 to 20"))
    if guess==n:
        print("congratulation,for wining")
        break
    else:
        ctr=ctr+1
if not ctr<5:
    print("try again you loose")
    print("wining number",n)
