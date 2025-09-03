public class SinglyLinkedList {
    
    Node head;

    public SinglyLinkedList()
    {
        this.head = null;
        System.out.println(("Singly linked list objected created"));
    }

    // It does not matter whether there are any nodes or not
    // We can set next to current head 
    // Make the new new as current head 
    public void InsertAtBeginning(int data)
    {
        Node newNode = new Node(data);
        newNode.next = this.head;
        this.head = newNode;
    }

    public void PrintAllNodesData()
    {
        if (this.head == null)
        {
            System.out.println("List is empty!");
            return;
        }

        System.out.println("Nodes in the list..");
        Node currentNode = this.head;
        while (currentNode != null)
        {
            System.out.print(" " + currentNode.data + " --> ");
            currentNode = currentNode.next;
        }

        System.out.print(" null ");
    }

    public void InsertAtEnd(int data)
    {
        Node newNode = new Node(data);

        if (this.head == null)
        {
            this.head = newNode;
            System.out.println("List was empty, made the new node as head");
            return;
        }

        Node currentNode = this.head;
        while (currentNode.next != null)
        {
            currentNode = currentNode.next;
        }
        
        currentNode.next = newNode;
        System.out.println("Inserted a node a the end  " + newNode.data);
    }

    public void deleteAtBeginning()
    {
        // list empty
        if (this.head == null)
        {
            System.out.println("Invalid operation, list is empty");
            return;
        }

        // List has only one or more nodes 
        this.head = this.head.next;
        System.err.println("Deleted a node from the list");
    }

    public void deleteAtEnd()
    {
        // list empty
        if (this.head == null)
        {
            System.out.println("Invalid operation, list is empty");
            return;
        }

        // List has one node , when you delete that node, list becomes empty
        if (this.head.next == null)
        {
            this.head = null;
            return;
        }

        // Two or more nodes
        Node currentNode = this.head;

       // while(currentNode != null) // wrong  - we will reach end of the list till null
       // while(currentNode.next != null) // wrong we will reach the last node which we need to delete

        while (currentNode.next.next != null) // we will reach one node before the last node
        {
            currentNode = currentNode.next;
        }

        // Delete operation 
        currentNode.next = null;
    }

    public void search(int key)
    {
        if (this.head == null)
        {
            System.out.println("List is empty!");
            return;
        }

        Node currentNode = this.head;
        while (currentNode != null)
        {
            if (currentNode.data == key)
            {
                System.err.println("Key is found in the list");
                return;
            }
            currentNode = currentNode.next;
        }
        System.out.println("Key is NOT found in the list!");
    }

    public int countKey(int key)
    {
        int count = 0;
        if (this.head == null)
        {
            return count;
        }

        Node currentNode = this.head;
        while (currentNode != null)
        {
            if (currentNode.data == key)
            {
                count++;                
            }
            currentNode = currentNode.next;
        }
        
        return count;
    }

    public void insertAtGivenPosition(int data, int targetPosition)
    {
        if (targetPosition <= 0)
        {
            System.err.println("Invalid position " + targetPosition);
            return;
        }

        if (targetPosition == 1)
        {
            this.InsertAtBeginning(data);
            return;
        }

        Node currentNode = this.head;
        int currentPosition = 1;

        while (currentPosition < targetPosition -1)
        {
            if (currentNode == null)
            {
                break;
            }

            currentNode = currentNode.next;
            currentPosition = currentPosition + 1;
        }
        
        if (currentNode == null)
        {
            System.out.println("Invalid position");
            return;
        }

        Node newNode = new Node(data);
        newNode.next = currentNode.next;
        currentNode.next = newNode;
    }

    public void deleteAtGivenPosition(int deletePosition)
    {
        if (this.head == null)
        {
            System.out.println("List is empty");
            return;
        }

        if (deletePosition <= 0)
        {
            System.out.println("Invalid delete position " + deletePosition);
            return;
        }

        if (deletePosition == 1 && this.head.next == null)
        {
            // There is only one node and we are trying to delete the same
            this.head = null;
            return;
        }

        int currentPosition = 1;
        Node currentNode = this.head;

        while (currentPosition < deletePosition-1)
        {
            currentNode = currentNode.next;
            currentPosition += 1;

            if (currentNode == null) // This happens only on invalid input of delete position
                break;
        }

        if (currentNode == null)
        {
            System.out.println("Invalid target position for deleting, there are less number of nodes");
            return;
        }

        currentNode.next = currentNode.next.next;
    }

    public void testDeleteAtPosition()
    {
        //  Empty list 
        this.deleteAtGivenPosition(0);
        this.deleteAtGivenPosition(-1);

        this.InsertAtBeginning(1);
        this.deleteAtGivenPosition(10);

        this.deleteAtGivenPosition(1);

        this.InsertAtBeginning(4);
        this.InsertAtBeginning(3);
        this.InsertAtBeginning(2);
        this.InsertAtBeginning(1);

        this.deleteAtGivenPosition(3);
        this.deleteAtGivenPosition(3);
    }

    public void testInsertAtPosition()
    {
        // Empty list but position values are invalid 
        this.insertAtGivenPosition(1, -1);
        this.insertAtGivenPosition(1, 0);

        // List has one node, we are performing insert at start
        this.InsertAtBeginning(1);
        this.insertAtGivenPosition(2, 1);
        
        this.insertAtGivenPosition(3, 3);
        this.insertAtGivenPosition(10, 10);

        this.insertAtGivenPosition(5, 1);
    }


    public void testAllOperations()
    {
        this.deleteAtBeginning();
        this.deleteAtEnd();

        this.InsertAtBeginning(1);
        this.deleteAtBeginning();

        this.InsertAtBeginning(1);
        this.deleteAtEnd();
        
        this.InsertAtBeginning(1);
        this.InsertAtBeginning(2);
        this.InsertAtBeginning(3);

        this.PrintAllNodesData();

        this.InsertAtEnd(4);
        this.InsertAtEnd(5);

        this.PrintAllNodesData();

        this.deleteAtBeginning();
        this.PrintAllNodesData();

        this.deleteAtEnd();
        this.PrintAllNodesData();

        this.search(100);
        this.search(4);
    }
}
