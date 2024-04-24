from collections import namedtuple
# first example "point"
point = namedtuple('Point', ['x','y'])
p = point(3,4)
print(p.x)
print(p.y)

# second examples "Car"
Car = namedtuple('Car',['make','model','year'])
c = Car('chevrolet','Gentra','2023')
print(c.make)
print(c.model)
print(c.year)

# third examples "person"
Person = namedtuple('Person',['name','age','nationality'])
p = Person('Sanjar','27','Uzbek')
print(p.name)
print(p.age)
print(p.nationality)

# fourth examples "Book"
Book = namedtuple('Book',{'title','author'})
b = Book('Shaytanat','Toxir Malik')
print(b)

# fifth examples "student"
from collections import namedtuple
from uuid import uuid4

Student = namedtuple('Student', ['name', 'id', 'grade'])

class Students:
    def __init__(self, name=None, id=None, grade=None):
        self.name = name
        self.id = uuid4()
        self.grade = grade
        
    def __str__(self):
        return f"Student Name: {self.name}, ID: {self.id}, Grade: {self.grade}"

students1 = Students('Sarvar', 'forth')
print(students1)

 

