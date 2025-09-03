class Student:
    # Static variable to count the number of students
    count = 0

    def __init__(self, name=None, age=None, course=None, hometown=None):
        # Initializing public and private attributes
        self.Name = name
        self.Age = age
        self.__Course = course  # Private attribute
        self.__ID = None
        self.Hometown = hometown 

        # If all arguments are passed, register the student
        if name and age and course and hometown:
            self.register()

    # Getters for the attributes
    def get_name(self):
        return self.Name

    def get_age(self):
        return self.Age

    def get_course(self):
        return self.__Course

    def get_hometown(self):
        return self.Hometown

    # Register the student and return the ID
    def register(self):
        Student.count += 1
        self.__ID = Student.count
        return self.__ID

    # Private method to update the name
    def __update_name(self, name):
        self.Name = name

    # Protected method to update the age
    def _update_age(self, age):
        self.Age = age


