from collections import deque
import csv

"""
A class representing a person.

Attributes:
    name (str): The name of the person.

Methods:
    __init__(name: str): Initializes an instance of the Person class with the given name.
"""
class Person:
    def __init__(self, name):
        self.name = name

       
"""
A class representing genealogical data.

Attributes:
    adjacency_list (dict): A dictionary representing the adjacency list of the genealogical data

Methods:
    __init__(): Initializes an instance of the GenealogicalData class
    add_person(person): Adds a person to the genealogical data.
    add_parent_child(parent, child): Adds a parent-child relationship to the genealogical data.
    are_biologically_related(person1, person2): Determines if two persons are biologically related.
"""
class GenealogicalData:
    def __init__(self):
        self.adjacency_list = {}

    def add_person(self, person):
        self.adjacency_list[person] = []

    def add_parent_child(self, parent, child):
        self.adjacency_list[parent].append(child)

    def are_biologically_related(self, person1, person2):
        visited = set()
        queue = deque([person1])

        while queue:
            person = queue.popleft()
            if person == person2:
                return True
            if person not in visited:
                visited.add(person)
                queue.extend(self.adjacency_list[person])

        return False

"""
A function that loads genealogical data from a CSV file.

Attributes:
    filename (str): The name of the CSV file containing the genealogical data.
"""
def load_data(filename):
    data = GenealogicalData()
    persons = {}

    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            parent_name, child_name = row
            if parent_name not in persons:
                persons[parent_name] = Person(parent_name)
                data.add_person(persons[parent_name])
            if child_name not in persons:
                persons[child_name] = Person(child_name)
                data.add_person(persons[child_name])
            data.add_parent_child(persons[parent_name], persons[child_name])

    return data, persons


if __name__=='__main__':
    data, persons = load_data('genealogical_data.csv')

    person1 = list(persons.keys())[0]
    person2 = list(persons.keys())[1]

    print(data.are_biologically_related(persons[person1], persons[person2]))
