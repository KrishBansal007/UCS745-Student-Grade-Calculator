"""A small command-line student grade calculator."""

def calculate_average(marks):
    """Return the arithmetic mean of a non-empty list of marks."""
    if not marks:
        raise ValueError("At least one mark is required.")
    if any(mark < 0 or mark > 100 for mark in marks):
        raise ValueError("Marks must be between 0 and 100.")
    return sum(marks) / len(marks)


def get_grade(average):
    """Convert an average mark into a letter grade."""
    if average >= 90:
        return "A"
    if average >= 80:
        return "B"
    if average >= 70:
        return "C"
    if average >= 60:
        return "D"
    return "F"


def main():
    print("STUDENT GRADE CALCULATOR")
    print("------------------------")
    name = input("Enter student name: ").strip()
    if not name:
        print("Student name cannot be empty.")
        return

    raw_marks = input("Enter marks separated by spaces (0-100): ").split()
    try:
        marks = [float(value) for value in raw_marks]
        average = calculate_average(marks)
    except ValueError as error:
        print(f"Input error: {error}")
        return

    print("\nRESULT")
    print(f"Student: {name}")
    print(f"Number of subjects: {len(marks)}")
    print(f"Average: {average:.2f}")
    print(f"Grade: {get_grade(average)}")


if __name__ == "__main__":
    main()
