/*
 * -----------------------------------------------------------------------------
 *
 * Copyright <2024> <algorithms365>
 *
 * Professional Coding Skills Workshops
 *
 * Licensed under the MIT License:
 *
 * https://opensource.org/licenses/MIT
 *
 * For more information about algorithms365:
 * Visit Our Skills Website: https://skills.algorithms365.com/
 * Our Company Website: https://algorithms365.com/
 *
 * For Regular Updates Follow & Subscribe Us on Our Social Media Platforms:
 * Instagram: https://www.instagram.com/algorithms365/
 * YouTube: https://www.youtube.com/@algorithms365
 * Facebook: https://www.facebook.com/algorithms365
 * Twitter(X): https://x.com/algorithms365
 * LinkedIn: https://www.linkedin.com/company/algorithms365-technologies-llp/
 *
 * Join Our Communities:
 * WhatsApp: https://chat.whatsapp.com/K1K7wDMEXG0DJhqMCxFtht
 * Telegram: https://t.me/+hyVHXek9WM0zNWQ1
 *
 * -----------------------------------------------------------------------------
 */
public class Arrays {
    public static void main(String[] args)
    {
        int[] numbers= {1, 9, 2}; // Declare , initialize 
        System.out.println("Number of elements in the array = " + numbers.length);
        numbers[0] = 10;
        System.out.println("Values in the array numbers \n");
        printElements(numbers);

        
        int[] ages = new int[3];
        ages[0] = 50;
        ages[1] = 60;
        ages[2] = 70;
        System.out.println("\n Values in the ages  \n");
        printElements2(ages);

        int[][] matrix = {
            {1,2,3},
            {4,5,6},
        };

        System.out.println("\n Values in the matrix  \n");
        System.out.println(matrix[0][0]);
        System.out.println(matrix[0][1]);
        System.out.println(matrix[0][2]);

        java.util.Arrays.sort(numbers);
        printElements(numbers);
        
    }

    public static void printElements(int[] elements)
    {
        // Generating the sequential array index from 0 to length-1
        for (int index=0; index < elements.length; index++)
        {
            System.out.print(" " + elements[index]);
        }
    }

    public static void printElements2(int[] elements)
    {
        // Generating the sequential array index from 0 to length-1
        for (int element : elements)
        {
            System.out.print(" " + element);
        }
    }

   
}