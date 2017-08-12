from random import randint

randomNum =  randint(0, 99)
print randomNum

tries = 0;
while tries<9:
    input = int(raw_input("Guess a number between 0 and 99: "))
    if input != randomNum:
        print "number you guessed was wrong"
        tries+=1
    else:
        print "you guessed it right"
        break
else:
    print "oops! your tries exceeded the limit"
    print "The correct answer is - ", randomNum
