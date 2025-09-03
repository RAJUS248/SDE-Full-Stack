public class Namaste 
{
    public static void main(String[] args)
    {
        enuMadudilla();  // Function invocation
    }

    // Function definition
    static void enuMadudilla()
    {
        String message = "Namaste Bharat!";
        //PrintMessage("Namaste Bharat!");
        PrintMessage(message);
    }

    static String PrintMessage(String message)
    {
        System.out.println(message);
        return message;
    }
}