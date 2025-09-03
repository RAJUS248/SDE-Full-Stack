public class OperatorsDemo {

    public static void demonstrateArithmeticOperators() {
        // Arithmetic Operators
        int countOfMangos = 10, countOfApples = 3;
        
        // Addition
        int answer = countOfMangos + countOfApples;
        System.out.println("Arithmetic Operators:");
        System.out.println("Addition: " + countOfMangos + " + " + countOfApples + " = " + answer);
        
        // Subtraction
        answer = countOfMangos - countOfApples;
        System.out.println("Subtraction: " + countOfMangos + " - " + countOfApples + " = " + answer);
        
        // Multiplication
        answer = countOfMangos * countOfApples;
        System.out.println("Multiplication: " + countOfMangos + " * " + countOfApples + " = " + answer);
        
        // Division
        answer = countOfMangos / countOfApples;
        System.out.println("Division: " + countOfMangos + " / " + countOfApples + " = " + answer);
        
        // Modulus
        answer = countOfMangos % countOfApples;
        System.out.println("Modulus: " + countOfMangos + " % " + countOfApples + " = " + answer);
        
        // Exponentiation
        double expAnswer = Math.pow(countOfMangos, countOfApples);
        System.out.println("Exponentiation: " + countOfMangos + " ** " + countOfApples + " = " + expAnswer);
        
        // Floor Division (using integer division in Java)
        answer = countOfMangos / countOfApples;
        System.out.println("Floor Division: " + countOfMangos + " // " + countOfApples + " = " + answer);
    }

    public static void demonstrateRelationalOperators() {
        // Relational Operators
        int countOfMangos = 10, countOfApples = 3;
        
        // Equal to
        boolean boolAnswer = (countOfMangos == countOfApples);
        System.out.println("\nRelational Operators:");
        System.out.println("Equal to: " + countOfMangos + " == " + countOfApples + " -> " + boolAnswer);
        
        // Not equal to
        boolAnswer = (countOfMangos != countOfApples);
        System.out.println("Not equal to: " + countOfMangos + " != " + countOfApples + " -> " + boolAnswer);
        
        // Greater than
        boolAnswer = (countOfMangos > countOfApples);
        System.out.println("Greater than: " + countOfMangos + " > " + countOfApples + " -> " + boolAnswer);
        
        // Less than
        boolAnswer = (countOfMangos < countOfApples);
        System.out.println("Less than: " + countOfMangos + " < " + countOfApples + " -> " + boolAnswer);
        
        // Greater than or equal to
        boolAnswer = (countOfMangos >= countOfApples);
        System.out.println("Greater than or equal to: " + countOfMangos + " >= " + countOfApples + " -> " + boolAnswer);
        
        // Less than or equal to
        boolAnswer = (countOfMangos <= countOfApples);
        System.out.println("Less than or equal to: " + countOfMangos + " <= " + countOfApples + " -> " + boolAnswer);
    }

    public static void demonstrateLogicalOperators() {
        // Logical Operators
        boolean isReady = true, isGood = false;
        
        // AND
        boolean answer = isReady && isGood;
        System.out.println("\nLogical Operators:");
        System.out.println("AND: " + isReady + " and " + isGood + " -> " + answer);
        
        // OR
        answer = isReady || isGood;
        System.out.println("OR: " + isReady + " or " + isGood + " -> " + answer);
        
        // NOT
        answer = !isReady;
        System.out.println("NOT: not " + isReady + " -> " + answer);
    }

    public static void demonstrateBitwiseOperators() {
        // Bitwise Operators
        int redTeamScore = 5, whiteTeamScore = 2;  // redTeamScore = 101 in binary, whiteTeamScore = 10 in binary
        
        // AND
        int answer = redTeamScore & whiteTeamScore;
        System.out.println("\nBitwise Operators:");
        System.out.println("AND: " + redTeamScore + " & " + whiteTeamScore + " -> " + answer);
        
        // OR
        answer = redTeamScore | whiteTeamScore;
        System.out.println("OR: " + redTeamScore + " | " + whiteTeamScore + " -> " + answer);
        
        // XOR
        answer = redTeamScore ^ whiteTeamScore;
        System.out.println("XOR: " + redTeamScore + " ^ " + whiteTeamScore + " -> " + answer);
        
        // NOT
        answer = ~redTeamScore;
        System.out.println("NOT: ~" + redTeamScore + " -> " + answer);
        
        // Left shift
        answer = redTeamScore << whiteTeamScore;
        System.out.println("Left shift: " + redTeamScore + " << " + whiteTeamScore + " -> " + answer);
        
        // Right shift
        answer = redTeamScore >> whiteTeamScore;
        System.out.println("Right shift: " + redTeamScore + " >> " + whiteTeamScore + " -> " + answer);
    }

    public static void demonstrateAssignmentOperators() {
        // Assignment Operators
        int totalScore = 5;
        
        // Assign
        int answer = totalScore;
        System.out.println("\nAssignment Operators:");
        System.out.println("Assign: totalScore = " + answer);
        
        // Add and assign
        totalScore += 2;
        answer = totalScore;
        System.out.println("Add and assign: totalScore += 2 -> " + answer);
        
        // Subtract and assign
        totalScore -= 1;
        answer = totalScore;
        System.out.println("Subtract and assign: totalScore -= 1 -> " + answer);
        
        // Multiply and assign
        totalScore *= 3;
        answer = totalScore;
        System.out.println("Multiply and assign: totalScore *= 3 -> " + answer);
        
        // Divide and assign
        totalScore /= 2;
        answer = totalScore;
        System.out.println("Divide and assign: totalScore /= 2 -> " + answer);
        
        // Modulus and assign
        totalScore %= 3;
        answer = totalScore;
        System.out.println("Modulus and assign: totalScore %= 3 -> " + answer);
        
        // Floor divide and assign
        totalScore /= 2;
        answer = totalScore;
        System.out.println("Floor divide and assign: totalScore /= 2 -> " + answer);
        
        // Exponent and assign (using pow function in Java)
        totalScore = (int) Math.pow(totalScore, 3);
        answer = totalScore;
        System.out.println("Exponent and assign: totalScore **= 3 -> " + answer);
    }

    public static void demonstrateOperators() {
        demonstrateArithmeticOperators();
        demonstrateRelationalOperators();
        demonstrateLogicalOperators();
        demonstrateBitwiseOperators();
        demonstrateAssignmentOperators();
    }

    public static void main(String[] args) {
        demonstrateOperators();
    }
}
