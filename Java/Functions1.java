public class Functions1 {
    public static void main(String[] args)
    {
        //String StudentName = getTopperNameForSubjectGrade(1, "Maths");
        //System.out.println(StudentName);

        printStudentDetails(1);
    }

    // Who is the topper 
    // Which subject ?
    // Which grade ?
    // response name of the student 

    static String getTopperNameForSubjectGrade(int grade, String subject)
    {
        //Dummy implenmentation 
        String name = "Sangeeta";
        return name;
    }

    // Returns array in which at 0 index boys count is present and 1 index girls count is present
    static int[] getTotalCountOfBoysGirls(int schoolID)
    {
        // Dummy 
        int[] results = {500,500};
        return results;
    }

    static void printStudentDetails(int studentId)
    {
        // Dummy 
        String name = "Radha";
        int age = 18;
        int grade = 10;
        double CGPA = 9.2;
        boolean isRegularToSchool = true;

        System.out.println(name);
        System.out.println(age);
        System.out.println(grade);
        System.out.println(CGPA);
        System.out.println(isRegularToSchool);
    }
    



}
