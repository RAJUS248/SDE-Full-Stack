import sys

sugar = 2
water = 1
print("Making tea with", sugar, "tsp sugar and", water, "cup water")

num1 = 1099999999999999999999999999999999999999999999999999
num2 = 2088888888888888888888888888888888888888888888888888888
ans = num1 + num2
print(ans)

x = 5888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
print(type(x))                # <class 'int'>
print(isinstance(x, int))     # True
print("Integer 5 takes:", sys.getsizeof(x), "bytes")

y = 1.23233333333333333333333333333333333333333333333333333333333333333333
print(type(y))      
print("float 1.2 takes:", sys.getsizeof(y), "bytes")          

z = "maheshasdfadsfasdfasdadsfsadfasdfasdfadsfsamaheshasdfadsfasdfasdadsfsadfasdfasdfadsfsadfasdfasdfasfasdfadsmaheshasdfadsfasdfasdadsfsadfasdfasdfadsfsadfasdfasdfasfasdfadsmaheshasdfadsfasdfasdadsfsadfasdfasdfadsfsadfasdfasdfasfasdfadsmaheshasdfadsfasdfasdadsfsadfasdfasdfadsfsadfasdfasdfasfasdfadsmaheshasdfadsfasdfasdadsfsadfasdfasdfadsfsadfasdfasdfasfasdfadsmaheshasdfadsfasdfasdadsfsadfasdfasdfadsfsadfasdfasdfasfasdfadsmaheshasdfadsfasdfasdadsfsadfasdfasdfadsfsadfasdfasdfasfasdfadsmaheshasdfadsfasdfasdadsfsadfasdfasdfadsfsadfasdfasdfasfasdfadsmaheshasdfadsfasdfasdadsfsadfasdfasdfadsfsadfasdfasdfasfasdfadsmaheshasdfadsfasdfasdadsfsadfasdfasdfadsfsadfasdfasdfasfasdfadsmaheshasdfadsfasdfasdadsfsadfasdfasdfadsfsadfasdfasdfasfasdfadsmaheshasdfadsfasdfasdadsfsadfasdfasdfadsfsadfasdfasdfasfasdfadsmaheshasdfadsfasdfasdadsfsadfasdfasdfadsfsadfasdfasdfasfasdfadsmaheshasdfadsfasdfasdadsfsadfasdfasdfadsfsadfasdfasdfasfasdfadsmaheshasdfadsfasdfasdadsfsadfasdfasdfadsfsadfasdfasdfasfasdfadsmaheshasdfadsfasdfasdadsfsadfasdfasdfadsfsadfasdfasdfasfasdfadsmaheshasdfadsfasdfasdadsfsadfasdfasdfadsfsadfasdfasdfasfasdfadsmaheshasdfadsfasdfasdadsfsadfasdfasdfadsfsadfasdfasdfasfasdfadsdfasdfasdfasfasdfads"
print(type(z))    
print("str mahesh takes:", sys.getsizeof(z), "bytes")  

result = True
print(type(result))
print("boolean true takes:", sys.getsizeof(result), "bytes")

print(5 + 2.0)      # 7.0 (int + float = float)
print("hi" + "5")   # "hi5"
print("hi" + 5)   