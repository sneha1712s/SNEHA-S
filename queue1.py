class Queue:
 
  def __init__(self):
      self.queue = list()
 
  def addToQueue(self,value):
# Insert method to add element
      if value not in self.queue:
          self.queue.insert(0,value)
          return True
      return False
 
  def size(self):
      return len(self.queue)
 
MySuperHero = Queue()
MySuperHero.addToQueue("Thor")
MySuperHero.addToQueue("Iron man")
MySuperHero.addToQueue("Hulk")
MySuperHero.addToQueue("Doctor Strange")
MySuperHero.addToQueue("Vision")
print(MySuperHero.size())
 
 
#---------------------------------


class Queue:
  def __init__(self):
      self.queue = list()
 
  def addToQueue(self,value):
# Insert method to add element
      if value not in self.queue:
          self.queue.insert(0,value)
          return True
      return False
# Pop method to remove element
  def removefromQueue(self):
      if len(self.queue)>0:
          return self.queue.pop()
      return ("No elements in Queue!")
 
MySuperHero = Queue()
MySuperHero.addToQueue("Thor")
MySuperHero.addToQueue("Iron man")
MySuperHero.addToQueue("Hulk")
MySuperHero.addToQueue("Doctor Strange")
MySuperHero.addToQueue("Vision")
print(MySuperHero.removefromQueue())
print(MySuperHero.removefromQueue())
 
 
#----------------------


import collections
 
# Create a deque
DoubleEnded = collections.deque(["Harry","Hermione","Ron"])
print (DoubleEnded)
 
# Append to the right
print("Adding to the right: ")
DoubleEnded.append("Ginny")
print (DoubleEnded)
 
# append to the left
print("Adding to the left: ")
DoubleEnded.appendleft("Fred")
print (DoubleEnded)
 
# Remove from the right
print("Removing from the right: ")
DoubleEnded.pop()
print (DoubleEnded)
 
# Remove from the left
print("Removing from the left: ")
DoubleEnded.popleft()
print (DoubleEnded)
 
# Reverse the dequeue
print("Reversing the deque: ")
DoubleEnded.reverse()
print (DoubleEnded)

#------------------------


import Queue as queue
 
#priority Queue
 
pq = queue.PriorityQueue()
 
pq.put((10,"Harry"))
pq.put((1,"Ron"))
pq.put((2,"Hermione"))
 
while not pq.empty():
        print(pq.get()[1])
        
        
#----------------------