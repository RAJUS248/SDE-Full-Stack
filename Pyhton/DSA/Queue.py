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
        self.next = None

class Queue:

    def __init__(self):
        self.rear = None
        self.front = None
        self.count = 0

    def enqueue(self, data):
        # Inserts from the rear 
        print(f"Inserting value {data} into the queue")
        new_node = Node(1)

        # Case 1: Queue is empty
        if (self.rear == None):
            self.front = new_node
        else:
            # Case 2: Queue has some nodes
            # Current read node 
            new_node.next = self.rear
            
        
        self.rear = new_node
        self.count += 1

    def dequeue(self) -> int:
        if (self.front == None):
             print("Queue is empty")
             return -100
        
        # Take copy of the value
        # Move to the next node
        return_data = self.front.data
        self.front = self.front.next

        # If there was only one element, queu became empty
        # In such case front also has to be pointed to None
        if (self.front == None):
            self.rear = None
        
        self.count -= 1
        print(f"Removing element {return_data} from the queue")
        return return_data
    
    def peek(self) -> int:
        if (self.front == None):
            print("Queue is empty")
            return -100
        
        return self.front.data
    
    def get_count(self) -> int:
        return self.count
    
    def print_all_elements(self):
        if (self.front == None):
            print("Queue is empty")
            return
        
        current_node = self.front
        print("Element in the queue")
        while (current_node != None):
            print(f" {current_node.data } -->")
            current_node = current_node.next

if __name__ == "__main__":
    print("queue implementation")
    my_queue = Queue()

    my_queue.dequeue()
    my_queue.print_all_elements()
    my_queue.get_count()

    my_queue.enqueue(1)
    my_queue.print_all_elements()
    my_queue.get_count()
    my_queue.dequeue()
    my_queue.print_all_elements()

    my_queue.enqueue(1)
    my_queue.enqueue(2)
    my_queue.enqueue(3)
    my_queue.enqueue(4)
    value = my_queue.dequeue()
    print(f"We got value {value} from the queue")


