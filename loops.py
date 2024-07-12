#We use generators here
#generators provide a way to iterate through data without storing it all in memory

def fibonacci(n):
    a,b=0,1
    while a<n:
        yield a
        a,b=b,a+b

for i in fibonacci(1000): #since fibonacci is now a generator, it doesn't calculate all numbers at once, it yields them one by one as needed in the loop
    print(i)

#Benifits of using a generator
#Memory efficiency since code avoids creating a large list of fibo nos at once
#laziness: the generator calculates the fibo nos that are actually needed in the loop
