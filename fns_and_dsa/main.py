class Product():
	def __init__(a, name, price, quantity):
		a.name = name
		a.price = price
		a.quantity = quantity

	def calculate_total_value(a):
		return a.quantity * a.price
		
my_product = Product("cake", 1000, 5) 
print(my_product.calculate_total_value())		

"""
class Student:
	def __init__(b, name, age):
		b.name = name
		b.age = age
	def display_details(b):
		return f"{b.name} {b.age}"

my_student = Student("Natasha", "21")
print(my_student.display_details())
"""

