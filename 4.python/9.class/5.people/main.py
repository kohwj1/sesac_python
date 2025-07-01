#import person
from person import Person
from student import Student
from employee import Employee

alice = Person('Alice',23)
alice.greet()
bob = Person('Bob',24)
bob.greet()

bob.name = 'BOB'
bob.greet()

tom = Student('Tom',20, "S123123")
tom.greet()
tom.study()

charlie = Employee('Charlie',30,'Samsung')
charlie.greet()
charlie.work()