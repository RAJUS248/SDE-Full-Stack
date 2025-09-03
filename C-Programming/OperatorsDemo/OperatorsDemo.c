#include <stdio.h>
#include <math.h>

void demonstrateArithmeticOperators() {
    // Arithmetic Operators
    int countOfMangos = 10, countOfApples = 3;
    int answer;

    printf("Arithmetic Operators:\n");

    // Addition
    answer = countOfMangos + countOfApples;
    printf("Addition: %d + %d = %d\n", countOfMangos, countOfApples, answer);

    // Subtraction
    answer = countOfMangos - countOfApples;
    printf("Subtraction: %d - %d = %d\n", countOfMangos, countOfApples, answer);

    // Multiplication
    answer = countOfMangos * countOfApples;
    printf("Multiplication: %d * %d = %d\n", countOfMangos, countOfApples, answer);

    // Division
    answer = countOfMangos / countOfApples;
    printf("Division: %d / %d = %d\n", countOfMangos, countOfApples, answer);

    // Modulus
    answer = countOfMangos % countOfApples;
    printf("Modulus: %d %% %d = %d\n", countOfMangos, countOfApples, answer);

    // Exponentiation
    double expAnswer = pow(countOfMangos, countOfApples);
    printf("Exponentiation: %d ** %d = %.2f\n", countOfMangos, countOfApples, expAnswer);

    // Floor Division (using integer division in C)
    answer = countOfMangos / countOfApples;
    printf("Floor Division: %d // %d = %d\n", countOfMangos, countOfApples, answer);
}

void demonstrateRelationalOperators() {
    // Relational Operators
    int countOfMangos = 10, countOfApples = 3;
    int boolAnswer;

    printf("\nRelational Operators:\n");

    // Equal to
    boolAnswer = (countOfMangos == countOfApples);
    printf("Equal to: %d == %d -> %d\n", countOfMangos, countOfApples, boolAnswer);

    // Not equal to
    boolAnswer = (countOfMangos != countOfApples);
    printf("Not equal to: %d != %d -> %d\n", countOfMangos, countOfApples, boolAnswer);

    // Greater than
    boolAnswer = (countOfMangos > countOfApples);
    printf("Greater than: %d > %d -> %d\n", countOfMangos, countOfApples, boolAnswer);

    // Less than
    boolAnswer = (countOfMangos < countOfApples);
    printf("Less than: %d < %d -> %d\n", countOfMangos, countOfApples, boolAnswer);

    // Greater than or equal to
    boolAnswer = (countOfMangos >= countOfApples);
    printf("Greater than or equal to: %d >= %d -> %d\n", countOfMangos, countOfApples, boolAnswer);

    // Less than or equal to
    boolAnswer = (countOfMangos <= countOfApples);
    printf("Less than or equal to: %d <= %d -> %d\n", countOfMangos, countOfApples, boolAnswer);
}

void demonstrateLogicalOperators() {
    // Logical Operators
    int isReady = 1, isGood = 0;
    int answer;

    printf("\nLogical Operators:\n");

    // AND
    answer = isReady && isGood;
    printf("AND: %d and %d -> %d\n", isReady, isGood, answer);

    // OR
    answer = isReady || isGood;
    printf("OR: %d or %d -> %d\n", isReady, isGood, answer);

    // NOT
    answer = !isReady;
    printf("NOT: not %d -> %d\n", isReady, answer);
}

void demonstrateBitwiseOperators() {
    // Bitwise Operators
    int redTeamScore = 5, whiteTeamScore = 2;  // redTeamScore = 101 in binary, whiteTeamScore = 10 in binary
    int answer;

    printf("\nBitwise Operators:\n");

    // AND
    answer = redTeamScore & whiteTeamScore;
    printf("AND: %d & %d -> %d\n", redTeamScore, whiteTeamScore, answer);

    // OR
    answer = redTeamScore | whiteTeamScore;
    printf("OR: %d | %d -> %d\n", redTeamScore, whiteTeamScore, answer);

    // XOR
    answer = redTeamScore ^ whiteTeamScore;
    printf("XOR: %d ^ %d -> %d\n", redTeamScore, whiteTeamScore, answer);

    // NOT
    answer = ~redTeamScore;
    printf("NOT: ~%d -> %d\n", redTeamScore, answer);

    // Left shift
    answer = redTeamScore << whiteTeamScore;
    printf("Left shift: %d << %d -> %d\n", redTeamScore, whiteTeamScore, answer);

    // Right shift
    answer = redTeamScore >> whiteTeamScore;
    printf("Right shift: %d >> %d -> %d\n", redTeamScore, whiteTeamScore, answer);
}

void demonstrateAssignmentOperators() {
    // Assignment Operators
    int totalScore = 5;
    int answer;

    printf("\nAssignment Operators:\n");

    // Assign
    answer = totalScore;
    printf("Assign: totalScore = %d\n", answer);

    // Add and assign
    totalScore += 2;
    answer = totalScore;
    printf("Add and assign: totalScore += 2 -> %d\n", answer);

    // Subtract and assign
    totalScore -= 1;
    answer = totalScore;
    printf("Subtract and assign: totalScore -= 1 -> %d\n", answer);

    // Multiply and assign
    totalScore *= 3;
    answer = totalScore;
    printf("Multiply and assign: totalScore *= 3 -> %d\n", answer);

    // Divide and assign
    totalScore /= 2;
    answer = totalScore;
    printf("Divide and assign: totalScore /= 2 -> %d\n", answer);

    // Modulus and assign
    totalScore %= 3;
    answer = totalScore;
    printf("Modulus and assign: totalScore %%= 3 -> %d\n", answer);

    // Floor divide and assign
    totalScore /= 2;
    answer = totalScore;
    printf("Floor divide and assign: totalScore /= 2 -> %d\n", answer);

    // Exponent and assign (using pow function in C)
    totalScore = pow(totalScore, 3);
    answer = totalScore;
    printf("Exponent and assign: totalScore **= 3 -> %d\n", answer);
}

void demonstrateOperators() {
    demonstrateArithmeticOperators();
    demonstrateRelationalOperators();
    demonstrateLogicalOperators();
    demonstrateBitwiseOperators();
    demonstrateAssignmentOperators();
}

int main() {
    demonstrateOperators();
    return 0;
}
