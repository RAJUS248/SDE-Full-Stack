def demonstrate_arithmetic_operators():
    # Arithmetic Operators
    countOfMangos, countOfApples = 10, 3
    
    # Addition
    answer = countOfMangos + countOfApples
    print("Arithmetic Operators:")
    print(f"Addition: {countOfMangos} + {countOfApples} = {answer}")
    
    # Subtraction
    answer = countOfMangos - countOfApples
    print(f"Subtraction: {countOfMangos} - {countOfApples} = {answer}")
    
    # Multiplication
    answer = countOfMangos * countOfApples
    print(f"Multiplication: {countOfMangos} * {countOfApples} = {answer}")
    
    # Division
    answer = countOfMangos / countOfApples
    print(f"Division: {countOfMangos} / {countOfApples} = {answer}")
    
    # Modulus
    answer = countOfMangos % countOfApples
    print(f"Modulus: {countOfMangos} % {countOfApples} = {answer}")
    
    # Exponentiation
    answer = countOfMangos ** countOfApples
    print(f"Exponentiation: {countOfMangos} ** {countOfApples} = {answer}")
    
    # Floor Division
    answer = countOfMangos // countOfApples
    print(f"Floor Division: {countOfMangos} // {countOfApples} = {answer}")

def demonstrate_relational_operators():
    # Relational Operators
    countOfMangos, countOfApples = 10, 3
    
    # Equal to
    answer = countOfMangos == countOfApples
    print("\nRelational Operators:")
    print(f"Equal to: {countOfMangos} == {countOfApples} -> {answer}")
    
    # Not equal to
    answer = countOfMangos != countOfApples
    print(f"Not equal to: {countOfMangos} != {countOfApples} -> {answer}")
    
    # Greater than
    answer = countOfMangos > countOfApples
    print(f"Greater than: {countOfMangos} > {countOfApples} -> {answer}")
    
    # Less than
    answer = countOfMangos < countOfApples
    print(f"Less than: {countOfMangos} < {countOfApples} -> {answer}")
    
    # Greater than or equal to
    answer = countOfMangos >= countOfApples
    print(f"Greater than or equal to: {countOfMangos} >= {countOfApples} -> {answer}")
    
    # Less than or equal to
    answer = countOfMangos <= countOfApples
    print(f"Less than or equal to: {countOfMangos} <= {countOfApples} -> {answer}")

def demonstrate_logical_operators():
    # Logical Operators
    isReady, isGood = True, False
    
    # AND
    answer = isReady and isGood
    print("\nLogical Operators:")
    print(f"AND: {isReady} and {isGood} -> {answer}")
    
    # OR
    answer = isReady or isGood
    print(f"OR: {isReady} or {isGood} -> {answer}")
    
    # NOT
    answer = not isReady
    print(f"NOT: not {isReady} -> {answer}")

def demonstrate_bitwise_operators():
    # Bitwise Operators
    redTeamScore, whiteTeamScore = 5, 2  # redTeamScore = 101 in binary, whiteTeamScore = 10 in binary
    
    # AND
    answer = redTeamScore & whiteTeamScore
    print("\nBitwise Operators:")
    print(f"AND: {redTeamScore} & {whiteTeamScore} -> {answer}")
    
    # OR
    answer = redTeamScore | whiteTeamScore
    print(f"OR: {redTeamScore} | {whiteTeamScore} -> {answer}")
    
    # XOR
    answer = redTeamScore ^ whiteTeamScore
    print(f"XOR: {redTeamScore} ^ {whiteTeamScore} -> {answer}")
    
    # NOT
    answer = ~redTeamScore
    print(f"NOT: ~{redTeamScore} -> {answer}")
    
    # Left shift
    answer = redTeamScore << whiteTeamScore
    print(f"Left shift: {redTeamScore} << {whiteTeamScore} -> {answer}")
    
    # Right shift
    answer = redTeamScore >> whiteTeamScore
    print(f"Right shift: {redTeamScore} >> {whiteTeamScore} -> {answer}")

def demonstrate_assignment_operators():
    # Assignment Operators
    totalScore = 5
    
    # Assign
    answer = totalScore
    print("\nAssignment Operators:")
    print(f"Assign: totalScore = {answer}")
    
    # Add and assign
    # totalScore = totalScore + 2
    totalScore += 2
    answer = totalScore
    print(f"Add and assign: totalScore += 2 -> {answer}")
    
    # Subtract and assign
    totalScore -= 1
    answer = totalScore
    print(f"Subtract and assign: totalScore -= 1 -> {answer}")
    
    # Multiply and assign
    totalScore *= 3
    answer = totalScore
    print(f"Multiply and assign: totalScore *= 3 -> {answer}")
    
    # Divide and assign
    totalScore /= 2
    answer = totalScore
    print(f"Divide and assign: totalScore /= 2 -> {answer}")
    
    # Modulus and assign
    totalScore %= 3
    answer = totalScore
    print(f"Modulus and assign: totalScore %= 3 -> {answer}")
    
    # Floor divide and assign
    totalScore //= 2
    answer = totalScore
    print(f"Floor divide and assign: totalScore //= 2 -> {answer}")
    
    # Exponent and assign
    totalScore **= 3
    answer = totalScore
    print(f"Exponent and assign: totalScore **= 3 -> {answer}")

# Call each function to demonstrate operators
def demonstrate_operators():
    demonstrate_arithmetic_operators()
    demonstrate_relational_operators()
    demonstrate_logical_operators()
    demonstrate_bitwise_operators()
    demonstrate_assignment_operators()

# Run the main demonstration function
demonstrate_operators()
