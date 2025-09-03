public class Stack {
    
    Node top;
    int count;

    public Stack()
    {
        this.top = null;
        this.count = 0;
    }

    public void Push(int data)
    {
        Node newNode = new Node(data);
        this.count++;

        // Stack is empty
        if (this.top == null)
        {
            this.top = newNode;
            return;
        }

        // Stack has some elements
        newNode.next = this.top;
        this.top = newNode;
    }

    public int Pop()
    {
        // Stack is empty
        if (this.top == null)
        {
            System.out.println("Stack is empty");
            return -1;
        }

        int value = this.top.data;
        this.top = this.top.next;
        this.count--;
        return value;
    }

    public int GetCount()
    {
        return this.count;
    }

    public int Peek()
    {
        if (this.top == null) // empty
        {
            return -1;
        }
        else 
        {
            return this.top.data;
        }
    }

    public void PrintAll()
    {
        if (this.top == null)
        {
            System.err.println("Stack is empty");
            return;
        }

        Node currentNode = this.top;
        while (currentNode != null)
        {
            System.out.println(currentNode.data);
            currentNode = currentNode.next;
        }
    }

    public void testStack()
    {
        this.Pop();
        this.PrintAll();
        this.Peek();
        System.out.println("Number of elements in the stack = " + this.GetCount());

        this.Push(10);
        this.Push(20);
        this.Push(30);

        this.PrintAll();
        this.Peek();
        System.out.println("Number of elements in the stack = " + this.GetCount());

        this.Pop();
        this.Pop();
        this.Pop();
        this.Pop();

        
    }
}
