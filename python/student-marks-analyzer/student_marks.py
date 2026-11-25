"""Beginner project: summarize a small set of student marks.

Run:
    python student_marks.py

Uses fictional sample data and only the Python standard library.
"""

students = {
    "Asha": [78, 85, 91],
    "Ravi": [66, 72, 70],
    "Mina": [92, 88, 95],
    "Kabir": [54, 61, 58],
}


def calculate_average(marks):
    """Return the arithmetic mean, or 0 when the list is empty."""
    if not marks:
        return 0
    return sum(marks) / len(marks)


def grade_from_average(average):
    """Return an illustrative grade for a numeric average."""
    if average >= 90:
        return "A"
    if average >= 75:
        return "B"
    if average >= 60:
        return "C"
    if average >= 40:
        return "D"
    return "F"


def main():
    print("STUDENT MARKS SUMMARY")
    print("-" * 55)

    averages = []
    for name, marks in students.items():
        average = calculate_average(marks)
        averages.append(average)
        print(
            f"{name:10} marks={str(marks):16} "
            f"average={average:5.1f} grade={grade_from_average(average)}"
        )

    if averages:
        class_average = sum(averages) / len(averages)
        print("-" * 55)
        print(f"Class average: {class_average:.1f}")


if __name__ == "__main__":
    main()
