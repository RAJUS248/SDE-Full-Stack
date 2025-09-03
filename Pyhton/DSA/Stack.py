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

class Stack:

    def __init__(self):
        self.count = 0
        self.top = None

    def push(self, data):
        new_node = Node(data)

        new_node.next = self.top
        self.top = new_node
        self.count = self.count + 1
        print(f"Pushed the value {data} to stack top")

    def pop(self) -> int: 
        # Case 1: Stack is empty
        if (self.top == None):
            print("Stack is empty! can't perform pop operation")
            return -100
        
        data = self.top.data
        self.top = self.top.next
        self.count = self.count - 1
        print(f"Popped the item from stack {data}")
        return data
    
    def peek(self) -> int:
         # Case 1: Stack is empty
        if (self.top == None):
            print("Stack is empty! can't perform pop operation")
            return -100
        
        return self.top.data
    
    def get_count(self) -> int:
        print(f"There are {self.count} items in the stack")
        return self.count
    
    def print_all_values(self):
        if (self.top == None):
            print("Stack is empty")
            return
        
        current_node = self.top
        print("Elements in the stack are as below")
        while( current_node is not None):
            print(f" {current_node.data} ")
            current_node = current_node.next

if __name__ == "__main__":

    stack = Stack()

    stack.pop()
    count_items = stack.get_count()
    stack.print_all_values()

    stack.push(1)
    stack.get_count()
    stack.print_all_values()
    stack.pop()

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.print_all_values()
    stack.pop()
    stack.print_all_values()





