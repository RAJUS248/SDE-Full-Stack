package Recursion;

public class Recursion {

    public static void printNumbersRecursive(int number)
    {
        // Termination block

        if (number == 0)
            return;

        // Work or logic block
        number = number -1;
        System.out.println("Before recursive call: " + number);

        // Recursive call
        printNumbersRecursive(number);
        
        System.out.println("After the recursive call " + number);
    }
    
    public static int fibonnacci(int number)
    {
        System.out.println("Recursive function invoked with number = " + number);
        if (number <= 1)
            return number;

        System.out.print("FIRST recursive call getting invoked");
            int result1 =  fibonnacci(number-1);
        System.out.println("Result 1 value  = " + result1);

        
        System.out.print("SECOND recursive call getting invoked");
        int result2 = fibonnacci(number-2);
        System.out.println("Result 2 value  = " + result2);

        int answer = result1 + result2;
        System.out.println("Answer value  = " + answer);

        return answer;
    }
     
    public static void main(String[] args) {
        //printNumbersRecursive(5);
        int result = fibonnacci(5);
        System.out.println("Result is " + result);

    }
}
