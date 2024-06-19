import multiprocessing
import time

def producer(queue):
    for i in range(5):
        item=f"item_{i}"
        print(f"Producer: Putting {item} in queue")
        queue.put(item)
        time.sleep(1)

def consumer(queue):
    while True:
        item=queue.get()
        if item is None:
            break
        print(f"Consumer: Got {item} from queue")
        time.sleep(2)

if __name__=='__main__':
    queue=multiprocessing.Queue() #create a queue for message passing

    producer_process=multiprocessing.Process(target=producer,args=(queue,))
    consumer_process=multiprocessing.Process(target=consumer,args=(queue,))

    producer_process.start()
    consumer_process.start()

    producer_process.join()#wait for producer process to finish

    queue.put(None) #No more items to add
    consumer_process.join()

    print("Main process complete")