public class Operators {

    public static void main(String[] args) {
        // Arithmetic Operators
        int a = 10, b = 3;
        System.out.println("Arithmetic Operators:");
        System.out.println("Addition: " + a + " + " + b + " = " + (a + b));
        System.out.println("Subtraction: " + a + " - " + b + " = " + (a - b));
        System.out.println("Multiplication: " + a + " * " + b + " = " + (a * b));
        System.out.println("Division: " + a + " / " + b + " = " + (a / b));
        System.out.println("Modulus: " + a + " % " + b + " = " + (a % b));
        System.out.println("Exponentiation: " + a + " ^ " + b + " = " + (int)Math.pow(a, b));
        System.out.println("Floor Division: " + a + " // " + b + " = " + (a / b));

        // Relational Operators
        System.out.println("\nRelational Operators:");
        System.out.println("Equal to: " + a + " == " + b + " -> " + (a == b));
        System.out.println("Not equal to: " + a + " != " + b + " -> " + (a != b));
        System.out.println("Greater than: " + a + " > " + b + " -> " + (a > b));
        System.out.println("Less than: " + a + " < " + b + " -> " + (a < b));
        System.out.println("Greater than or equal to: " + a + " >= " + b + " -> " + (a >= b));
        System.out.println("Less than or equal to: " + a + " <= " + b + " -> " + (a <= b));

        // Logical Operators
        System.out.println("\nLogical Operators:");
        boolean x = true, y = false;
        System.out.println("AND: " + x + " && " + y + " -> " + (x && y));
        System.out.println("OR: " + x + " || " + y + " -> " + (x || y));
        System.out.println("NOT: !" + x + " -> " + (!x));

        // Bitwise Operators
        System.out.println("\nBitwise Operators:");
        int c = 5, d = 2;  // c = 101 in binary, d = 10 in binary
        System.out.println("AND: " + c + " & " + d + " -> " + (c & d));
        System.out.println("OR: " + c + " | " + d + " -> " + (c | d));
        System.out.println("XOR: " + c + " ^ " + d + " -> " + (c ^ d));
        System.out.println("NOT: ~" + c + " -> " + (~c));
        System.out.println("Left shift: " + c + " << " + d + " -> " + (c << d));
        System.out.println("Right shift: " + c + " >> " + d + " -> " + (c >> d));

        // Assignment Operators
        System.out.println("\nAssignment Operators:");
        int e = 5;
        System.out.println("Assign: e = " + e);
        e += 2;
        System.out.println("Add and assign: e += 2 -> " + e);
        e -= 1;
        System.out.println("Subtract and assign: e -= 1 -> " + e);
        e *= 3;
        System.out.println("Multiply and assign: e *= 3 -> " + e);
        e /= 2;
        System.out.println("Divide and assign: e /= 2 -> " + e);
        e %= 3;
        System.out.println("Modulus and assign: e %= 3 -> " + e);
        e <<= 2;
        System.out.println("Left shift and assign: e <<= 2 -> " + e);
        e >>= 1;
        System.out.println("Right shift and assign: e >>= 1 -> " + e);
        e &= 2;
        System.out.println("Bitwise AND and assign: e &= 2 -> " + e);
        e |= 2;
        System.out.println("Bitwise OR and assign: e |= 2 -> " + e);
        e ^= 2;
        System.out.println("Bitwise XOR and assign: e ^= 2 -> " + e);

        // Miscellaneous Operators
        System.out.println("\nMiscellaneous Operators:");
        int f = 6, g = 7;
        System.out.println("Conditional expression: " + f + " > " + g + " ? " + f + " : " + g + " -> " + (f > g ? f : g));
        System.out.println("Instance check: 5 instanceof Integer -> " + (Integer.valueOf(5) instanceof Integer));
    }
}
