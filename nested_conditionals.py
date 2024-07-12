def complex_condition(x,y):
    if x>10:
        if y>5:
            return "x is greater than 10 and y is greater than 5"
        elif y<5:
            return "x is greater than 10 and y is lesser than 5"
        else:
            return "x is greater than 10 and y is equal to 5"
    
    else:
        if y==5:
            return "x may be 10 or less and y is 5"
        else:
            return "x is 10 or less and y is not 5"
        

print(complex_condition(15,10))
print(complex_condition(5,5))