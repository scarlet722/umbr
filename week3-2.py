class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"이름: {self.name}, 나이: {self.age}"

class Dog(Pet):
    def bark(self, n):
        for _ in range(n):
            print("bark!")

    def human_age(self):
        return self.age * 4

class Cat(Pet):
    def meow(self, n):
        for _ in range(n):
            print("meow~")

    def human_age(self):
        return self.age * 4

if __name__ == "__main__":
    dog1 = Dog("강아지", 3)

    print(dog1)
    dog1.bark(3)
    print("인간 나이:", dog1.human_age())
    cat1 = Cat("고양이", 2)
    print(cat1)
    cat1.meow(2)
    print("인간 나이:", cat1.human_age())
