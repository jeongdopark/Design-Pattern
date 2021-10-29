
'''
Solid Principles
single-responsibilit 단일 책임 원칙
모든 함수나 클래스는 하나에 part에 대해서 책임을 가져야 한다.
'''

class Cat:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def eat(self):
        print("eating..")
    
    def walk(self):
        print("walking..")
    
    def speak(self):
        print("meow~")
    
    def repr(self):
        return f"name : {self.name}, age : {self.age}"

    def print(self): # Cat Class에 부합하지 않는 기능이다.
        print(f"name : {self.name}, age : {self.age}")

kitty = Cat(3, "kitty")
kitty.eat()
kitty.walk()
kitty.speak()
print(kitty.repr())
kitty.print()
