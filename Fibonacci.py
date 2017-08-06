def fibonacci(num) :
    num_array = []
    num1 = 0
    num2 = 1
    num_array.append(int(num1))
    num_array.append(int(num2))
    for i in range(1,num+1) :
        num3 = num1 + num2
        num_array.append(int(num3))
        num1 = num2
        num2 = num3

    print "Fibonacci Series is : ",num_array
num = int(raw_input("Enter the number of fibonacci :"))
fibonacci(num)