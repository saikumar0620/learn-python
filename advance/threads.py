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

# def hi():
#   for i in range(5):
#     print("hi",i+1)
#     sleep(0.3)
    
# def hlo():
#   for i in range(5):
#     print("hlo",i+1)
#     sleep(0.3)

    
# if __name__== "__main__":
    
#   t1=Thread(target=hi)
#   t2=Thread(target=hlo)
  
#   t1.start()
#   t2.start()
  # t1.join()
  # t2.join()
  # print("excecution complete")
  
  
  # 
def download(file_name):
    print("download start",file_name)
    sleep(0.3)
    print("download done")
if __name__=='__main__':
  
  files=["videos:mp4","audio: mp3","images: jpg"]
  start=time()
  for f in files:
    download(f)
  end=time()
  
  print(f"the parellel excecution taken time is {start-end:.2f}")

  
  Threads=[]
  for f in files:
    t=Thread(target=download,args=(f,))
    Threads.append(t)
    start=time()
  for t in Threads:
    t.start()
  for t in Threads:
    t.join()
  end=time()
  print(f"the parellel excecution with threads taken time is {start - end:.2f}")
    
    
    