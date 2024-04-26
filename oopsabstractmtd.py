'''
Python provides the abc module to use the abstraction in the Python program

We use the @abstractmethod decorator to define
an abstract method or if we don't provide the definition to the method,
it automatically becomes the abstract method.

from abc import ABC  
class ClassName(ABC):

'''

from abc import ABC, abstractmethod   
class Car(ABC):   
    def mileage(self):  #abstract method 
        pass
    def bitm_mileage(self):   
        print('non abstract method')
  
class Tesla(Car):   
    def mileage(self):   
        print("abstract method defined in 'tesla' class-The mileage is 30kmph")   

class Suzuki(Car):   
    def mileage(self):   
        print("abstract method defined in 'Suzuki' class-The mileage is 25kmph ")   
 
class Duster(Car):   
     def mileage(self):   
          print("abstract method defined in 'Duster' class-The mileage is 24kmph ")   
  
class Renault(Car):   
    def mileage(self):   
            print("abstract method defined in 'Renault' class-The mileage is 27kmph ")   
             
t= Tesla ()   
t.mileage()   
  
r = Renault()   
r.mileage()   
  
s = Suzuki()   
s.mileage()

d = Duster()   
d.mileage()

c=Car()
c.mileage()




'''

from abc import ABC  
  
class Polygon(ABC):   
  
   # abstract method   
   def sides(self):   
      pass  
  
class Triangle(Polygon):   
  
     
   def sides(self):   
      print("Triangle has 3 sides")   
  
class Pentagon(Polygon):   
  
     
   def sides(self):   
      print("Pentagon has 5 sides")   
  
class Hexagon(Polygon):   
  
   def sides(self):   
      print("Hexagon has 6 sides")   
  
class square(Polygon):   
  
   def sides(self):   
      print("I have 4 sides")   
  
# Driver code   
t = Triangle()   
t.sides()   
  
s = square()   
s.sides()   
  
p = Pentagon()   
p.sides()   
  
k = Hexagon()   
K.sides()

'''
