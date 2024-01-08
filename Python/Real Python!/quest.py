class Cat:
    def __init__(self, name, cute_level):
        self.name = name 
        self.cute_level = cute_level

    def add_cute_level(self, cute_level):    
        if self.cute_level + cute_level <= 10:
            self.cute_level += cute_level


        
Cat_01 = Cat('Chanom', 8)
Cat_02 = Cat('Loma', 3)

Cat_01.add_cute_level(2)
Cat_01.add_cute_level(3)

print(Cat_01.name, Cat_01.cute_level)
print(Cat_02.name, Cat_02.cute_level)