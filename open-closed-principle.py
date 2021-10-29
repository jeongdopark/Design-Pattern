'''
확장에 대해선 개방, 수정에 대해선 폐쇄.
code behavior에 대한 principle이다.
'''

class Animal():
    def __init__(self, type):
        self.type = type

def hey(animal):
    if animal.type == 'Cat':
        print('meow')
    elif animal.type == 'Dog':
        print('bark')

bingo = Animal('Dog')
kitty = Animal('Cat')

# hey(bingo)
# hey(kitty)

'''
앞으로 다른 동물들을 추가하게 되면 hey 함수의 수정이 필요하다.
open-closed (확장에 대해선 개방, 수정에 대해선 폐쇄)
확장 -> 동물의 종류를 늘리는 것.
수정 -> hey 함수의 수정
open-closed에 위배되는 코드이다.
'''

class O_C_Animal():
    def speak(self): # interface method
        pass

class Cat(O_C_Animal):
    def speak(self):
        print("meow")

class Dog(O_C_Animal):
    def speak(self):
        print("bark")

def hey(animal):
    animal.speak();

bingo1 = Dog()
kitty1 = Cat()

hey(bingo1)
hey(kitty1)

'''
hey 함수를 수정하지 않고
자유롭게 동물의 종류를 확장할 수 있다.
'''
class Cow(O_C_Animal):
    def speak(self):
        print("moo")

class Sheep(O_C_Animal):
    def speak(self):
        print("meh")

cow = Cow()
sheep = Sheep()

hey(cow)
hey(sheep)
