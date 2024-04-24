# Python3 code to demonstrate working of 
# Functions as dictionary values
# Using Without params
 
def balaji():
	return "This is my bank balance"

# initializing dictionary
# check for function name as key
test_dict = {"fname": balaji, "age" : 50, "address" : "salem"}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# calling function using brackets 
res = test_dict['fname']()

# printing result 
print("The required call result : " + str(res)) 
