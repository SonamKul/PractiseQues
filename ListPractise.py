import time
list = ['Sonam',786,80.2,'Vikram',70.2]
print "List is :\n " , list
time.sleep(2)
print "Index 0 in the list is having the value : " + list[0]
time.sleep(2)
print "The list at [1:3] is : " , list[1:3]
time.sleep(2)
print "The list at [2:] is : " , list[2:]
time.sleep(2)
print "The list at [1:3] is : " , list[1:3]
time.sleep(2)
tiny_tupple = ['Hello',70.58]
print "The tiny_list value after (tiny_tupple * 2) is : " , (tiny_tupple * 2)
time.sleep(2)
tiny = tiny_tupple + list
print "The concate of tupple and tiny_tupple is : \n", tiny