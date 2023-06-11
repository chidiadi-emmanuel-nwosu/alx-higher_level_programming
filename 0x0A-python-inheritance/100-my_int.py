#!/usr/bin/python3
"""MyInt module
"""


class MyInt(int):
    """MyInt class"""

    def __eq__(self, others):
        """equality magic method"""
        return super().__ne__(others)

    def __ne__(self, others):
        """equality magic method"""
        return super().__eq__(others)
