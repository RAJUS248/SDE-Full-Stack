arr = [10, 20, 30, 20, 10]  # Integer array

value_to_index = {}  # Dictionary declaration

for indexAsValue, valueAsKey in enumerate(arr):
    value_to_index[valueAsKey] = indexAsValue  # Key: element value, Value: index

indexOfNumber = value_to_index.get(10)

print(indexOfNumber)

print(arr)
print(value_to_index)


students = { "1": "mahesh", "2":"ram", "3":"sham"}

value_ret = students.get("3")
print(value_ret)

students["4"] = "radha"

print(students)

students.pop("1")

print(students)

