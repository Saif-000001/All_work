class User:
    def __init__(self, name , age, money) -> None:
        self._name = name
        self._age = age
        self.__money = money
    
    # without private getter
    @property
    def age(self):
        return self._age
    
    @property
    def salary(self):
        return self.__money
    
    # setter
    # value changing method in class
    @salary.setter
    def salary(self, value):
        if value<0:
            return 'salary cannot be negative'
        self.__money+=value



m = User('msi', 23, 0)

m.salary = 700
print(m.age)

print(m.salary)



# class GridPoint:
#     def __init__(self, x, y):  
#         self.x = x  
#         self.y = y  
  
#     def __add__(self, other):  	# Overloading + operator
#         return GridPoint(self.x + other.x, self.y + other.y)
  
#     def __str__(self):  		# Overloading "to string" (for printing)
#         string = str(self.x)  
#         string = string + ", " + str(self.y)  
#         return string  
#     def __gt__(self, other):
#              	# Overloading > operator (Greater Than)
#        	    return self.x > other.x   

# point1 = GridPoint(3, 5) 
# point2 = GridPoint(-1, 4)
# point3 = point1 + point2  	# Add two points using __add__() method
# print(point3)  				# Print the attributes using __str__() method
# if point1 > point2:  		# Compares using __gt__() method
#    print('point 1 is greater than point 2')  

class A:
    def first(self):
        print("First function of class A")

    def second(self):
        print('Second function of class A')

# # Derived Class
# class B(A):
#     # Overriden Function
#     def first(self):
#         print("Redefined function of class A in class B")

#     def display(self):
#         print('Display Function of Child class')

# # Driver Code
# if(__name__ == "__main__"):
#     # Creating child class object
#     child_obj = B()
    
#     # Calling the overridden method
#     print("Method Overriding\n")
#     child_obj.first()
    
#     # Calling the original Parent class method
#     # Using parent class object.
#     A().first()
