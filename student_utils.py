"""
Student Academic Utility Functions
Author: Aryan Raj (JECRC University)
Debugging and Refactoring via Cursor AI (Lecture 8)
"""

PASS_MARK = 40

def calculate_average(marks):
    """
    Calculate the arithmetic average of marks.
    Fixed bug: Changed divisor from len(marks) - 1 to len(marks).
    Prevents ZeroDivisionError on single mark and incorrect calculation.
    """
    if not marks:
        return 0.0
    total = sum(marks)
    return float(total / len(marks))


def is_passing(mark):
    """
    Determine if a mark meets the passing threshold.
    Fixed bug: Changed strict inequality (mark > PASS_MARK) to inclusive (mark >= PASS_MARK).
    Ensures boundary value of 40 correctly passes.
    """
    return mark >= PASS_MARK


def get_grade(average):
    """
    Determine student grade category from average.
    Fixed bug: Reordered evaluation sequence so >= 90 is checked before >= 60.
    Prevents Distinction scores (e.g. 95) from erroneously returning 'First'.
    """
    if average >= 90:
        return "Distinction"
    elif average >= 60:
        return "First"
    elif average >= 45:
        return "Second"
    return "Fail"
