#!/usr/bin/python3
"""square module
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        """initializes the class"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter"""
        return self.width

    @size.setter
    def size(self, value):
        """setter"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.width = value
        self.height = value

    def __str__(self):
        """returns a string"""
        return (
            f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
        )

    def update(self, *args, **kwargs):
        """asigns an argument to each attribute"""
        if args and len(args):
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
                self.height = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for k, v in kwargs.items():
                if k == 'size':
                    self.width = kwargs[k]
                    self.height = kwargs[k]
                elif hasattr(self, k):
                    setattr(self, k, v)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        keys = ['id', 'size', 'x', 'y']
        _dict = dict()

        for key in keys:
            if key == 'size':
                _dict[key] = getattr(self, 'width')
            else:
                _dict[key] = getattr(self, key)

        return _dict
