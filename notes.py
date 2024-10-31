class Dog: 
    species = "canies familiaris"
    fetch_count = 0

    def __init__(self, n = "", a = 0): #'self' is the same as 'this' in java
        self.name = n
        self.age = a

    def __str__(self):
        s = f"{self.name} is {self.age} years old"
        return s

    def play_fetch(self, num_fetch = 0):
        self.fetch_count += num_fetch


logan = Dog("logan", 8)
becker = Dog("becker", 4)
kepa = Dog("kepa", 4)

print(logan.fetch_count)
print(becker)
print(Dog())

logan.play_fetch(5)

print(logan.fetch_count)