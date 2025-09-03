public class GenericsDemo {
    

    public static <T> void sumOfTwoNumbers(T value1, T value2)
    {
        System.out.println("Value1 = " + value1 + " Value2 = " + value2);
    }

    public static <T> void PrintvalueOnTerminal(T value)
    {
        System.out.println("Value is = " + value);
    }
    
    public static void main(String[] args)
    {
        Box<Integer> intbox = new Box<>();
        intbox.SetValue(10);
        intbox.Printvalue();
        System.out.println("Print using getvalue " + intbox.GetValue());

        Box<String> names = new Box<>();
        names.SetValue("Sangeeta");
        names.Printvalue();

        PrintvalueOnTerminal("Mahesh Arali");
        PrintvalueOnTerminal(10);
        PrintvalueOnTerminal(10.2);

        sumOfTwoNumbers(10, 5.5);

    }
}
