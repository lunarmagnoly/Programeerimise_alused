"""Encapsulation exercise."""


class Student:
    """Represent student with name, id and status."""

    def __init__(self, name, id):
        """Initialize a student."""
        self.__name = name
        self.__id = id
        self.__status = "Active"

    def get_id(self):
        """Get student's id."""
        return self.__id

    def set_name(self, name):
        """
        Change student's name.

        :param name: Student's name
        """
        self.__name = name

    def get_name(self):
        """Change student's name."""
        return self.__name

    def set_status(self, status):
        """
        Change student's status if status is equal "Active", "Expelled", "Finished" or "Inactive".

        :param status: Student's name
        """
        allowed_statuses = ["Active", "Expelled", "Finished", "Inactive"]

        if status in allowed_statuses:
            self.__status = status

    def get_status(self):
        """Get student's status."""
        return self.__status