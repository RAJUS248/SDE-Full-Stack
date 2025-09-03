public class Magazine extends LibraryItem{
    private int issueNumber;

    public Magazine(String id, String title, String author, int issueNumber) {
        super(id,title, author);
        this.issueNumber = issueNumber;
    }

    @Override
    public void displayInfo() {
        super.displayInfo();
        System.out.println("Issue Number: " + issueNumber);
    }
    
    public void checkout()
    {
        System.out.println("Checking out the Magazine");
    }
}
