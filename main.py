from random import randint

num=randint(1,100)
guesses=1
yourGuess=0
while yourGuess!=num:
    yourGuess=int(input("Enter a number between 1 and 100:"))

    if(num>yourGuess):
        print("Higher number please!")
        guesses+=1
    elif(num<yourGuess):
        print("Lower number please!")
        guesses+=1
    
print(f"You guessed the number {num} correctly in {guesses} attempts")