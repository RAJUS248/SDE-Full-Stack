package com.algorithms365.App;

// Import everything from DataStrctures folder 
import com.algorithms365.Datastrctures.*;

//import com.algorithms365.Datastrctures.MyList;

public class App {
    public static void main(String[] args)
    {
        MyList obj = new MyList();
        obj.addElement(1);
        obj.addElement(2);

        obj.printList();
    }
}
