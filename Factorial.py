import time
print "Find the factorial of any number by inputting it in Console."
time.sleep(1)
number = int(raw_input("Enter the number : "))
fact = 1
for i in range(1,number+1) :
    fact = fact * i
print "The factorial of %d" %number + " is %d" %fact
