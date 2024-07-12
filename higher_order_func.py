from functools import reduce

def apply_function(func,items):
    return [func(item) for item in items]

#example function to be used with higher order functions
def square(x):
    return x*x

def is_even(x):
    return x%2==0

#Example of using apply_function
numbers=[1,2,3,4,5]
squared_numbers=apply_function(square,numbers)
print("Squared Numbers:",squared_numbers)

#using map to achieve same result as apply_function
squared_numbers_map=list(map(square,numbers)) #map applies a function to all items of input list
print("Squared numbers with map:",squared_numbers_map)

#using filter to get even numbers
even_numbers=list(filter(is_even,numbers))
print("Even Numbers:",even_numbers)

#Using reduce to get product of all nos
product=reduce(lambda x,y:x*y,numbers)
print("Product of Numbers:",product)

#Custom higher ord function: returns a function that adds a constant value to its input
def create_adder(x):
    def adder(y):
        return x+y
    return adder

#Creating an adder func that adds 10
add_10=create_adder(10)
print("Add 10 to 5:",add_10(5))

