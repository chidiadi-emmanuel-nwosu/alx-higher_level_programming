#!/usr/bin/python3
"""LockedClass module
"""


class LockedClass:
    """creates a locked class with no attributes
    """

    def __setattr__(self, name, value):
        """prevents the user from dynamically creating
           new instance attributes, except if the new
           instance attribute is called first_name
        """

        if name == "first_name" and isinstance(value, str):
            super().__setattr__(name, value)
        else:
            raise AttributeError(
                f"'{self.__class__.__name__}' object has no attribute '{name}'"
            )
