// Parent class 
abstract class LibraryItem  {
    public String Id;
    private String title;
    protected String author;
    
    public LibraryItem(String Id, String title, String author)
    {
        this.Id = Id;
        this.title = title;
        this.author = author;
    }

    public void setTitle(String titleName)
    {
        this.title = titleName;
    }

     // Method to display details
     public void displayInfo() {
        System.out.println("Id: " + this.Id);
        System.out.println("Title: " + this.title);
        System.out.println("Author: " + this.author);
    }

    private void searchItems(String name)
    {
        System.out.println("Searching ");
    }

    protected void searchAllItems(String name)
    {
        System.out.println("Inside protected method - Searching ");
        this.searchItems(name);
    }

    // Declaring an abstract method, all the child classes of this must implement this method.
    abstract public void checkout();

}
