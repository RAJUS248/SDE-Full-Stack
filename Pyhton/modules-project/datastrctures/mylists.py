class MyList:

    def __init__(self):
        self.list = []
    
    def add(self, item):
        self.list.append(item)

    def remove(self, item):
        self.list.remove(item)
    
    def print(self):
        print(self.list)

class StudentList:

    def __init__(self):
        self.list = []
    
    def add(self, item):
        self.list.append(item)
        