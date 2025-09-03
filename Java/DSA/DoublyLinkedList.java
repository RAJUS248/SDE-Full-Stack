public class DoublyLinkedList {
    Dnode head;

    public DoublyLinkedList()
    {
        this.head = null;
    }

    public void InsertAtBeginning(int data)
    {
        Dnode newNode = new Dnode(data);

        // List is empty
        if (this.head == null)
        {
            this.head = newNode;
            return;
        }

        // There are one or more nodes 
        newNode.next = this.head;
        this.head.prev = newNode;
        this.head = newNode;
    }

    public void InsertAtEnd(int data)
    {
        Dnode newNode = new Dnode(data);

        // List is empty
        if (this.head == null)
        {
            this.head = newNode;
            return;
        }

        // List has one or more nodes
        Dnode lastNode = this.head;
        while(lastNode.next != null)
        {
            lastNode = lastNode.next;
        }
        
        // append the new node to the last node
        lastNode.next = newNode;
        newNode.prev = lastNode;
    }

    public void insertAtPosition(int data, int taregetPosition)
    {
        if (taregetPosition <= 0)
        {
            System.out.println("Invalid position");
            return;
        }

        if (this.head == null && taregetPosition == 1)
        {
            this.InsertAtBeginning(data);
            return;
        }

        Dnode leftNode = this.head;
        int currentPosition = 1;
        while (currentPosition < taregetPosition -1)
        {
            if (leftNode == null)
            {
                System.out.println("Invalid target position, it's more than the number of nodes");
                return;
            }

            leftNode = leftNode.next;
            currentPosition = currentPosition + 1;
        }

        // lefNode is now one step away from the node with position in which we want to 
        // insert a node
        Dnode newNode = new Dnode(data);
        if (leftNode.next == null) 
        {
            // Case when new node is added at the end
            leftNode.next = newNode;
            newNode.prev = leftNode;
        }
        else 
        {
            // Case when new node is added in between
            newNode.next = leftNode.next; // 1
            newNode.prev = leftNode; // 2
            leftNode.next.prev = newNode; // 3
            leftNode.next = newNode; // 4
        }
    }

    public void printAllNodes()
    {
        // List is empty
        if (this.head == null)
        {
            System.out.println("List is empty!");
            return;
        }

        Dnode currentNode = this.head;
        System.out.println("Nodes in the list are !");
        while (currentNode != null)
        {
            System.err.print("  " + currentNode.data + "  <--> ");
            currentNode = currentNode.next;
        }
        System.out.println("\n");

    }

    public void printAllNodesReverseOrder()
    {
        // List is empty
        if (this.head == null)
        {
            System.out.println("List is empty!");
            return;
        }

        Dnode currentNode = this.head;
        System.out.println("Nodes in the list are !");
        while (currentNode.next != null)
        {
            System.out.print("  " + currentNode.data + "  <--> ");
            currentNode = currentNode.next;
        }

        System.out.println("reverse order ");
        while (currentNode != this.head)
        {
            System.out.print("  " + currentNode.data + "  <--> ");
            currentNode = currentNode.prev;
        }


        System.out.println("\n");

    }

    public void search(int key)
    {
       // List is empty
       if (this.head == null)
       {
           System.out.println("List is empty!");
           return;
       }

       Dnode currentNode = this.head;
       System.out.println("Nodes in the list are !");
       while (currentNode != null)
       {
           if (key == currentNode.data)
           {
                // key is found
                System.out.println("Key is found");
                return;
           }

           currentNode = currentNode.next;
       }

       System.out.println("Key is NOT found!");
    }

    public void deleteAtBeginning()
    {
        // List is empty
        if (this.head == null)
        {
            System.out.println("List is empty");
            return;
        }

        // Single node, list become empty
        if (this.head.next == null)
        {
            this.head = null;
            return;
        }

        // Two or more nodes
        this.head = this.head.next;
        this.head.prev = null;
    }

    public void deleteAtEnd()
    {
        // List is empty
        if (this.head == null)
        {
            System.out.println("List is empty");
            return;
        }

        // Single node, list become empty
        if (this.head.next == null)
        {
            this.head = null;
            return;
        }

        // Two or more nodes
        Dnode lastNode = this.head;
       while (lastNode.next.next != null)
       {
            lastNode = lastNode.next;
       }
       lastNode.next = null;
    }

    public void deleteAtPosition(int targetPosition)
    {
        if (targetPosition <=0 )
        {
            System.out.println("Invalid position");
            return;
        }

        if (this.head == null)
        {
            System.out.println("List is empty");
            return;
        }

        if (this.head.next == null && targetPosition == 1)
        {
            this.head = null;
            return;
        }

        int currentPosition = 1;
        Dnode delNode = this.head;

        while (currentPosition < targetPosition -1)
        {
            currentPosition = currentPosition + 1;
            delNode = delNode.next;

            if (delNode == null)
            {
                System.out.println("Invalid posiiton");
                return;
            }
        }

        if (delNode.next == null)
        {
            System.out.println("Can't perform this operation");
            return;
        }

        if (delNode.next.next == null)
        {
            // DelNode becomes the new last node
            delNode.next = null;
            return;
        }

        delNode.next = delNode.next.next;
        delNode.next.prev = delNode;
    }

    public void testInsertOperations()
    {
        this.insertAtPosition(100, -1);
        this.insertAtPosition(4, 1);
        this.InsertAtBeginning(1);
        this.InsertAtEnd(10);
        this.printAllNodes();
        this.insertAtPosition(2, 2);
        this.search(10);
        this.insertAtPosition(50, 100);
    }

    public void testDeleteOperations()
    {
        this.deleteAtBeginning();
        this.deleteAtEnd();
        this.deleteAtPosition(-1);

        this.InsertAtBeginning(1);
        this.deleteAtBeginning();

        this.InsertAtBeginning(1);
        this.deleteAtEnd();

        this.InsertAtBeginning(1);
        this.deleteAtPosition(1);

        this.InsertAtBeginning(3);
        this.InsertAtBeginning(2);
        this.InsertAtBeginning(1);

        this.deleteAtPosition(3);

        this.InsertAtBeginning(10);
        this.InsertAtBeginning(20);
        this.InsertAtBeginning(30);
        this.InsertAtBeginning(40);

        this.deleteAtPosition(4);




    }





    








































    
    
}
