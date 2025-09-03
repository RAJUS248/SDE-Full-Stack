package com.algorithms365.Datastrctures;

import java.util.ArrayList; // Built-in package

public class MyList {
    private ArrayList<Integer> list = new ArrayList<>();

    // Method to add elements to the list
    public void addElement(int element) {
        list.add(element);
    }

    // Method to print the list
    public void printList() {
        System.out.println("List: " + list);
    }
}
