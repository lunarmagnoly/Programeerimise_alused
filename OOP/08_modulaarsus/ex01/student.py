"""Student class with student name and grades."""
from course import Course


class Student:
    """Student class, do not change."""

    def __init__(self, name: str):
        """ Student constructor. """
        self.__name = name
        self.__id = None
        self.grades = []

    def __repr__(self) -> str:
        """ Return student's name. """
        return self.__name

    def set_id(self, id: int):
        """Set student id if it is not set yet."""
        if self.__id is None:
            self.__id = id

    def get_id(self) -> int:
        """ Return student's id """
        return self.__id

    def get_grades(self) -> list[tuple[Course, int]]:
        """Return list of (course, grade) tuples."""
        return self.grades

    def get_average_grade(self):
        """Return average grade or -1 if no grades."""
        if len(self.grades) == 0:
            return -1

        total = 0
        for course, grade in self.grades:
            total += grade

        return total / len(self.grades)