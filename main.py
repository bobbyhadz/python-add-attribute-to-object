# Add attributes to an Object in Python

class Employee():
    def __init__(self, name):
        self.name = name


emp1 = Employee('bobby')

setattr(emp1, 'salary', 100)
setattr(emp1, 'age', 30)

print(getattr(emp1, 'salary'))  # 👉️ 100
print(getattr(emp1, 'age'))  # 👉️ 30
print(getattr(emp1, 'name'))  # 👉️ bobby