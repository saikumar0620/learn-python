# this is the example of with class 
from threading import Thread
from time import sleep
class Hello(Thread):
  def run(self):
    for i in range(5):
      print("hello",i+1)
      sleep(0.3)
class Hi(Thread):
  def run(self):
    for i in range(5):
      print("Hi",i+1)
      sleep(0.3)

      
t1=Hello()
sleep(0.2)
t2=Hi()

t1.start()
t2.start()