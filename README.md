# Bug Fixing Using Cursor AI (RED -> FIX -> GREEN)

Developed by **Aryan Raj** (JECRC University) based on Lecture 8 of the AI-Assisted Software Development course.

## Overview
This repository documents identifying and systematically eliminating critical logical bugs from a student grading utility module using Cursor AI and Python `unittest`.

## The RED -> FIX -> GREEN Lifecycle
1. **RED (Failing State):** Test suite executed against original buggy code; 4 out of 9 tests failed.
2. **FIX (Targeted Resolution):** AI-guided analysis isolated root causes in boundary comparison, denominator indexing, and conditional ordering.
3. **GREEN (Passing State):** All 9 tests passed without weakening test expectations.

## Bugs Resolved
* **Denominator Bug:** Fixed `total / (len(marks) - 1)` to `total / len(marks)`.
* **Boundary Condition Bug:** Fixed `mark > PASS_MARK` to `mark >= PASS_MARK` (pass mark = 40).
* **Grade Precedence Bug:** Checked `average >= 90` before `average >= 60`.

## Running the Unit Tests
```bash
python test_student_utils.py
```

Expected result:
```
Ran 9 tests in 0.001s
OK
```

## Author
* **Aryan Raj**
* GitHub: [@Aaryan-Raj21](https://github.com/Aaryan-Raj21)
