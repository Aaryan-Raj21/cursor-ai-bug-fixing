# Bug Fixing Notes: Lecture 8 (Cursor AI Assisted)

| Bug Name | Evidence / Failed Test | Root Cause | Fix Applied |
|---|---|---|---|
| Average Calculation | `calculate_average([80, 90, 100])` returned 135.0 instead of 90.0; single-mark `[40]` raised `ZeroDivisionError` | Divisor was written as `len(marks) - 1` | Changed denominator to `len(marks)` |
| Passing Boundary | `is_passing(40)` returned `False` | Used strict greater-than (`mark > PASS_MARK`) | Changed condition to `mark >= PASS_MARK` |
| Grade Ordering (Distinction) | `get_grade(95)` returned `"First"` instead of `"Distinction"` | `average >= 60` was evaluated before `average >= 90` | Reordered evaluation so `average >= 90` is checked first |
