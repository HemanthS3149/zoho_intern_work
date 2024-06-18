#Forking is used by OS to create new processes which are essential for implementing multiprocessing
#Multiprocessing builds on forking to provide a higher level approach to parallelism 
#Both aim to acheive concurrent execution

#Forking refers to the process of creating new processes(child process) that is a copy of current process/parent process
#It is used for parallelism and multitasking

#REAL LIFE USES OF FORKING
#Web servers like Apache use forking to handle multiple client requests concurrently
#This allows the server to serve multiple clients simultaneously without blockin

#In scientific computing forking is used to distribite computational tasks across multiple processes

#Job Scheduling systems: tasks often use forking to execute each job in a seperate process=> maximum system utilization

'''
#FOR UNIX LIKE SYSTEMS
import os

def child_process():
    print(f"Child process: PID= {os.getpid()}, Parent PID={os.getppid()}")
    print("Hello from child process!")

def parent_process():
    print(f"Parent process: PID={os.getpid()}")
    print("Hello from parent process!")

    #fork a child process
    pid=os.fork()
    if pid==0:
        child_process()
    else:
        print(f"Parent process continued, child PID= {pid}")

#Entry point of the program
if __name__=="__main__":
    parent_process()
    '''
#os.fork() is not available in windows, so we use multiprocessing module

#Modified code
#FOR WINDOWS
'''
import multiprocessing
import os

def child_process():
    print(f"Child process: PID={os.getpid()},Parent PID={os.getppid()}")
    print("Hello from child process!")

def parent_process():
    print(f"Parent process: PID={os.getpid()}")
    print("Hello from the parent process!")

if __name__=='__main__':
    p=multiprocessing.Process(target=child_process) #os.fork() replaced by multiprocessing.Process
    p.start() #start the child process

    try:
        p.join() #wait for this process to complete
        print(f"Parent process continued,child PID={p.pid}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__=="__main__":
    parent_process()
'''

'''
Process ID(PID): in a multiprocessing environment, each process
or thread running on the OS is identified by a unique PID.
Its a numerical identifier assigned to each process when its cread3
'''

#Another example
# PID helps to identify and distinguis between different processes when dealing with multiprocessing
import multiprocessing
import os
import time

def child_process(task_id):
    print(f"Child process {task_id}: PID={os.getpid()},parent PID={os.getppid()}")
    print(f"Task {task_id} started.")
    time.sleep(2)
    print(f"Task {task_id} completed.")

def parent_process(num_processes):
    print(f"Parent process: PID={os.getpid()}")
    print("Starting child process...")

    #create multiple multiprocessing processes
    processes=[]
    for i in range(num_processes):
        p=multiprocessing.Process(target=child_process,args=(i,))
        processes.append(p)
        p.start() #start each child process

    #wait for all child processes to complete
    for p in processes:
        p.join()

    print('All child processes have completed.')

if __name__=='__main__':
    num_processes=3
    parent_process(num_processes)

#The parent process starts and prints its PID
#It creates child processes.Each child process prints its own PID and PID of parent process
#This info helps verify that each child process has been correctly created and is linked to the correct parent process


#INFERENCE: 
#ALL CHILD PROCESSES HAVE THE SAME PPID AND GET STARTED IN A FOR LOOP AND COMPLETE
#EACH CHILD PROCESS HAS DIFFERENT PID, AND GETS COMPLETED randomly
