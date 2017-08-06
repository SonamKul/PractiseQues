import random
number = random.randint(1,7)
print "Guessing Game. Guess a number of your choice and compare it that of computer whether it is low,high or equal to it."
user = int(raw_input("Enter a number of your choice : "))
if user < number :
    print "System generated random number is : ",number
    print "Your number is low. Sorry, Try again."
elif user == number :
    print "System generated random number is : ", number
    print "Congratulations!! You won."
elif user > number :
    print "System generated random number is : ", number
    print "Your number is high. Sorry, Try again. "