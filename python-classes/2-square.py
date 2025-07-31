#!/usr/bin/python3
"""Defines a Square class with size validation and area calculation."""


class Square:
    """Square class with private size attribute and area method."""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the current square area."""
        return self.__size * self.__size
