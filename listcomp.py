numbers = [10, 20, 30, 40, 50]

# list comprehension to create new list
doubled_numbers = [num * 2 for num in numbers]

print(doubled_numbers)












numbers = [10, 20, 30, 40, 50]
square_numbers = []
# for loop to square each elements
for num in numbers:
    square_numbers.append(num * num)
    
print(square_numbers)

# Output: [100, 400, 900, 1600, 2500]

numbers = [10, 20, 30, 40, 50]
# create a new list using list comprehension
square_numbers = [num * num for num in numbers]
print(square_numbers)

# Output: [100, 400, 900, 1600, 2500]


#Conditionals in List Comprehension
#[expression for item in list if condition == True]
# filtering even numbers from a list
even_numbers = [num for num in range(1, 10) if num % 2 == 0 ]

print(even_numbers)

# Output: [2, 4, 6, 8]

word = "Balaji"
vowels = "aeiou"

# find vowel in the string "Balaji"
result = [char for char in word if char in vowels]

print(result)

# Output: ['a','a','i']

