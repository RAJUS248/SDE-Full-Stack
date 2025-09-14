import java.util.ArrayList;

public class LoopsAdvanced {

    public static void Print100Stars(int countOfStars)
    {
        for (int count=1; count <= countOfStars; count++)
        {
            System.out.print("*");
        }
    }

    public static void PrintStarGrid(int gridSize)
    {
        
        for (int count=1; count <= gridSize; count++)
        {
            for (int row=1; row<= gridSize; row++)
            {
                System.out.print("*");
            }
            System.out.println("");
        }
    }

    public static void PrintStarGridConcatApproach(int gridSize)
    {   
        for (int count=1; count <= gridSize; count++)
        {
            StringBuilder line = new StringBuilder();
            for (int row=1; row<= gridSize; row++)
            {
                line.append("*");
            }
            System.out.println(line.toString());
        }
    }

    public static void printStarsForArray(int[] numbers)
    {
        for (int index=0; index < numbers.length; index++) // To read elements from the array
        {
            for (int count=1; count <= numbers[index] ; count++ ) // To print *
            {
                System.out.print("*");
            }
            System.out.println("");
        }
    }

     public static void PrintStarGridSkipEven(int gridSize)
    {   
        for (int count=1; count <= gridSize; count++)
        {
            StringBuilder line = new StringBuilder();
            for (int row=1; row<= gridSize; row++)
            {
                // How to check if row value is even
                /* 
                if (row % 2 == 0)
                {
                    line.append(" ");
                }
                else
                {
                    line.append("*");
                } */
                line.append(row % 2 == 0 ? " " : "*");
            }
            System.out.println(line.toString());
        }
    }

    public static void PrintStarsOnlyAtBorders(int gridSize)
    {
        for (int row=1; row <= gridSize; row++)
        {
            StringBuilder line = new StringBuilder();
            for (int column=1; column <= gridSize; column++)
            {
                /*if (row == 1 || row == gridSize || column == 1 || column == gridSize)
                {
                    line.append("* ");
                }
                else
                {
                    line.append("  ");
                }*/

                Boolean isStar = row == 1 || row == gridSize || column == 1 || column == gridSize;
                line.append(isStar ? "* ": "  ");
            }
            System.out.println(line.toString());
        }
    }

    public static void PrintPyramid(int height)
    {
        int countOfStars = 1;
        for (int level=1; level <= height; level++)
        {
            int noOfSpace = height-level;
            StringBuilder line = new StringBuilder();
            for (int count=0; count<noOfSpace; count++)
            {
                line.append(" ");
            }

            for (int count=0; count<countOfStars; count++)
            {
                line.append("*");
            }

            System.out.println(line.toString());
            countOfStars = countOfStars + 2;
        }
    }

    public static void PrintInvertedPyramid(int height)
    {
        
        for (int level=1; level <= height; level++)
        {
            int noOfSpace = level - 1;
            int noOfStars = ( height - level ) * 2 + 1;

            StringBuilder line = new StringBuilder();
            for (int count=0; count<noOfSpace; count++)
            {
                line.append(" ");
            }

            for (int count=0; count<noOfStars; count++)
            {
                line.append("*");
            }

            System.out.println(line.toString());
        }
    }

    public static void main(String[] args) {
        PrintInvertedPyramid(10);
        PrintPyramid(10);
        //PrintStarsOnlyAtBorders(10);

        //Print100Stars(10000);
        // PrintStarGrid(5);

        //int[] numbers = { 1,5,8,10,4,6,9,10,11,12};
        //printStarsForArray(numbers);

        //PrintStarGridConcatApproach(5);

        //PrintStarGridSkipEven(5);
    }
}
