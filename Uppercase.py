import time
print "Enter a string and change it to Upper case or Lower case as per your choice \n Enter 1 - Upper case String. \n 2 - Lower case"

time.sleep(1)
str = raw_input("Enter a String : \n")
time.sleep(1)

choice = int(raw_input("Enter your choice : \n"))
if choice == 1 :
    new_str = str.upper()
    print new_str
elif choice == 2 :
    new_str = str.lower()
    print new_str

