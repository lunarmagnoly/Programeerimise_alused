"""School class which stores information about courses and students."""
from student import Student
from course import Course


class School:
    """School class, do not change."""

    def __init__(self, name):
        """ Initialize school with a name and empty list of students and courses. """
        self.name = name
        self.students = []
        self.courses = []


    def add_course(self, course: Course):
        """ Add new course to school."""
        if course not in self.courses:
            self.courses.append(course)

    def add_student(self, student: Student):
        """ Add new student to school. """
        if student not in self.students:
            self.students.append(student)
            student.set_id(len(self.students))

    def add_student_grade(self, student: Student, course: Course, grade: int):
        """ Add new student's grade to school. """
        if student in self.students and course in self.courses:
            student.grades.append((course, grade))
            course.grades.append((student, grade))

    def get_students(self) -> list[Student]:
        """ Request student info."""
        return self.students

    def get_courses(self) -> list[Course]:
        """ Request course info. """
        return self.courses

    def get_students_ordered_by_average_grade(self) -> list[Student]:
        """ Get students list ordered by average grade """
        return sorted(self.students, key=lambda s: s.get_average_grade(), reverse=True)