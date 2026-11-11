# University Admission Eligibility System

A beginner-level Python program that checks whether an applicant meets a university's admission requirements using Mathematics, English, Science, and Interview scores.

This is **Problem 3** from a Python mentoring class assignment on **Conditional Statements (`if`, `elif`, and `else`)**.

## What the Program Does

The program asks the applicant to enter four scores:

- Mathematics
- English
- Science
- Interview

It first checks whether any score is outside the valid range of 0 to 100. If all scores are valid, it checks the subject and interview requirements one by one, then calculates the average of Mathematics, English, and Science.

The program displays **Admission Approved** if all requirements are met. Otherwise, it displays an admission rejection message for the first requirement that is not met.

## Admission Requirements

| Requirement | Minimum score |
|---|---:|
| Mathematics | 60 |
| English | 50 |
| Science | 55 |
| Interview | 70 |
| Average of Mathematics, English, and Science | 65 |

All four entered scores must be between 0 and 100.

## Example

**Input**

```text
Mathematics: 75
English: 60
Science: 70
Interview: 80
```

**Output**

```text
Average: 68.33333333333333.
Admission Approved!
```

## How to Run

1. Make sure Python 3 is installed.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run:

```bash
python "problem 3.U admission.py"
```

On some systems, use `python3` instead of `python`.

## Concepts Practiced

- Getting user input with `input()`
- Converting input to floating-point numbers with `float()`
- Conditional statements: `if`, `elif`, and `else`
- Nested conditional statements
- Comparison operators (`<`, `>`)
- Logical operators (`or`)
- Calculating an average
- Checking score validity and admission conditions
- Displaying results with f-strings

## Notes

- The average is calculated using Mathematics, English, and Science only; the Interview score is not included.
- The program checks requirements in sequence and displays the first unmet requirement, rather than listing every unmet requirement.
- The program validates that scores are within 0–100 before checking admission eligibility.

## Learning Context

This program was completed as **Problem 3** in Python mentoring classes. It is an exercise in applying conditional logic, nested decisions, logical operators, and arithmetic calculations to a university admission scenario.
