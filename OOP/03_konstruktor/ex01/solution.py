"""Constructor exercise."""


class Empty:
    """An empty class without constructor."""


class Person:
    """Represent person with firstname, lastname and age."""

    def __init__(self):
        """Initialize a person."""
        self.firstname = ""
        self.lastname = ""
        self.age = 0


class Student:
    """Represent student with firstname, lastname and age."""

    def __init__(self, firstname: str, lastname: str, age: int):
        """
        Initialize a student.

        :param firstname: Student's first name
        :param lastname: Student's last name
        :param age: Student's age
        """
        self.firstname = firstname
        self.lastname = lastname
        self.age = age


if __name__ == '__main__':
    # empty usage
    empty = Empty()
    # 3 x person usage
    person1 = Person("M", "L", 30)
    person2 = Person("L", "T", 20)
    person3 = Person("K", "L", 30)
    # 3 x student usage
    student1 = Student("M", "L", 30)
    student2 = Student("L", "T", 20)
    student3 = Student("K", "L", 30)
