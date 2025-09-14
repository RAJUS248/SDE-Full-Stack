public class StarPatternPrinting {

    public static void main(String[] args) {
        
    }



    public static void PrintGrid1(int size)
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

    public static void PrintStarGrid2(int size)
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

    public static void PrintStarTriagleLeft2(int size)
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

    public static void PrintStarTriagleExp2(int size)
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