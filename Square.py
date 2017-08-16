import time

num_list = []
number = int(raw_input("Enter the number till where you want to have squares : "))
time.sleep(1)
for i in range(number+1) :
    add = {i,i*i}
    num_list.append(add)
    list(num_list)
print num_list