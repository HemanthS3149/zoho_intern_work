class CustomList:
    def __init__(self,*values):
        self.values=list(values)

    def __len__(self):
        return len(self.values)
    
    def __getitem__(self,index):
        return self.values[index]
    
    def __setitem__(self,index,value):
        self.values[index]=value
    
    def __delitem__(self,index):
        del self.values[index]

    def __repr__(self):
        return f"CustomList({', '.join(map(str,self.values))})"
    
my_list=CustomList(1,2,3,4,5)
print(my_list)
print(len(my_list))
print(my_list[2])

my_list[2]=30
print