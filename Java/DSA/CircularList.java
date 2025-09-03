import javax.swing.plaf.TreeUI;

public class CircularList {

    Node tail;

    public CircularList()
    {
        this.tail = null;
    }

    public void InsertAtTail(int data)
    {
        Node newNode = new Node(data);
        
        // List is empty
        if (this.tail == null)
        {
            newNode.next = newNode;
            this.tail = newNode;
            return;
        }

        // List has one or more elements 
        newNode.next = this.tail.next;
        this.tail.next = newNode;
        this.tail = newNode;
    }

   public void InsertAtStart(int data)
   {
        Node newNode = new Node(data);

        // Empty list 
        if (this.tail == null)
        {
            newNode.next = newNode;
            this.tail = newNode;
            return;
        }

        // List has one or more nodes
        newNode.next = tail.next;
        tail.next = newNode;
   }

   public void PrintList()
   {
        // Empty list
        if (this.tail == null)
        {
            System.out.println("List is empty!");
            return;
        }
        
        // List has one or more nodes
        Node currentNode = this.tail.next;
        System.out.println("  Nodes in the list are ... \n");
        while (true)
        {
            System.out.print("  " + currentNode.data + " --> ");
            currentNode = currentNode.next;

            if (currentNode == tail)
            {
                System.out.print("  " + currentNode.data + " --> ");
                break;
            }
        }
   }

   public void Search(int key)
   {
        boolean isKeyFound = false;

        // Empty list
        if (this.tail == null)
        {
            System.out.println("List is empty!");
            return;
        }
        
        // List has one or more nodes
        Node currentNode = this.tail.next;
        while (true)
        {
            if (key == currentNode.data)
            {
                isKeyFound = true;
                break; // Stop searching when the key is found
            }

            currentNode = currentNode.next;
            if (currentNode == tail)
            {
                if (currentNode.data == key)
                {
                    isKeyFound = true;
                }
                break; // Terminating the loop
            }
        }

        if (isKeyFound)  // if (isKeyFound == true)
        {
            System.out.println("Key is found");
        }
        else 
        {
            System.out.println("Key is not found");
        }
   }

   public void deleteAtTail()
   {
        //List is empty
        if (this.tail == null)
        {
            System.out.println("List is empty");
            return;
        }

        // If there is only one node 
        if (this.tail.next == this.tail)
        {
            this.tail = null;
            return;
        }

        // If there are two or more nodes
        Node newTail = this.tail.next; 
        while (newTail.next != this.tail)
        {
            newTail = newTail.next;
        }

        newTail.next = this.tail.next;
        this.tail = newTail;
   }

   public void deleteAtHead()
   {
         //List is empty
         if (this.tail == null)
         {
             System.out.println("List is empty");
             return;
         }
 
         // If there is only one node 
         if (this.tail.next == this.tail)
         {
             this.tail = null;
             return;
         }

         // Two or more nodes
         tail.next = tail.next.next;
   }

   public  void testCicularList()
   {
        //this.PrintList();

        this.InsertAtStart(1);
        this.InsertAtStart(4);
        this.InsertAtStart(10);
        //this.PrintList();

        this.InsertAtTail(2);
        this.PrintList();

        this.Search(100);
        this.Search(4);

        this.deleteAtHead();
        this.PrintList();
        this.deleteAtTail();
        this.PrintList();
        

   }
}
