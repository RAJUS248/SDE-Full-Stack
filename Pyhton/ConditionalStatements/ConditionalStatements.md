
# 🧠 Python Conditional Statements – A Complete Guide

---

## 🚦 What Are Conditional Statements?

Conditional statements let your program make decisions based on certain conditions. It’s how we bring logic to life in code.

> 🎯 **Analogy**:  
A hiring panel evaluates a candidate based on:
- Coding skills  
- Problem-solving  
- CS fundamentals  
- CGPA  
- Communication skills

Just like interviewers use judgment, Python uses `if`, `else`, and `elif` to make logical choices.

---

## 🛠️ Types of Conditional Statements in Python

### 1. `if` Statement

```python
if condition:
    # execute this block
```

### 2. `if-else` Statement

```python
if condition:
    # true block
else:
    # false block
```

### 3. `if-elif-else` Statement

```python
if condition1:
    # block1
elif condition2:
    # block2
else:
    # fallback block
```

### 4. Nested `if` Statements

```python
if condition1:
    if condition2:
        # nested block
```

---

## 📊 Python Conditional Operators

| Symbol | Name                | Meaning                                             | Example               |
|--------|---------------------|-----------------------------------------------------|------------------------|
| `==`   | Equal to            | Checks if values are equal                         | `5 == 5` is True      |
| `!=`   | Not equal to        | Checks if values are not equal                     | `4 != 5` is True      |
| `>`    | Greater than        | True if left is greater than right                 | `10 > 3` is True      |
| `<`    | Less than           | True if left is less than right                    | `2 < 9` is True       |
| `>=`   | Greater than or equal to | True if left ≥ right                      | `6 >= 6` is True      |
| `<=`   | Less than or equal to    | True if left ≤ right                      | `4 <= 7` is True      |
| `and`  | Logical AND         | True if both conditions are True                   | `exp > 5 and rating > 8` |
| `or`   | Logical OR          | True if at least one condition is True             | `impact > 80 or perf > 7` |
| `not`  | Logical NOT         | Inverts the Boolean value                          | `not False` is True   |

---

## 👥 Hiring Decision Example – Interview Evaluation

### 🔧 Variables (All rated on scale of 1 to 5):

```python
coding_skill = 4
problem_solving = 5
cs_fundamentals = 4
cgpa = 8.2         # Out of 10
communication = 3
```

### ✅ Rule 1: Candidate passes technical if all core skills ≥ 4

```python
if coding_skill >= 4 and problem_solving >= 4 and cs_fundamentals >= 4:
    print("✅ Passed Technical Evaluation")
else:
    print("❌ Failed Technical Evaluation")
```

### ✅ Rule 2: CGPA must be ≥ 7.0 and communication ≥ 3

```python
if cgpa >= 7.0 and communication >= 3:
    print("✅ Meets Academic & Communication Criteria")
else:
    print("❌ Does not meet CGPA or communication bar")
```

### ✅ Final Hiring Decision

```python
if (
    coding_skill >= 4 and
    problem_solving >= 4 and
    cs_fundamentals >= 4 and
    cgpa >= 7.0 and
    communication >= 3
):
    print("🎉 Hiring Decision: SELECTED")
else:
    print("📋 Hiring Decision: REJECTED")
```

---

## 🧬 Order of Execution in Python Conditions

### Operator Precedence:

1. `()` Parentheses
2. Comparison operators: `==`, `!=`, `<`, `>`, `<=`, `>=`
3. Logical NOT: `not`
4. Logical AND: `and`
5. Logical OR: `or`

### Example:
```python
if (coding_skill >= 4 and not communication < 3) or cgpa > 9:
    print("Eligible for fast-track")
```

---

## 🐞 Real-World Bug Stories from Conditional Mistakes

### 🚀 NASA Mars Orbiter (1999)
- **Issue**: No condition checking for units (imperial vs metric).
- **Loss**: $125 million spacecraft destroyed.
- **Lesson**: Always validate input assumptions.

### 🛒 Amazon Pricing Glitch
- **Issue**: A wrong operator (`<` instead of `>`) in pricing logic.
- **Loss**: Expensive items sold for $0.01.
- **Lesson**: Triple-check your conditions!

---

## 📈 How Much Code Involves Conditional Statements?

📊 Studies suggest:
- 35% to 45% of business logic involves conditions.
- Crucial for validations, decision trees, algorithms, and UI control.

---

## 🧠 Best Practices for Writing Conditionals

| Best Practice | Why It’s Important |
|---------------|--------------------|
| ✅ Use clear variable names | `impact_score` is better than `x` |
| ✅ Avoid deep nesting | Improves readability |
| ✅ Use `elif` for multiple branches | Cleaner than nested `if` |
| ✅ Comment complex logic | Makes logic easier to understand |
| ✅ Use constants | Replace magic numbers with named values |
| ✅ Be explicit | Don't rely on truthy/falsy for clarity |
| ✅ Validate input types first | Avoid runtime crashes |

---

## 🎉 Summary

Conditional statements are the **decision-makers** in your code. Whether you're evaluating a candidate or launching a spacecraft, **logic matters!**  
A single mistake can cost you a hire—or millions 💸

---
