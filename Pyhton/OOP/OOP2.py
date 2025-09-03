class Customer:
    __slots__ = ['name', 'age']

    # Constructors
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def place_order(self, item):
        print(f"placed an order for {item}")

# Creating an object
cust1 = Customer("mahesh", 40)
cust1.place_order("Paneer Biryani")

cust1.fullname = "mahesh"
cust1.orderCount = 30

cust2 = Customer("sangeeta", 40)

#print(cust1.__dict__)
