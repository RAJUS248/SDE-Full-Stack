
# 🧠 Set Operations in Python — With Student Course Funnel Example

This guide covers core set operations in Python using a real-world example of students going through an online course funnel.

---

## 📊 Data Sets: Students and Course Funnel

```python
students_trial_course = {"ram", "sham", "radha", "mahesh", "magesh"}
students_bought_course = {"radha", "magesh"}
students_showed_interest = {"ram", "sham", "radha"}
```

---

## 🔹 Who tried but didn't buy? (`difference`)

```python
not_converted = students_trial_course - students_bought_course
print("Tried but didn't buy:", not_converted)
# Output: {'ram', 'sham', 'mahesh'}
```

---

## 🔹 Who bought but didn’t take trial?

```python
bought_without_trial = students_bought_course - students_trial_course
print("Bought without trial:", bought_without_trial)
# Output: set()
```

---

## 🔹 Who tried and also showed interest? (`intersection`)

```python
interested_and_tried = students_trial_course & students_showed_interest
print("Tried and interested:", interested_and_tried)
# Output: {'ram', 'sham', 'radha'}
```

---

## 🔹 All unique students in the funnel (`union`)

```python
all_students = students_trial_course | students_bought_course | students_showed_interest
print("All unique students:", all_students)
# Output: {'magesh', 'radha', 'mahesh', 'ram', 'sham'}
```

---

## 🔹 Who only showed interest but did not try?

```python
interested_but_not_tried = students_showed_interest - students_trial_course
print("Interested but not tried:", interested_but_not_tried)
# Output: set()
```

---

## 🔹 Who bought the course and also showed interest?

```python
interested_and_bought = students_bought_course & students_showed_interest
print("Interested and bought:", interested_and_bought)
# Output: {'radha'}
```

---

## 🔹 Symmetric Difference: in trial or interest but not both

```python
trial_xor_interest = students_trial_course ^ students_showed_interest
print("Trial XOR Interest (but not both):", trial_xor_interest)
# Output: {'mahesh', 'magesh'}
```

---

## 🔹 Subset Check: Did all who bought take the trial?

```python
print(students_bought_course.issubset(students_trial_course))  
# Output: True
```

---

## 🛠️ Summary of Key Set Operations

| Operation                | Symbol | Method                   | Description                                |
|--------------------------|--------|---------------------------|--------------------------------------------|
| Union                    | `|`    | `set1.union(set2)`        | All unique items from both sets            |
| Intersection             | `&`    | `set1.intersection(set2)` | Common items in both sets                  |
| Difference               | `-`    | `set1.difference(set2)`   | Items in first set but not in second       |
| Symmetric Difference     | `^`    | `set1.symmetric_difference(set2)` | Items in either but not both     |
| Subset check             | —      | `set1.issubset(set2)`     | True if all items of set1 are in set2      |
| Superset check           | —      | `set1.issuperset(set2)`   | True if all items of set2 are in set1      |
| Disjoint check           | —      | `set1.isdisjoint(set2)`   | True if no common items                    |

---

## ✅ Real-World Use Cases for Sets

- Removing duplicates
- Checking membership (faster than lists)
- Managing unique users, tags, IDs, etc.
- Comparing large datasets efficiently

---
