from tiere import Tiere

class Prey(Tiere):
        def fluechten(self):
            print(f"{self.name} flüchtet")

class Predator(Tiere):
        def jagen(self):
            print(f"{self.name} jägt")

class Rabbit(Prey):
         pass

class Hawk(Predator):
         pass

class Fish(Prey, Predator):
         pass

rabbit = Rabbit("Horst der Hase")
hawk = Hawk("Tony Hawk")
fish = Fish("Peter der Fisch")



fish.schlafen()
rabbit.fluechten()
hawk.jagen()
