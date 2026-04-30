"""Course class with name and grades."""
from student import Student


class Course:
    """Course class, do not change."""

    def __init__(self, name: str):
        """Initialize course with a name and empty list of grades."""
        self.name = name
        self.grades = []

    def __repr__(self):
        """Return course name as string representation."""
        return self.name

    def get_grades(self) -> list[tuple[Student, int]]:
        """Return list of (student, grade) tuples."""
        return self.grades

    def get_average_grade(self) -> float:
        """Return average grade of the course or -1 if no grades."""
        if len(self.grades) == 0:
            return -1

        total = 0
        for student, grade in self.grades:
            total += grade

        return total / len(self.grades)