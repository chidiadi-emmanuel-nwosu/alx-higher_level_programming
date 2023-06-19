#!/usr/bin/python3
"""base module
"""
import csv
import json
import os


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initializes the class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or not len(list_dictionaries):
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of
           list_objs to a file
        """
        new = cls.to_json_string(
                [obj.to_dictionary() for obj in list_objs]
                if list_objs else None
            )

        with open(f"{cls.__name__}.json", 'w', encoding="utf-8") as file:
            file.write(new)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation"""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        new = cls(1, 1) if cls.__name__ == "Rectangle" else cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = f"{cls.__name__}.json"

        if not os.path.exists(filename):
            return []

        with open(filename, encoding="utf-8") as file:
            new = cls.from_json_string(file.read())

        ins = [cls.create(**new[i]) for i in range(len(new))]
        return ins

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """writes the string representation of
           list_objs to a csv file
        """
        filename = f"{cls.__name__}.csv"

        with open(f"{cls.__name__}.csv", 'w', encoding="utf-8") as file:
            if list_objs is None or len(list_objs) == 0:
                file.write("[]")
            else:
                if filename == "Rectangle.csv":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]

                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()

                new = (
                        [obj.to_dictionary() for obj in list_objs]
                        if list_objs else None
                )
                for i in new:
                    writer.writerow(i)

    @classmethod
    def load_from_file_csv(cls):
        """returns a list of instances"""
        filename = f"{cls.__name__}.csv"

        if not os.path.exists(filename):
            return []

        new = []
        with open(filename, encoding="utf-8") as file:
            reader = csv.DictReader(file)
            new = [dict([k, int(v)] for k, v in d.items()) for d in reader]

        ins = [cls.create(**new[i]) for i in range(len(new))]
        return ins
