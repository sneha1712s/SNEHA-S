# Reads two numbers from input and typecasts them to int using 
# list comprehension
x, y = [int(x) for x in input().split()]
print(x)
print(y)

# Reads two numbers from input and typecasts them to int using 
# map function
x, y = map(int, input().split())
print(x)
print(y)
