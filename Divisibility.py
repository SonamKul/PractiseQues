starting_no = 2000
ending_no = 3200
numbers = []
for i in range(starting_no, ending_no) :
    if(i % 7 == 0) and (i % 5 != 0 ) :
        numbers.append(i)
print numbers
