"""
* -----------------------------------------------------------------------------
* 
* Copyright <2024> <algorithms365>
* 
* Professional Coding Skills Workshops
* 
* Licensed under the MIT License:
*  
* https://opensource.org/licenses/MIT
* 
* For more information about algorithms365:
* Visit Our Skills Website: https://skills.algorithms365.com/
* Our Company Website: https://algorithms365.com/
*
* For Regular Updates Follow & Subscribe Us on Our Social Media Platforms:
* Instagram: https://www.instagram.com/algorithms365/
* YouTube: https://www.youtube.com/@algorithms365
* Facebook: https://www.facebook.com/algorithms365 
* Twitter(X): https://x.com/algorithms365
* LinkedIn: https://www.linkedin.com/company/algorithms365-technologies-llp/
* 
* Join Our Communities:
* WhatsApp: https://chat.whatsapp.com/K1K7wDMEXG0DJhqMCxFtht
* Telegram: https://t.me/+hyVHXek9WM0zNWQ1
* 
* -----------------------------------------------------------------------------
"""

# This class represent a single node
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class CicularList:

    def __init__(self):
        self.tail = None
    
    # This function insert a node after tail (start)
    # If there is node at start then it becomes the 2nd node
    # Tail node remains the same
    # Time complexity O(1)
    def insert_at_beginning(self, data):
        # Create new node
        new_node = Node(data)

        # Empty list
        if (self.tail == None):
            self.tail = new_node
            new_node.next = new_node
            return

        # Single node / multi node
        new_node.next = self.tail.next
        self.tail.next = new_node

    
    # This function insert node at tail and new node becomes the tail
    # Time complexity O(1)
    def insert_at_tail(self, data):
        new_node = Node(data)

        # Case 1: Empty list
        if (self.tail == None):
            self.tail = new_node
            new_node.next = new_node
            return
        
        # You don't know the address of node before the tail node.
        # Case 2: Single node / multi node
        new_node.next = self.tail.next
        self.tail.next = new_node
        self.tail = new_node

    # Delete the node after tail node
    # Tail remains same
    def delete_at_beginning(self):
        # List empty
        if (self.tail == None):
            print("List is empty")
            return
        
        # Case 1: Single node then list will become empty
        if (self.tail.next == self.tail):
            self.tail = None
            return
        
        # Case 2: Two or more nodes
        self.tail.next = self.tail.next.next 

    # Node before tail becomes the new tail
    # Since we don't have address of node before tail node 
    # we have to traverse to reach there
    def delete_at_tail(self):
        # Case 1: Empty list
        if (self.tail == None):
            return
        
        # Case 2: Single node
        if (self.tail.next == self.tail):
            self.tail = None
            return
        
        # Case 3: 2 or more nodes
        # Find the ref to the node previous to the current tail node
        new_tail = self.tail.next
        while (new_tail.next != self.tail ):
            new_tail = new_tail.next

        new_tail.next   = self.tail.next
        self.tail = new_tail
    
    def print_all_nodes(self):
        # Case 1: List is empty
        if (self.tail == None):
            print("List is empty")
            return

        current_node = self.tail.next
        while (True):
            print(f"  {current_node.data} --> ")

            if (current_node == self.tail):
                break
            
            current_node = current_node.next
        # This is after the while loop


    def search_key(self, key):
        # Case 1: List is empty
        if (self.tail == None):
            print("List is empty")
            return

        current_node = self.tail.next
        while (True):
            if (current_node.data == key):
                print("Key is found in the list")
                return

            if (current_node == self.tail):
                break
            
            current_node = current_node.next
        
        print("Key is not present in the list")

def Cicular_list_tests(clist: CicularList):
    # List is empty and trying to delete a node
    clist.delete_at_beginning()
    clist.delete_at_tail()
    clist.print_all_nodes()
    clist.search_key(40)
    
    # Perform insert and delete single node
    clist.insert_at_beginning(10)
    clist.delete_at_beginning()

    clist.insert_at_tail(30)
    clist.delete_at_tail()

    # Create list with multiple nodes
    clist.insert_at_beginning(10)
    clist.print_all_nodes()
    clist.search_key(40)


    clist.insert_at_beginning(20)
    clist.insert_at_beginning(30)

    clist.insert_at_tail(40)
    clist.print_all_nodes()
    clist.search_key(40)
    clist.search_key(100)

def demo_infinite_loop(clist: CicularList):
    clist.insert_at_beginning(10)
    clist.insert_at_beginning(20)
    clist.insert_at_beginning(30)
    clist.insert_at_beginning(40)

    clist.search_key(100)



if __name__ == "__main__":
    clist = CicularList()
    #Cicular_list_tests(clist)

    demo_infinite_loop(clist)



    

