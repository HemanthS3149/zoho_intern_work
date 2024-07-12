'''
from typing import Protocol

class Drivable(Protocol):
    def drive(self)->None:
        ...

class Car:
    def drive(self)->None:
        print("Driving the car")

class Bicycle:
    def drive(self)->None:
        print("Riding the bicycle")

def start_driving(vehicle:Drivable)->None:
    vehicle.drive()

car=Car()
bike=Bicycle()
start_driving(car)
start_driving(bike)
'''

from typing import Protocol
#defining the protocol
class Printable(Protocol):
    def print(self,document:str)->None:
        ...
class Scannable(Protocol):
    def scan(self)->str: #no args
        ...

#Now define classes that implement the protocols
class Printer:
    def print(self,document:str)->None:
        print(f"Printing documnet: {document}")
    
class Scanner:
    def scan(self)->str:
        return "Scanned document content"

class MultiFunctionDevice(Printable,Scannable):
    def print(self,document:str)->None:
        print(f"Multifunction device printing:{document}")

    def scan(self)->str:
        return "Multifunction device scanned content"

#Function to handle prining
def handle_printing(device:Printable,document:str)->None:
    device.print(document)

#function to handle scanning
def handle_scanning(device:Scannable)->None:
    scanned_content=device.scan()
    print(f"Scanned content:{scanned_content}")

#Instance of the devices
printer=Printer()
scanner=Scanner()
mfd=MultiFunctionDevice()

#using the functions for different devices
handle_printing(printer,"Printer Document")
handle_printing(mfd,"MFD Document")
handle_scanning(scanner)
handle_scanning(mfd)