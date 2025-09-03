public class Ebook extends Book {
    private String fileFormat;

    public Ebook(String id, String title, String author, int pages, String fileFormat)
    {
        super(id, author, title, pages);
        this.fileFormat = fileFormat;
    }

    public String getFileFormat()
    {
        return fileFormat;
    }

    public void Search(String name)
    {
        System.out.println("Searching by name");
    }

    public void Search(String author, String id)
    {
        System.out.println("Searching by autor");
    }


    
}
