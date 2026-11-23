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
  
  print(f"the parellel excecution taken time is {end - start:.2f}")

  
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
  print(f"the parellel excecution with threads taken time is {end - start:.2f}")
    
    
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from time import time

# Real URLs mapped to local filenames
files_to_download = [
    ("https://jsonplaceholder.typicode.com/posts", "posts.json"),
    ("https://jsonplaceholder.typicode.com/comments", "comments.json"),
    ("https://jsonplaceholder.typicode.com/users", "users.json"),
]

def download(file_info):
    url, save_as = file_info
    print(f"Starting download: {save_as}")
    try:
        # Actually fetches the data from the web and saves it to disk
        urllib.request.urlretrieve(url, save_as)
        print(f"Done: {save_as}")
    except Exception as e:
        print(f"Failed {save_as}: {e}")

if __name__ == "__main__":
    # 1. Sequential Execution (One by one)
    start = time()
    for item in files_to_download:
        download(item)
    end = time()
    print(f"\nSequential time taken: {end - start:.2f} seconds\n")

    # 2. Threaded Execution (Concurrent)
    start = time()
    with ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(download, files_to_download)
    end = time()
    print(f"\nThreaded time taken: {end - start:.2f} seconds")