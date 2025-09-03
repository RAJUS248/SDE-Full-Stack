public class Application {
    public static void main(String[] args)
    {
        // Parent class object 
      //  LibraryItem item1 = new LibraryItem("123", "PCS", "Mahesh");
      //  item1.displayInfo();
      //  System.out.println("------------------");

      // - Try this when you are leanring about abstract class and interfaces.
      // Why we can't assign the object of one child class to the variable of type another child class
      // Book bookalpha;
      // bookalpha = new Magazine(); 
      
      // Child class object 
        Book book1 = new Book("124", "Mahesh", "DSA", 250);
        book1.displayInfo();
        book1.checkout();
        System.out.println("------------------");

        // Child class object
        Magazine magazine1 = new Magazine("234", "Tech today", "Ram", 100);
        magazine1.displayInfo();
        System.out.println("------------------");

        Ebook ebook1 = new Ebook("111", "PCS by Mahesh", "Mahesh", 250, "Pdf");
        ebook1.displayInfo();
        System.out.println("File format : " + ebook1.getFileFormat());

        ebook1.Search("PCS");
        ebook1.Search("Mahesh", "123");
    }
}
