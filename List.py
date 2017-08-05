array_list =[2,8,6,9,10,3,5,0,2,4,3,50,1,32]
print "Check which numbers in the list of the system are less than 5  "

num = 5
new_list = []
for i in array_list:
    if i <  num:
       new_list.append(i)

print  new_list