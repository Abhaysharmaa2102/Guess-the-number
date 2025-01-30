import random
rd_number= random.randint(1,100)
print(rd_number)
chance=1
score=110
while chance<=10:
    user=int(input(" Guess The Number= "))
    if rd_number==user:
        score = score - (chance * 10)
        print("You Won")
        print(score)
        break
    elif user>rd_number:
        print("Hint:     Go Lower")
        print(f'you have chances left:{10-chance}')
    elif user<rd_number:
        print("Hint:    Go Higher")
        print(f'you have chances left:{10-chance}')
    chance=chance+1
else:
    print(f"you have consumed your all chances.'you Lost'")
    print(f"random Number Was: {rd_number}")


