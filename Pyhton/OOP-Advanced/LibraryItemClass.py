# We need this module to create abstract class in Python
from abc import ABC, abstractmethod

# Parent class - Abstract class
class LibraryItem(ABC):
    # Constructor 
    def __init__(self, count, id):
        self.count = count
        self.id = id
    
    def display_info(self):
        print(f"Count: {self.count}")
        print(f"Id: {self.id}")
    
    @abstractmethod
    def check_out(self):
        print("Invoking checkout method in LibraryItem")
        
        