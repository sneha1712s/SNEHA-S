'''
states = {"Goa", "MP", "UP", "Tamilnadu", "Karnataka", "Mumbai", "Kashmir"}    
print(states)    
print(type(states))    
print("looping through the set elements ... ")    
for i in states:    
    print(i)
    
states = set(["Goa", "MP", "UP", "Tamilnadu", "Karnataka", "Mumbai", "Kashmir"])    
print(states)    
print(type(states))    
print("looping through the set elements ... ")    
for i in states:    
    print(i)
    
# Empty curly braces will create dictionary  
set3 = {}  
print(type(set3))  
  
# Empty set using set() function  
set4 = set()  
print(type(set4))

set5 = {10,20,40,40,50,80,90,90,100}
print(set5)

districts = set(["Ooty","Banglore", "Manglore", "Ballari", "Udupi", "Chennai"])    
print("\nprinting the original set ... ")    
print(districts)    
print("\nAdding other districts to the set...");    
districts.add("Kovai");    
districts.add ("Kanyakumari");    
print("\nPrinting the modified set...");    
print(districts)    
print("\nlooping through the set elements ... ")    
for i in districts:    
    print(i)   
print("Return set with unique elements:",set5)


districts = set(["Ooty","Banglore", "Manglore", "Ballari", "Udupi", "Chennai"])    
print("\nprinting the original set ... ")    
print(districts)    
print("\nupdating the original set ... ")    
districts.update(["Kovai","Kanyakumari","Madurai","Trichy"]);    
print("\nprinting the modified set ... ")     
print(districts);


districts = set(["Ooty","Banglore", "Manglore", "Ballari", "Udupi", "Chennai"])
print("\nprinting the original set ... ")    
print(districts)    
print("\nRemoving some months from the set...");    
districts.discard("Ooty");    
districts.discard("Banglore");    
print("\nPrinting the modified set...");    
print(districts)    
print("\nlooping through the set elements ... ")    
for i in districts:    
    print(i)
   
districts = set(["Ooty","Banglore", "Manglore", "Ballari", "Udupi", "Chennai"])    
print("\nprinting the original set ... ")    
print(districts)    
print("\nRemoving some months from the set...");    
districts.remove("Banglore");    
districts.discard("Vijayawada");    
print("\nPrinting the modified set...");    
print(districts)

districts = set(["Ooty","Banglore", "Manglore", "Ballari", "Udupi", "Chennai"])        
print("\nprinting the original set ... ")    
print(districts)    
print("\nRemoving some months from the set...");    
districts.pop();    
districts.pop();    
print("\nPrinting the modified set...");    Banglore', 'Ooty', 'Manglore', 'Udupi', 'Ballari', 'Chennai
print(districts)

districts = set(["Ooty","Banglore", "Manglore", "Ballari", "Udupi", "Chennai"])
print("\nprinting the original set ... ")    
print(districts)    Banglore', 'Ooty', 'Manglore', 'Udupi', 'Ballari', 'Chennai
print("\nRemoving all the items from the set...");    
districts.clear()    
print("\nPrinting the modified set...")    
print(districts)

districts = set(["Ooty","Banglore", "Manglore", "Ballari", "Udupi", "Chennai"])    
print("\nprinting the original set ... ")    
print(districts)    
print("\nRemoving items through discard() method...");    
districts.discard("Kadappa"); #will not give an error although the key feb is not available in the set    
print("\nprinting the modified set...")    
print(districts)    
print("\nRemoving items through remove() method...");    
districts.remove("Kadappa") #will give an error as the key jan is not available in the set.     
print("\nPrinting the modified set...")    
print(districts)

Days1 = {"Monday","Tuesday","Wednesday","Thursday", "Sunday"}    
Days2 = {"Friday","Saturday","Sunday"}    
print(Days1|Days2) #printing the union of the sets

Days1 = {"Monday","Tuesday","Wednesday","Thursday"}    
Days2 = {"Friday","Saturday","Sunday"}    
print(Days1.union(Days2)) #printing the union of the sets

# Create three sets  
set1 = {1, 2, 3}  
set2 = {2, 3, 4}  
set3 = {3, 4, 5}  
  
# Find the common elements between the three sets  
common_elements = set1.union(set2, set3)  
  
# Print the common elements  
print(common_elements)

Days1 = {"Monday","Tuesday", "Wednesday", "Thursday"}    
Days2 = {"Monday","Tuesday","Sunday", "Friday"}    
print(Days1&Days2) #prints the intersection of the two sets

set1 = {"Devansh","John", "David", "Martin"}    
set2 = {"Steve", "Milan", "David", "Martin"}    
print(set1.intersection(set2)) #prints the intersection of the two sets

set1 = {1,2,3,4,5,6,7}  
set2 = {1,2,20,32,5,9}  
set3 = set1.intersection(set2)  
print(set3)

# Create three sets  
set1 = {1, 2, 3}  
set2 = {2, 3, 4}  
set3 = {3, 4, 5}  
  
# Find the common elements between the three sets  
common_elements = set1.intersection(set2, set3)  
  
# Print the common elements  
print(common_elements)

Days1 = {"Monday",  "Tuesday", "Wednesday", "Thursday"}    
Days2 = {"Monday", "Tuesday", "Sunday"}    
print(Days2-Days1) #{"Wednesday", "Thursday" will be printed}

Days1 = {"Monday",  "Tuesday", "Wednesday", "Thursday"}    
Days2 = {"Monday", "Tuesday", "Sunday"}    
print(Days1.difference(Days2)) # prints the difference of the two sets Days1 and Days2

a = {1,2,3,4,5,6}  
b = {1,2,9,8,10}  
c = a^b  
print(c)

a = {1,2,3,4,5,6}  
b = {1,2,9,8,10}  
c = a.symmetric_difference(b)  
print(c)
'''
Days1 = {"Monday",  "Tuesday", "Wednesday", "Thursday"}    
Days2 = {"Monday", "Tuesday","Wednesday"}    
Days3 = {"Monday", "Tuesday", "Friday"}    
    
#Days1 is the superset of Days2 hence it will print true.     
print (Days1>Days2)     
    
#prints false since Days1 is not the subset of Days2     
print (Days1<Days2)
#prints false since Days2 and Days3 are not equivalent     
print (Days2 == Days3)    




