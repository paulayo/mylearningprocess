#### INHERITANCE

class Animal:
    def __init__(self,name):
        self.name = name

    def speak(self):    # Abstract method
        raise NotImplementedError('Subclass must implement abstract method')


class Dog(Animal):
    def speak(self):
        return self.name + ' says Whoofs'

class Cat(Animal):
    def speak(self):
        return self.name + ' says Meow'

whisky = Dog('whisky')
kitty = Cat('kitty')

(whisky.speak())
(kitty.speak())

class Animal:
    def __init__(self,name,legs):
        self.name = name
        self.legs = legs

class Bear(Animal):
    def __init__(self,name,legs=4,hibernate='yes'):
        Animal.__init__(self,name,legs)
        self.hibernate = hibernate

scary = Bear('Scary')
(scary.name)
(scary.legs)
(scary.hibernate)


################## MULTIPLE INHERITANCE ##################

class Car:
    def __init__(self,wheels=4):
        self.wheels = wheels

class Gasoline(Car):
    def __init__(self,engine='gasoline',tank_cap=20):
        Car.__init__(self)
        self.engine = engine
        self.tank_cap = tank_cap
        self.tank = 0

    def refuel(self):
        self.tank += self.tank_cap

class Electric(Car):
    def __init__(self,engine='electric',KWh_cap=60):
        Car.__init__(self)
        self.engine = engine
        self.KWh_cap = KWh_cap
        self.KWh = 0

    def recharge(self):
        self.KWh += self.KWh_cap



class Hybrid(Gasoline,Electric):
    def __init__(self,engine='hybrid',tank_cap=11,KWh_cap=5):
        Gasoline.__init__(self,engine,tank_cap)
        Electric.__init__(self,engine,KWh_cap)

    def __str__(self):
        return f'The engine is {self.engine}'


gWagon = Hybrid()
(gWagon.tank)
(gWagon.KWh)
(gWagon.__str__)
(gWagon.KWh_cap)
gWagon.refuel()
(gWagon.tank_cap)

######################## METHOD RESOLUTION ORDER ######

class A:
    num = 4

class B(A):
    pass

class C(A):
    num = 5

class D(B,C):
    pass

(D.num)


##### MRO -----------> super()

class MyBaseClass():
    def __init__(self,x,y):
        self.x = x
        self.y = y

class MyDerivedClass(MyBaseClass):
    def __init(self,x,y,z):
        super().__init__(x,y)
        self.z = z

### ------------------------------------##
# the super() built-in-function also helps in managing the method order resolution
class A:
    def truth(self):
        return 'All numbers are even'

class B(A):
    pass

class C(A):
    def truth(self):
        return 'Some numbers are even'

class D(B,C):
    def truth(self,num):
        if num%2 == 0:
            return A.truth(self)
        else:
            return super().truth()

d = D()
print(d.truth(6))
print(d.truth(5))
