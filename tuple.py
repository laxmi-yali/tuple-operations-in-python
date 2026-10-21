# ======== tuple ========

item1 = ("laxmi","basu","swati","nivas",("goutham",6,8,"ravi"),"basu")

print(item1)
print(type(item1))
# item1[2] = "sumyukta" # it gives error because tuple object doesn't support item assignment
print(item1)

print(len(item1))
print(item1[4]) # indexing
print(item1[-3]) # negative indexing
print(item1[4][2])
print(item1[2:4:2])

print(item1.index("swati"))
print(item1.count("basu"))

a = (10,20) 
b = (30,40)
print(a + b) # combining two tuples
print(a * 3) # replication
print(min(b))
print(max(a))

"""in tuple we can't delet individual element so if we want to delete element from tuple
we should convert it into list after that we can delet by 'del'"""


c = list(a) 
del c[1]
print(c)

print("goutham" in item1) # membership operators
print("swati" not in item1)

# ======== Problems ========
# Shoping products details
print("")
print("# ======= 1.PROBLEM =======")
print("")

product = ("laptop",50000,"Electronics","lenovo")
print(product)
print(product[3])
print(product[1])
print(product[:2])
print(len(product))

# Student Marks Management
print("")
print("# ======= 2.PROBLEM =======")
print("")

marks = (85, 90, 76, 95, 80)
print(marks)
print(max(marks))
print(min(marks))
print(sum(marks))

total = sum(marks)
number = len(marks)

average = total/number
print(average)

# Bus Ticket Booking
print("")
print("# ======= 3.PROBLEM =======")
print("")

passengers = ("Laxmi","saraswati","Shivaraj","Swati")
print("laxmi" in passengers)
print("Ravi" not in passengers)
print(passengers[0])
print(passengers[-1])
print(passengers[:3])

# Store inventory
print("")
print("# ======= 4.PROBLEM =======")
print("")

products = ("mouse","keyborad","mouse","monitor")
new_products = ("printer","speaker")
print(products.count("mouse"))
print(products.index("monitor"))
combined_products = products + new_products
print(combined_products)
print(len(combined_products))

# Warehouse Temperature Monitoring 
print("")
print("# ======= 5.PROBLEM =======")
print("")

temperatures = (24, 26 ,25, 28, 27)
print(temperatures)
print(min(temperatures))
print(max(temperatures))

for values in temperatures :
    print(values)

print(temperatures *2)



