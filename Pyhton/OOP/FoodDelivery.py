class Customer:
    def place_order(self, item):
        return f"{self.name} placed an order for {item}"

# Creating an object
cust1 = Customer()

cust1.name = "mahesh"
print(cust1.name)

cust2 = Customer()
cust2.age = 18

print(cust2.age)
print(cust1.age)