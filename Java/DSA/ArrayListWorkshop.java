import java.util.ArrayList;

public class ArrayListWorkshop {
    
    public static void demoArrayList()
    {
        ArrayList list = new ArrayList();
        list.add("mahesh"); // zero indiex string 
        list.add(50);  // 1 - integer 
        
        System.out.println(list);
        System.out.println("Size of list: " + list.size());

        int number = (int) list.get(1);
        System.out.println("Number after typecasting " + number);
    }

    public static void DemoArrayListWithGenerics()
    {
        ArrayList<String> list = new ArrayList<>();
        list.add("mahesh");
        list.add("");

    }

    public static ArrayList<String> GetNames()
    {
        ArrayList<String> names = new ArrayList<>();
        names.add("mahesh");
        names.add("sangeeta");
        names.add("amit");
        names.add("santosh");
        names.add("mahesh");
        names.add("mahat");

        
        return names;
    }

    public static void DemoArrayListMethods(ArrayList<String> names)    
    {
        names.addFirst("First name");
        names.addLast("Last name");

        if ( names.contains("mahesh"))
        {
            System.out.print("Mahsh is there in the list");
        }

        ArrayList<String> findNames = new ArrayList<>();
        findNames.add("mahesh");
        findNames.add("santosh");

        if (names.containsAll(findNames))
        {
            System.out.print("Mahsh and Santosh are present in the list");
        }

        System.out.println(names);
    }
    
    public static void main(String[] args)
    {
        //demoArrayList();
        //DemoArrayListWithGenerics();

        ArrayList<String> members = GetNames();
        System.out.println(members);

        for (String member : members) {
            System.out.println(member);
        }

        DemoArrayListMethods(members);
        
    }
    
}
