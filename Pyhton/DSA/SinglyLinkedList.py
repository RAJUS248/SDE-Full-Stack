"""
-----------------------------------------------------------------------------
Copyright <2024> <algorithms365>

Professional Coding Skills Workshops

Licensed under the MIT License:
https://opensource.org/licenses/MIT

For more information about algorithms365:
Visit Our Skills Website: https://skills.algorithms365.com/
Our Company Website: https://algorithms365.com/

For Regular Updates Follow & Subscribe Us on Our Social Media Platforms:
Instagram: https://www.instagram.com/algorithms365/
YouTube: https://www.youtube.com/@algorithms365
Facebook: https://www.facebook.com/algorithms365
Twitter(X): https://x.com/algorithms365
LinkedIn: https://www.linkedin.com/company/algorithms365-technologies-llp/

Join Our Communities:
WhatsApp: https://chat.whatsapp.com/K1K7wDMEXG0DJhqMCxFtht
Telegram: https://t.me/+hyVHXek9WM0zNWQ1
-----------------------------------------------------------------------------
"""

# Class which represent the node in a singly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Class implements all the operations for singly linked list
class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    # This function add the node at the beginning
    # This needs to handle two scenarios/cases
    # 1) When list is empty
    # 2) List has some elements
    def insert_at_beginning(self, data):
        # Create a new node
        new_node = Node(data)

        # Case 1: If the list is empty, make the new node as head
        if (self.head == None):
            self.head = new_node
            return
        
        # Case 2: If the list is not empty, make the new node as head and point to the old head
        new_node.next = self.head
        self.head = new_node
        return

    # This function adds the node at the end of the linked list
    # It needs to handle two cases
    # 1. When list is empty
    # 2. When list has only one node 
    # 3. When list has more than one node 

    def insert_at_end(self, data):
        # Create an object of type Node
        new_node = Node(data)
        
        # 1 When list is empty
        if (self.head == None):
            self.head = new_node
            return
        
        # 2 When list has only one node 
        if (self.head.next == None):
            self.head.next = new_node
            return
        
        # 3 When there are more than one node loop till the last node
        current_node = self.head
        while (current_node.next != None):
            current_node = current_node.next

        # Set the last node next to the new node
        current_node.next = new_node
        return

    def print_list(self):
        # When list is empty
        if (self.head == None):
            print("List is empty")
            return
        
        current_node = self.head

        #while (current_node.next != None):
        while (current_node != None):
            print (str(current_node.data) + " --> ")
            current_node = current_node.next
    
    def search(self, key):
        # When list is empty
        if (self.head == None):
            print("List is empty")
            return
        
        current_node = self.head

        #while (current_node.next != None):
        while (current_node != None):
            print (str(current_node.data) + " --> ")
            
            if (key == current_node.data):
                print("Given key is present in the list")
                return
            
            current_node = current_node.next
        
        print("Given key is not present in the list")

    def delete_at_beginning(self):
        # List is empty
        if (self.head == None):
            return

        # List has only one node
        if (self.head.next == None):
            self.head = None
            return
        
        # two or more nodes present 
        self.head = self.head.next

    def delete_at_end(self):
        # list is empty
        if (self.head == None):
            return
        
        # List has one node 
        if (self.head.next == None):
            self.head = None
            return

        # We have 2 more more nodes in the list 
        current_node = self.head
        while (current_node.next.next != None):
            current_node = current_node.next

        current_node.next = None

    def insert_at_position(self, data, insert_position):
        # Position is invalid 
        if (insert_position <= 0):
            print("Invalid position")
            return
        
        # Insert at the first position
        if (insert_position == 1):
            self.insert_at_beginning(data)
            return

        # Insert at positions 2 or greater 
        current_node = self.head
        current_position = 1

        while current_position < insert_position-1 and current_node is not None:
            current_position = current_position + 1
            current_node = current_node.next
        
        if (current_node == None):
            print("Invalid position, there are lesser number of nodes")
            return
        
        new_node = Node(data)
        new_node.next = current_node.next #1
        current_node.next = new_node #2
        

    def delete_at_position(self, delete_position):
        # Position is invalid 
        if (delete_position <= 0):
            print("Invalid position")
            return
        
        # Insert at the first position
        if (delete_position == 1):
            self.delete_at_beginning()
            return

        # Insert at positions 2 or greater 
        current_node = self.head
        current_position = 1

        while current_position < delete_position-1 and current_node is not None:
            current_position = current_position + 1
            current_node = current_node.next
        
        if (current_node == None):
            print("Invalid position, there are lesser number of nodes")
            return
        
        current_node.next = current_node.next.next




### This code is outside the class
# Driver code to test the above class

def insert_at_beginning_driver_code(list: SinglyLinkedList):
    list.insert_at_beginning(10)
    list.insert_at_beginning(20)
    list.insert_at_beginning(30)
    

    print("List is created successfully")
    print("Head node data is: ", list.head.data)
    print("Next node data is: ", list.head.next.data)
    print("Next node data is: ", list.head.next.next.data)  

def insert_at_end_driver_code(list: SinglyLinkedList):
    list.insert_at_end(10)
    list.insert_at_end(20)
    list.insert_at_end(30)
    list.insert_at_end(40)

def print_search_list_driver_code(list: SinglyLinkedList):
    list.print_list()

    list.insert_at_end(10)
    list.print_list()

    list.insert_at_end(20)
    list.insert_at_end(30)
    list.print_list()

    list.search(100)
    list.search(20)

def delete_operations_start_end(list: SinglyLinkedList):
    list.delete_at_beginning()
    list.delete_at_end()

    list.insert_at_beginning(10)
    list.delete_at_beginning()

    list.insert_at_beginning(10)
    list.delete_at_end()

    list.insert_at_beginning(10)
    list.insert_at_beginning(20)
    list.insert_at_beginning(30)
    list.delete_at_end()
    list.delete_at_end()

def insert_delete_at_given_position(list: SinglyLinkedList):
    list.insert_at_position(10, -1)
    list.delete_at_position(-1)

    list.insert_at_position(10, 1)
    list.delete_at_position(1)

    list.insert_at_end(10)
    list.insert_at_end(20)
    list.insert_at_end(30)

    list.insert_at_position(15, 2)
    list.insert_at_position(40, 4)
    list.insert_at_position(100, 10)




# This is the main block to invoke the driver methods and test your code

if __name__ == "__main__":
    # Create a new singly linked list
    list = SinglyLinkedList()

   # insert_at_beginning_driver_code(list)

   # insert_at_end_driver_code(list)

   # print_search_list_driver_code(list)

   # delete_operations_start_end(list)

    insert_delete_at_given_position(list)




   
    
  
    


    
        

        




    

