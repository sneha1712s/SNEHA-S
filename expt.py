'''
try:
    # code that may cause exception
except:
    # code to run when exception occurs
'''    
#balaji=5/0
#print(balaji)
'''a=assert num % 2 == 0
print(a)'''
'''
try:
    num = 10
    deno = 0#ArithmeticError

    result = num/deno

    print(result)
except:
    print("Error: Denominator cannot be 0.")

# Output: Error: Denominator cannot be 0.


try:
    
    even_numbers = [2,4,6,8]
    print(even_numbers[2]/0)

except ZeroDivisionError:
    print("Denominator cannot be 0.")
    
except IndexError:
    print("Index Out of Bound.")

# Output: Index Out of Bound
'''

# program to print the reciprocal of even numbers
'''
try:
    num = int(input("Enter a number: "))
    assert num % 2 == 0 #The assert keyword is used when debugging code.The assert keyword lets you test if a condition in your code returns True, if not, the program will raise an AssertionError.
except:
    print("Not an even number!")
else:
    reciprocal = 1/num
    print(reciprocal)
    
'''
try:
    num = 10
    deno = 10
    result = num/deno 
except:
    print("Error: Denominator cannot be 0.")
    
finally:
    print("This is finally block.")

    

















#print(dir(locals()['__builtins__']))

'''ib-5L
sbi-10L
icici-25L
hdfc-30L
UB-50L'''








