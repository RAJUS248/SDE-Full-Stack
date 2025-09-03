
class Customer:
    __slots__ = ['name', 'age']
                 
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._location = "HSR" # private
        self.__rating = 4.5 # protected

    def add_to_cart(self, item_name):
        print(f"order placed for {item_name}")


customer1 = Customer("mahesh", 18) 
# customer1 is the object 
# Customer is the class 

customer1.add_to_cart("pizza")
customer1.add_to_cart("pasta")

customer1.cusrrent_age = 18
customer1.full_name = "mahesh"

print(f"customer name is {customer1.name} and age is = {customer1.age}")


customer2 = Customer("sangeeta", 18)
customer2.add_to_cart("roti")



customer3 = Customer("santosh", 20)
customer3.add_to_cart("rice")
