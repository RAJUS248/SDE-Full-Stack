package ExceptionHandling;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.Reader;

class ExceptionHandlingDemo {

    public static void main(String[] args) {
        // readAndPrintFile("Myfirstfile.txt");
        checkEligiblityForVoting();
    }

    public static void checkAge(int age) throws Exception
    {
        if (age<18)
            throw new Exception("Not allowed to vote before 18 years");
        
        System.out.println("Eligible to vote");
    }

    public static void checkEligiblityForVoting()
    {
        try
        {
            // #1 Happy path scenario
            checkAge(16);
            //checkIDDuplicate()
            //checkAddress()
            //CheckCitizenship()
            //CheckBirthCertficate()
        }
        // #2 Error handling 
        catch (Exception ex)
        {
            System.out.println("Not allowed to vote below 18 years");
        }
        // #3 - cleanup
        finally
        {
            System.out.println("Cleaning work is done");
        }
    }

    public static void readAndPrintFile(String filePath)
    {
        try
        {        
            FileReader reader = new FileReader(filePath);
            BufferedReader buffer = new BufferedReader(reader);
            String content = buffer.readLine();
        }
        catch (Exception ex)
        {
            System.out.println(ex.toString());            
        }
        finally
        {
            System.out.println("Nothing to clearn, evertying is fine!");
        }
    }

    public static void readFileDemo2(String filePath)
    {
        FileReader reader = null;

        try
        {
            reader = new FileReader(filePath);
            BufferedReader buffer = new BufferedReader(reader);
            String content = buffer.readLine();
        }
        catch (FileNotFoundException ex)
        {
            System.out.println("⚠️ Error: File not found at " + filePath);
        }
        catch (IOException ex)
        {
            System.out.println("IO exception occured " + filePath);
        }
        finally 
        {
            try {
                if (reader != null)
                {
                    reader.close();
                }
            }
            catch (Exception ex)
            {
                // do nothing , swallow the exception.
            }

        }
    }
}