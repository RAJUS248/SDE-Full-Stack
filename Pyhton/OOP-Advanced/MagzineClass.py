from LibraryItemClass import LibraryItem

class Magzine(LibraryItem):

    def __init__(self, count, id, name, publisher, issuenumber):
        super().__init__(count, id)

        self.name = name
        self.publisher = publisher
        self.issuenumber = issuenumber
    
    def display_info(self):
        super().display_info()
        print(f"Issue Number: {self.issuenumber}")

    def check_out(self):
        return super().check_out()