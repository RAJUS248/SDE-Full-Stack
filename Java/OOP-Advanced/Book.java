// Derived class or Child class 
public class Book extends LibraryItem {
    private int pages;

    public Book(String id, String author, String title, int pages)
    {
        super(id, title, author);
        this.pages = pages;
    }

    @Override 
    public void displayInfo()
    {
        super.displayInfo();
        System.out.println("No of pages: " + this.pages);
    }
    
    public void checkout()
    {
        System.out.println("Checking out the book");
    }
}
