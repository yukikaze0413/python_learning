class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print("Hello, my name is " + self.name)

person1 = Person("John")
person1.talk() # Output: Hello, my name is John
