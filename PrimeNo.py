print "Check whether number is Prime or not."
number = int(raw_input("Enter the number which you want to check : "))
for i in range(2,number) :
    if(number % i == 0) :
        print "Number is not a Prime Number."
        break
else :
    print "Number is a Prime Number. "

