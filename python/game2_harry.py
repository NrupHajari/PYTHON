import random
randnumber = random.randint(1,100)
userguess= None
guesses=0

while(userguess != randnumber):
    userguess = int(input("enter guess: "))
    guesses += 1
    if(userguess==randnumber):
        print(" you guess right ")

    elif(userguess > randnumber):
        print("worng guess ! enter smaller number")

    elif(userguess < randnumber):
        print("wrong guess ! enter larger number")

print(f" you guess number {guesses} guesses") 