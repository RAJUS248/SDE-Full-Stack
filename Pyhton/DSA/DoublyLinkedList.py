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

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        # Case 1: List is empty
        if (self.head == None):
            self.head = new_node
            return

        # Case 2: List has one or more nodes 
        new_node.next = self.head # 1
        self.head.prev = new_node # 2
        self.head = new_node #3

    def insert_at_end(self, data):
        new_node = Node(data)

        # Case 1: List is empty
        if (self.head == None):
            self.head = new_node
            return

        # Case 2: List has only one node
        if (self.head.next == None):
            self.head.next = new_node
            new_node.prev = self.head
            return
        
        # Case 3: List has more than one node
        # Loop exist to find the ref to the last node
        last_node = self.head
        while (last_node.next != None):
            last_node = last_node.next
        
        last_node.next = new_node
        new_node.prev = last_node

    def print_all_nodes(self):
        print(" \n Printing all the nodes in the doubly linked list \n")
        # Case 1: List is empty
        if (self.head == None):
            print("List is empty")
            return
        
        # Case 2: List has more than one node
        current_node = self.head
        while (current_node != None):
            print(f" <-- {current_node.data} -->", end=" ")
            current_node = current_node.next
        
    
    def search(self, key):
        if (self.head == None):
            print("Key is not found in the list")
            return
        
        # Case 2: List has more than one node
        current_node = self.head
        while (current_node != None):
            if (current_node.data == key):
                print("Key is found in the list")
                return
            
            current_node = current_node.next
        
        # if we reach here, it means key is not found
        print("Key is not found in the list")

    def delete_at_beginning(self):
        # Case 1: List is empty
        if (self.head == None):
            return
        
        # Case 2: Only one node is present
        if (self.head.next == None):
            self.head = None
            return
        
        # Case 3: We have 2 or more nodes
        self.head = self.head.next
        self.head.prev = None

        # You can also write above two lines in this way for simplicity
        """
        new_head = self.head.next 
        new_head.prev = None
        self.head = new_head 
        """

    def delete_at_end(self):
        # Case 1: List is empty
        if (self.head == None):
            return
        
        # Case 2: List has only one node
        if (self.head.next == None):
            self.head = None
            return
        
        # Case 3: 2 more more nodes present in the list
        # Loop till we get last_node to last but one node
        last_node = self.head
        while(last_node.next.next != None):
            last_node = last_node.next
        
        last_node.next = None

    def insert_at_position(self, data, target_position):
        print(f"\nInsert at position {target_position} value {data}")
        
        if (target_position <= 0 ):
            print("Invalid position")
            return
        
        # When list is empty, we can only support insert at position 1
        if (self.head == None and target_position != 1):
            print("Invalid position")
            return
        
        if (target_position == 1):
            self.insert_at_beginning(data)
            return

        # Trying to handle the case when we have only one node and valid operation is 
        # you can insert at 1st or 2nd position
      #  if (self.head.next == None and target_position > 2):
        #    print("Invalid position")
        
        current_position = 1
        current_node = self.head
        while (current_node != None and current_position < target_position-1):
            current_position = current_position + 1
            current_node = current_node.next

        if (current_node == None):
            print("Invalid position")
            return
        
        new_node = Node(data)

        # When we are inserting between two nodes, we need these steps
        if (current_node.next != None):
            current_node.next.prev = new_node #1
            new_node.next = current_node.next #2

        # These are needed for both inserting between and also at the end
        current_node.next = new_node #3
        new_node.prev = current_node #4

    def delete_at_position(self, target_position):
        #1. List is empty
        if (self.head == None):
            print("List is empty")
            return
        
        #2. Position is invalid 
        if (target_position <= 0):
            print(f"Invalid target position {target_position}")
            return

        #3. Single node
        if (self.head.next == None):
            self.head = None
            return

        #4. Multi node
        to_be_deleted = self.head
        current_position = 1

        while (current_position < target_position and to_be_deleted is not None):
            current_position = current_position + 1
            to_be_deleted = to_be_deleted.next
        
        if (to_be_deleted == None):
            print(f"Target position {target_position} is invalid, we have lesser number of nodes")
            return
        
              
        # Case 4.1: to_be_deleted node is the last node
        if (to_be_deleted.next == None):
            to_be_deleted.prev.next = None
            return
        
         # Case 4.2: There are nodes after the to_be_deleted Node
        to_be_deleted.next.prev = to_be_deleted.prev
        to_be_deleted.prev.next = to_be_deleted.next


def delete_at_position_test(dlist: DoublyLinkedList):
    dlist.delete_at_position(-1)
    dlist.delete_at_position(1)
    dlist.insert_at_beginning(10)
    dlist.delete_at_position(-1)
    dlist.delete_at_position(1)

    dlist.insert_at_beginning(40)
    dlist.insert_at_beginning(30)
    dlist.insert_at_beginning(20)
    dlist.insert_at_beginning(10)

    dlist.delete_at_position(4)
    dlist.delete_at_position(2)



    




def insert_at_position_test(dlist: DoublyLinkedList):
    dlist.insert_at_position(10, -1)
    dlist.print_all_nodes()
    dlist.insert_at_position(10, 2)
    dlist.insert_at_position(10, 1)
    dlist.print_all_nodes()
    dlist.insert_at_position(20, 1)
    dlist.print_all_nodes()
    dlist.insert_at_position(30, 2)
    dlist.print_all_nodes()
    dlist.insert_at_position(30, 10)
    dlist.print_all_nodes()
    dlist.insert_at_position(40, 3)
    dlist.print_all_nodes()
    dlist.insert_at_position(50, 3)
    dlist.print_all_nodes()




def delete_tests(dlist: DoublyLinkedList):
    dlist.delete_at_beginning()
    dlist.delete_at_end()

    dlist.insert_at_beginning(10)
    dlist.delete_at_beginning()

    dlist.insert_at_beginning(10)
    dlist.delete_at_end()

    dlist.insert_at_beginning(10)
    dlist.insert_at_beginning(20)
    dlist.insert_at_beginning(30)
    dlist.insert_at_beginning(40)
    dlist.delete_at_end()


def search_test(dlist: DoublyLinkedList):
    dlist.insert_at_beginning(20)
    dlist.insert_at_beginning(30)
    dlist.insert_at_beginning(40)

    dlist.search(100)
    dlist.search(30)

def print_all_nodes_test(dlist: DoublyLinkedList):
    dlist.print_all_nodes()
    dlist.insert_at_beginning(10)
    dlist.print_all_nodes()
    
    dlist.insert_at_beginning(20)
    dlist.insert_at_beginning(30)
    dlist.insert_at_beginning(40)
    dlist.print_all_nodes()


def insert_at_beginning_test(dlist: DoublyLinkedList):
    dlist.insert_at_beginning(10)
    dlist.insert_at_beginning(20)

def insert_at_end_test(dlist: DoublyLinkedList):
    dlist.insert_at_end(10)
    dlist.insert_at_end(20)
    dlist.insert_at_end(30)
    dlist.insert_at_end(40)

if __name__ == "__main__":
    dlist = DoublyLinkedList()

    #insert_at_beginning_test(dlist)
    #insert_at_end_test(dlist)
    #print_all_nodes_test(dlist)

    #search_test(dlist)

    #delete_tests(dlist)

    #insert_at_position_test(dlist)

    delete_at_position_test(dlist)

   

