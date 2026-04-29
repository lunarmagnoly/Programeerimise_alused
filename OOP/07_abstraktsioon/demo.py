from abc import ABC

class Animal(ABC):

    def sleep(self):
        print("I am going to sleep.")

    def speak(self):
        pass

class Human(Animal):

    def speak(self):
        print("I can talk.")

class Snake(Animal):

    def speak(self):
        print("I can hiss.")

class Dog(Animal):

    def speak(self):
        print("I can bark.")

class Lion(Animal):

    def speak(self):
        print("I can roar.")

human = Human()
human.speak()

snake = Snake()
snake.speak()

dog = Dog()
dog.speak()

lion = Lion()
lion.speak()