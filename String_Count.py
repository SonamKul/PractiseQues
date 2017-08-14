import time
print "Count the number of Upper Case letters and Lower Case letters in a string"
time.sleep(2)
message = raw_input("Enter a string here : ")

print("Upper Case Letters : ", sum(1 for c in message if c.isupper()))
print("Lower Case Letters : ", sum(1 for c in message if c.islower()))
