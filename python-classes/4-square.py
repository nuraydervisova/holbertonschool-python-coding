#!/usr/bin/python3
"""Defines a Square class with size, area, and printing capabilities."""


class Square:
    """Square class with size property, area and print methods."""

    def __init__(self, size=0):
        self.size = size  # Setter çağırılır, yoxlamalar burada edilir

    @property
    def size(self):
        """Get the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size, with type and value validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return current square area."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with the character # to stdout.
        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print()
            return
        for _ in range(self.__size):
            print("#" * self.__size)
