#!/usr/bin/python3
"""Defines a Rectangle class with width and height properties."""


class Rectangle:
    """Rectangle class with private width and height attributes."""

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle instance with optional width and height."""
        self.width = width    # setter çağırılır, yoxlama burada edilir
        self.height = height  # setter çağırılır, yoxlama burada edilir

    @property
    def width(self):
        """Retrieve the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width attribute with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height attribute with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
