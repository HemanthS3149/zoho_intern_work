import multiprocessing
import time

def writer(shared_array,lock):
    for i in range(len(shared_array)):
        with lock: #proceeds only when we have access to lock
            shared_array[i]=i*i
            print(f"Writer: shared_array[{i}]={shared_array[i]}")
        time.sleep(1)

def reader(shared_array,lock):
    while True:
        with lock:
            print(f"Reader: shared_array={list(shared_array)}") #printing as a list
        time.sleep(1)

if __name__=="__main__":
    #Creating a lock to synchronize access to shared memory
    lock=multiprocessing.Lock()
    shared_array=multiprocessing.Array('i',5) #5 integer type nos

    #creating processes for write and read
    write_process=multiprocessing.Process(target=writer,args=(shared_array,lock))
    read_process=multiprocessing.Process(target=reader,args=(shared_array,lock))

    write_process.start()
    read_process.start()

    time.sleep(12)#letting the process be for sometime

    write_process.terminate()
    read_process.terminate()

    write_process.join()
    read_process.join()
    print("Main process finished.")