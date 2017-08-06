print "Reverse of a String Program"
string = raw_input("Enter a String : ")
reversed_string = " ".join(string.split(" ")[::-1])
print "Reversed string is :", reversed_string
