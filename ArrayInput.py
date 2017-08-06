def list(number) :
    num_array = []
    print "Enter the values in the array."
    for i in range(1,number+1) :
        no = raw_input("Number :" )
        num_array.append(int(no))
        new_list = []
        new_list.append(num_array[0])
        new_list.append(num_array[-1])
    print "Inputted Array : ",num_array
    print "New Array : ",new_list
number = int(raw_input("Enter the number of elements you want in the list : "))
list(number)


