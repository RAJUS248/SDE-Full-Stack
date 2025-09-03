from typing import List, Tuple, Union



def f(l):
 a=b=float('-inf')
 for x in l:
  if x>a:
   b=a
   a=x
  elif x>b and x!=a:
   b=x
 return a,b














def get_first_and_second_largest(numbers: List[Union[int, float]]) -> Tuple[Union[int, float], Union[int, float]]:
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list.")

    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements.")

    first_largest = second_largest = float('-inf')
    for number in numbers:
        if not isinstance(number, (int, float)):
            raise ValueError("List must contain only numeric values.")

        if number > first_largest:
            second_largest = first_largest
            first_largest = number
        elif first_largest > number > second_largest:
            second_largest = number

    if second_largest == float('-inf'):
        raise ValueError("List must contain at least two unique values.")

    return first_largest, second_largest

print(get_first_and_second_largest([10, 5, 30, 20, 30]))  # Output: (30, 20)
