public class Application {

    public static void main(String[] args)
    {
        int demo = 5; // creating an integer object and assigning the value 5 , allocated in the stack
        
        // Declared the variable newStudent and create an object of type Student 
        Student newStudent = new Student(); // Heap memory dynamic memory allocation

        // Access the public varirables fo the class and update values 
        newStudent.Name = "Ram";
        newStudent.Age = 50;
        newStudent.Hometown = "Bengaluru";

        // newStudent.ID = 1; You can't access private variable like this, compiler won't allow

        // access or invoke or calling public methods of the class for the object new Student
        System.out.println("Student name is " + newStudent.getName());
        System.out.println("Student name age is  " + newStudent.getAge());

        // newStudent.updateName("Sita"); You can't access private method like this

        // Run time error NullPointerException 
        Student secondStudent = null;
        if (secondStudent != null)
        {
            secondStudent.Name = "Sita";  // Dead code, this will never be executed
        }

        // Creating another student object with constructor taking input
        secondStudent = new Student("Sita", 45, "Science", "Bengaluru");
        System.out.println("Student name is " + secondStudent.getName());
        System.out.println("Student name age is  " + secondStudent.getAge());

        BookManagement operations = new BookManagement();        
        Book book1 = new Book("PCS", 
                                "Mahesh Arali", 
                                "Coding", 
                                "1");

        operations.checkoutBook(secondStudent, book1);
        operations.checkoutBook(newStudent, book1);

        operations.returnBook(newStudent, book1);

    }
}