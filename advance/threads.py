# this is the example of with class 
from threading import Thread
from time import sleep,time
# class Hello(Thread):
#   def run(self):
#     for i in range(5):
#       print("hello",i+1)
#       sleep(0.3)
# class Hi(Thread):
#   def run(self):
#     for i in range(5):
#       print("Hi",i+1)
#       sleep(0.3)

      
# t1=Hello()
# sleep(0.2)
# t2=Hi()

# t1.start()
# t2.start()



# threads with the functions
def hi():
  for i in range(5):
    print("hi",i+1)
    sleep(0.3)
    
def hlo():
  for i in range(5):
    print("hlo",i+1)
    sleep(0.3)

    
if __name__== "__main__":
    
  t1=Thread(target=hi)
  t2=Thread(target=hlo)
  
  t1.start()
  t2.start()
  
  # print("excecution complete")