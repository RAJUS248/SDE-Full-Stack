public class StarPatternPrinting {

    public static void main(String[] args) {
        PrintStarGrid(5);
        PrintStarTriagleLeft(5);
        PrintStarTriagleExp(5);
    }

    public static void PrintGrid(int size)
    {
        for (int row=1; row <= size; row++)
        {
            for (int col=1; col <= size; col++)
            {
                System.out.print(row + "," + col + " ");
            }
            System.out.println();
        }
    }

    public static void PrintStarGrid(int size)
    {
        for (int row=1; row <= size; row++)
        {
            for (int col=1; col <= size; col++)
            {
                System.out.print("*");
            }
            System.out.println();
        }
    }

    public static void PrintStarTriagleLeft(int size)
    {
        for (int row=1; row <= size; row++)
        {
            for (int col=1; col <= row; col++)
            {
                System.out.print("*");
            }
            System.out.println();
        }
    }

    public static void PrintStarTriagleExp(int size)
    {
        for (int row=size; row >= 1; row--)
        {
            for (int col=row; col >= 1; col--)
            {
                System.out.print("*");
            }
            System.out.println();
        }
    }
    
}