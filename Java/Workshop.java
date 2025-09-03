import java.util.Scanner; 

public class Workshop {

    // 1 - Function getSum to get Sum of numbers
    static int getSum(int number1, int number2)
    {
        int sum = number1 + number2;
        return sum;
    }

    static void invoke_getSum()
    {
        int result = getSum(10, 20);
        System.out.println("Sum of two numbers is = " + result);
    }

    // 2 - Function swapNumbers to Swap two variable values

    // This code doesn't work, it is written here to demonstrate that 
    // Java is using pass by value 
    static void swap(int number1, int number2)
    {
        int temp = number1;
        number1 = number2;
        number2 = temp;

        System.out.println(" number1 = " + number1 + " number2 = "+ number2);
    }

    // pass by ref example using the array
    static void swap_v2(int[] numbers)
    {
        int temp = numbers[0];
        numbers[0] = numbers[1];
        numbers[1] = temp;
    }

    static void invoke_swap()
    {
        int input1 = 10;
        int input2 = 20;
        System.out.println("BEFORE Input1 = " + input1 + " input2 = "+ input2);
        swap(input1, input2);
        System.out.println("AFTER Input1 = " + input1 + " input2 = "+ input2);

        int[] input3 = {10,20};
        swap_v2(input3);

        System.out.println("AFTER input3[0] = " + input3[0] + " input3[1] = "+ input3[1]);
    }

    static boolean isEven(int number)
    {
        if (number % 2 == 0)
        {
            System.out.println( number + " Number is even");
            return true;
        }
        else
        {
            System.out.println(number + " Number is odd");
            return false;
        }
    }

    static void invoke_isEven()
    {
        isEven(10);
        isEven(11);
    }

    // 4 - Function isNumber to return true if it is a digit

    static boolean isNumber(String input)
    {
        boolean result = true;

        for (int index=0; index < input.length(); index++)
        {
            char character = input.charAt(index);
            if (character < '0' || character > '9')
            {
                result = false;
                break;
            }
        }
        return result;
    }

    static void invoke_inNumber()
    {
        boolean result = isNumber("12a");
        if (result)
            System.out.println("It is a proper number");
        else
            System.out.println("It is a invalid number");
    }

    // 5 - Function  simpleGreetings to accept name as input and print simple greetings Namaskara name

    static void simpleInputAndGreet()
    {
        Scanner reader = new Scanner(System.in);
        String Name;

        Name = reader.nextLine();
        reader.close();

        System.out.println("Namaskara " + Name);
    }

    // Function to Print ASCII  values of string input

    static void printASCII(String input)
    {
        char character;

        for (int index=0; index < input.length(); index++)
        {
            character = input.charAt(index);
            int asciiValue = character;

            System.out.println("Asccii value fo the char  " + character + "  " +  asciiValue);
        }
    }

    static void invoke_printAscii()
    {
        printASCII("abc");
    }

    // 7 Function to getStrlength to get string length

    static int getStringLength(String input)
    {
        int length = 0;

        for (char c : input.toCharArray()) {
            length++;
        }

        return length;
    }

    static void invoke_stringlength()
    {
        String input = "ab";
        int result = getStringLength(input);

        System.out.println("Length of the string is " + result);
    }


    // 8 - Function to Count vowels  getCountOfOvewel for a given string

    static int getCountOfOvewels(String input)
    {
        int count = 0;

        for (int index=0; index < input.length(); index++)
        {
            char character  = input.charAt(index);

            if (character == 'a' || character == 'e' || character == 'i' || character == 'o' || character == 'u')
                count++;
        }

        return count;
    }

    static void invoke_getCountOfVowels()
    {
        String input = "mahesh";

        int count = getCountOfOvewels(input);
        System.out.println("Number of voewes in string " + input + "   " + count);
    }

    static String reveseString(String input)
    {
        StringBuilder output = new StringBuilder();

        for (int index = input.length()-1 ; index >= 0; index--)
        {
            output.append(input.charAt(index));
        }

        return output.toString();
    }

    static String reveseStringV2(String input)
    {
        char[] inputArray = input.toCharArray();
        
        int leftIndex = 0;
        int rightIndex = input.length()-1;
        
        while(leftIndex < rightIndex)
        {
            char temp = inputArray[leftIndex];
            inputArray[leftIndex] = inputArray[rightIndex];
            inputArray[rightIndex] = temp;

            leftIndex++;
            rightIndex--;
        }

        String output = new String(inputArray);
        System.out.println(output);

        return output;
    }

    static void invoke_reverseString()
    {
        String input1 = "abcd";

        //String output1 = reveseString(input1);

        String output1 = reveseStringV2(input1);

        System.out.println("Input " + input1 + " Output " + output1);
    }

    // 10 - Function to get sum of all elements in the integer array getSum

    static int getSum(int[] numbers)
    {
        int sum = 0 ;

        for (int index =0; index < numbers.length; index++)
        {
            sum = sum + numbers[index];
        }
        return sum;
    }

    static void invoke_getSumArray()
    {
        int[] input1 = {1,2,3};

        int sumOfElements = getSum(input1);

        System.out.println("Sum of elements = " + sumOfElements);

    }

    // 11 - Function to find given string is Palindrome, function isPalidrome returns true if string is palindrome

    static boolean isPalidrome(String input)
    {
        boolean result = true;

        int leftIndex = 0;
        int rightIndex = input.length()-1;

        while(leftIndex < rightIndex)
        {
            if (input.charAt(leftIndex) != input.charAt(rightIndex))
            {
                result = false;
                break;
            }
            leftIndex++;
            rightIndex--;
        }

        return result;
    }
    
    static void invoke_isPalidrome()
    {
        String input1 = "abba"; // abcba


        boolean result = isPalidrome(input1);

        if (result == true)
        {
            System.out.println("String is palindrome");
        }
        else
        {
            System.out.println("String is NOT palindrome");
        }
    
    }

    // 12 - Function to print max and min value from an integer array ,  printMaxMin

    static void printMaxMin(int[] numbers)
    {
        int max = Integer.MIN_VALUE;
        int min = Integer.MAX_VALUE;

        for (int index=0; index < numbers.length; index++)
        {
            if (numbers[index] > max)
                max = numbers[index];

            if (numbers[index] < min)
                min = numbers[index];
                
        }
        System.out.println("Max value = " + max + " Min value = " + min);
    }

    static void printMaxMinV2(int[] numbers)
    {
        if (numbers.length == 0)
            return;
        
        int max = numbers[0] ;
        int min = numbers[0];

        for (int index=1; index < numbers.length; index++)
        {
            if (numbers[index] > max)
                max = numbers[index];

            if (numbers[index] < min)
                min = numbers[index];
                
        }
        System.out.println("Max value = " + max + " Min value = " + min);
    }

    static void invoke_printMaxMin()
    {
        //int[] input1 = {5,2,-3,4,5,-6,999};

        //int[] input1 = {-1,-2,-3};
        int[] input1 = {-1};

        printMaxMin(input1);
    }

    // 13 - Function to search in an sorted integer array
    static boolean binarySearch(int[] numbers, int key)
    {
        boolean isFound = false;

        int leftIndex = 0;
        int rightIndex = numbers.length - 1;
        int midIndex = (rightIndex - leftIndex) / 2;
        
        while (leftIndex <= rightIndex)
        {
            if (key == numbers[midIndex])
            {
                isFound = true;
                break;
            }
            else if (key > numbers[midIndex])
            {
                leftIndex = midIndex+1;
            }
            else if (key < numbers[midIndex])
            {
                rightIndex = rightIndex-1;
            }

            midIndex = leftIndex + (rightIndex - leftIndex)/2; 
        }

        return isFound;
    }

    static void invoke_binarySearch()
    {
        int[] input1 = { 1,2,3,4,5,6,7,8,9,10};
        int key = 10;

        boolean result = binarySearch(input1, key);

        if (result)
        {
            System.out.println("number is found");
        }
        else
        {
            System.out.println("number is NOT found");
        }

    }

    // 14 - Function to merge two arrays and return combined output in first array

    // Assume that master array has memory allocated to have all elements from data 
    static void mergeArrays(int[] masterArray, int[] data)
    {
        if (masterArray == null || data == null)            
            return;
        
            
        
        int countData = data.length;

        int startIndex =  masterArray.length - countData ; 

        for (int dataIndex =0 ; startIndex < masterArray.length ; startIndex++, dataIndex++)
        {
            masterArray[startIndex] = data[dataIndex];
        }
    }

    static void printArray(int[] numbers)
    {
        for (int index=0; index < numbers.length; index++)
        {
            System.out.println(numbers[index]);
        }
    }

    static void invoke_mergeArrays()
    {
        int[] masterArray = { 1,2,3,0,0,0,0};
        //int[] masterArray = { 1,2,3};
        int[] data = {5,9,20,24};

        mergeArrays(masterArray, data);

        printArray(masterArray);
    }

    // 15 - Function get second largest element in an integer array  getSecondLargest

    static int getSecondLargest(int[] numbers)
    {
        if (numbers == null)
            return -1;
        
        if (numbers.length == 0)
            return -1;
        
        int largest = numbers[0];
        int secondLargest = numbers[0];

        for( int index=1; index < numbers.length; index++)
        {
            if (numbers[index] > largest)
            {
                secondLargest = largest;
                largest = numbers[index];
            }
            else if (numbers[index] > secondLargest)
            {
                secondLargest = numbers[index];
            }
        }

        return secondLargest;
    }

    static void invoke_getSecondLargest()
    {
        int[] input1 = {1,2,3,4,5,6};
        //int[] input1 = {5,1};
        //int[] input1 = {1};

        int result = getSecondLargest(input1);

        System.out.print("Second largest element is " + result);
    }

    // 16 - Function to print unique elements in an integer array   printUniqueElements

    static void printUniqueElements(int[] numbers)
    {
        for (int readIndex=0 ; readIndex < numbers.length; readIndex++)
        {
            boolean isDuplicate = false;
            
            // Check if the number has any duplicates in the array
            for (int compareIndex=0; compareIndex< numbers.length; compareIndex++)
            {
                if (readIndex == compareIndex)
                    continue;

                if (numbers[readIndex] == numbers[compareIndex])
                {
                    isDuplicate = true;
                    break;
                }
            }

            if (!isDuplicate)
                System.out.println(numbers[readIndex]);
        }
    }

    static void invoke_printUniqueElements()
    {
        int[] intput1 = {6,1,2,3,4,2,6,4};
        printUniqueElements(intput1);
    }


    // 17 - Function to print intersection or common elements of two integer arrays  getCommonElements

    static void printCommonElements(int[] input1, int[] input2)
    {
        for (int input1Index=0; input1Index < input1.length; input1Index++ )
        {
            boolean isFound = false;
            for (int input2Index=0; input2Index< input2.length; input2Index++ )
            {
                if (input1[input1Index] == input2[input2Index])
                {
                    isFound = true;
                    break;
                }
            }

            if (isFound)
                System.out.println(input1[input1Index]);
        }
    }

    static void invoke_printCommonElements()
    {
        int[] input1 = {1,2,3,4,5};
        int[] input2 = {4,5,9,10};

        printCommonElements(input1, input2);
    }

// 18 - Function to get count of words in the string  getCountOfWords

static int getCountOfWords(String input)
{
    int countOfWords = 0;

    if ( input == null)
        return countOfWords;

    if (input.length() == 0)
        return countOfWords;
    
    
    char prevCharacter = input.charAt(0);

    for(int index=0; index < input.length(); index++)
    {
        char oneChar = input.charAt(index);

        if (oneChar == ' ' || oneChar == '\t' || oneChar == '\n')
        {
            if (prevCharacter != ' ' && prevCharacter != '\t' && prevCharacter != '\n')
                countOfWords++;
        }
        prevCharacter = oneChar;
    }

    //Increment the count for the last word
    countOfWords = countOfWords + 1;
    return countOfWords;
}

    static void invoke_getCountOfWords()
    {
        //String input = "India is a great country";
        //String input = null;
        //String input = ""; // Empty string 

        //String input = "a"; // Single character

        String input = "Namaskara  Bharat";


        int countOfWords = getCountOfWords(input);
        System.out.println("Number of words in  " + input);
        System.out.println(countOfWords);
    }

// 19 - Function to print binary values of various input like integer, char , also perform shift operations on integers

    static void printBinary(int number) // Singed Int, positive and negative numbers 
    {
        if (number < 0)
            return;

        int countOfBits = Integer.BYTES * 8 ;

        // Ex: Integer is 4 bytes, 4*8 = 32 bits , left most bit is for the sign
        // 31 bits for the value 

        int mask = 1; 
        mask = mask << (countOfBits - 2);

        System.out.println("\nBinary form of number " + number + "  ");
        while (mask > 0)
        {
            int result = number & mask;
            if (result != 0)
                System.out.print("1");
            else    
                System.out.print("0");
            
            mask = mask >> 1;
        }
    }

    static void invoke_printBinary()
    {
        printBinary(500);
        printBinary(2);
        printBinary(3);
        printBinary(4);

    }

// 20 - Function to remove spaces from the string  removeSpaces

    static String removeSpaces(String input)
    {
        StringBuilder result = new StringBuilder();

        for (int index=0 ; index < input.length(); index++)
        {
            char oneChar = input.charAt(index);
            if (oneChar == ' ')
                continue;
            
            result.append(oneChar);
        }

        return result.toString();
    }

    static void invoke_removeSpaces()
    {
        String result = "";
        
        result = removeSpaces("Namaskara friends");
        System.out.println(result);

        result = removeSpaces("   Namaskara    friends   ");
        System.out.println(result);

    }

    public static void main(String[] args)
    {
        invoke_removeSpaces();
    }


}
