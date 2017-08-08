spy_name = raw_input("Provide your name here : ")
if len(spy_name) > 0 :
    print "Alright "+ spy_name + "i'd like to know more about you before proceeding further. "
    spy_salutation = raw_input("Provide your salutation whether Mr. or Ms. : ")
    spy_name = spy_salutation + "." + spy_name  # the old value get's overwritten here in spy_name
    print "Welcome " + spy_name + ".Glad to have you back here "
    # Check the year when u will be of 100.

    spy_age = int(raw_input("Enter your age : "))
    print  "Your age in 2017 is %d" % (spy_age)

    age = (100 - spy_age) + 2017
    print "You will be of 100 years in %d" % (age) + " year."
else:
    print "Name cannot be empty. Re-enter your name please."

