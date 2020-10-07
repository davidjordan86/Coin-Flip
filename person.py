# Person class: responsible for holding the name and side of coin that person picked
class Person:

    # Two variables must be declared when a person is created: name and side
    # Note: latest python supports strongly typed variables as seen here
    # both name and side are declared as strings, this can help with debugging.
    def __init__(self, name: str, chosen_side: str):
        self.name = name
        self.chosen_side = chosen_side
    
    # Using decorators to assign setter and getter functions
    # This returns the private variable _side
    # Note: apprently in python nothing is actually private?
    # Assigning a variable as private seems to be a suggestion/syntatic sugar
    @property
    def side(self):
        return self._chosen_side

    @side.setter
    def side(self, chosen_side):
        self._chosen_side = chosen_side
        