"""Simple class."""


class Student:
    """Contains student name and status."""

    def __init__(self, name):
        """Initialize student with name and default status."""
        self.name = name
        self.finished = False

    def set_name(self, name):
        """Set student`s name."""
        self.name = name

    def set_status(self, finished):
        """Set student`s status."""
        self.finished = finished

    def get_status(self):
        """Get student`s status."""
        return self.finished