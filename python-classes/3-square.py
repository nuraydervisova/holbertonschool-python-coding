#!/usr/bin/python3
"""Defines a Square class with private size attribute,
getter/setter, and area method.
"""


class Square:
    """Square class with size property and area calculation."""

    def __init__(self, size=0):
        self.size = size  # setter çağırılır, yoxlama burada edilir

    @property
    def size(self):
        """Retrieve the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size attribute with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size * self.__size

