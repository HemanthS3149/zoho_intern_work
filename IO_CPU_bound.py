#IO Bound processes involve waiting for io ops to complete
#reading/writing onto files, interacting with db
'''
import multiprocessing
import requests
import time

def io_bound_task(url):
    response=requests.get(url)
    return len(response.content)
if __name__=="__main__":
    urls=[
        "https://www.wikipedia.com",
        "https://www.python.org",
        "https://www.openai.com"
    ]

    #creating a pool of worker processes
    pool=multiprocessing.Pool()
    start_time=time.time()
    #execute tasks asynchronously using the pool of processes
    results=pool.map(io_bound_task,urls)
    total_time=time.time()-start_time
    print(f"Results: {results}")
    print(f"Total time taken: {total_time:.2f} seconds")
    
    pool.close()
    pool.join()
'''
import multiprocessing
import time

def cpu_bound_task(x):
    result=0
    for _ in range(x):
        result+=sum(i*i for i in range(x)) #Heavy computation
    return result

if __name__=="__main__":
    num_cores=multiprocessing.cpu_count()
    print(f"This machine has {num_cores} CPU cores.")

    pool=multiprocessing.Pool(processes=num_cores) #created a pool of worker processes

    tasks=[100000,100000,1000000,1000000] #tasks with heave computation
    start_time=time.time()
    result=pool.map(cpu_bound_task,tasks)
    total_time=time.time()-start_time

    print(f"Results: {result}")
    print(f"Total time taken: {total_time:.2f} seconds")

    pool.close()#closed the pool of processes
    pool.join()