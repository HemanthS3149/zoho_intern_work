#Classes,objects
#Encapsulating methods and variables in classes
#Constructor(init),Inheritance
#Polymorphism(Borrowtransaction and returntransaction override process method inherited from Transaction)
class Book:
    def __init__(self,title,author,isbn,available_copies):
        self.title=title
        self.author=author
        self.isbn=isbn
        self.available_copies=available_copies

    def display_info(self):
        print(f"Title: {self.title}\nAuthor: {self.author}\nISBN: {self.isbn}\nAvailable Copies: {self.available_copies}")

    def borrow(self):
        if self.available_copies>0:
            self.available_copies-=1
            return True
        else:
            print("Sorry this book is not available!")
            return False
        
    def return_book(self):
        self.available_copies+=1
#Book class encapsulates concept of a book with attributes title,author,isbn,available_copies and methods like display_info,borrow,return_book

class Member:
    def __init__(self,name,member_id):
        self.name=name
        self.member_id=member_id

    def display_info(self):
        print(f"Name: {self.name}\nMember ID:{self.member_id}")

class Transaction: #base class
    def __init__(self,transaction_id,book,member,date): # we pass an instance of the book and member class as arguments
        self.transaction_id=transaction_id
        self.book=book
        self.member=member
        self.date=date

    def process(self): #defined but not implemented
        #to be overridden later
        pass

class BorrowTransaction(Transaction):
    def process(self):
        if self.book.borrow():
            print(f"Borrow transaction successful: {self.member.name} borrowed {self.book.title} on {self.date}")
        else:
            print("Borrow transaction failed")

class ReturnTransaction(Transaction):
    def process(self):
        self.book.return_book()
        print(f"Return transaction successful: {self.member.name} returned {self.book.title} on {self.date}")

book1=Book("Agatha Criste","S.Hemanth","9080336770",2)
member1=Member("Amrit","M001")
member2=Member("Arya","M002")
member3=Member("Anant","M003")

print("---Book Information---")
book1.display_info()

print("\n---Member Information ---")
member1.display_info()
member2.display_info()
member3.display_info()

print("---Performing Transactions ---")

print("\nBorrow Operations:")
transaction1=BorrowTransaction("T001",book1,member1,"2024-06-18")
transaction1.process() #Amrit will borrow the book
transaction2=BorrowTransaction("T002",book1,member2,"2024-06-19")
transaction2.process() #Arya will borrow
transaction3=BorrowTransaction("T003",book1,member3,"2024-06-20")
transaction3.process() # anant tries to borrow

print("\nReturn Operations:")
transaction4=ReturnTransaction("T004",book1,member1,"2024-060-25")
transaction4.process() #Amrit returns the book

#Displaying updated book info
print("\n---Updated Book Information ---")
book1.display_info()