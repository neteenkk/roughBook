# For every mutable reference field, create a separate copy when deep cloning.
# In Java, immutable means: once the object is created, its internal state cannot be changed.
# eg: String, Integer, Float, Long, Double, Boolean
# eg of Mutable : ArrayList, LinkedList, HashMap, HashSet, StringBuilder

from abc import ABC, abstractmethod

class EnemyRegister(ABC):
    @abstractmethod
    def clone(self):
        pass

class Enemy(EnemyRegister):
    def __init__(self, type, health, speed, armored, weapon, inventory):
        self.type = type
        self.health = health
        self.speed = speed
        self.armored = armored
        self.weapon = weapon
        self.inventory = list(inventory)

    def clone(self):
        return Enemy(self.type, self.health, self.speed, self.armored, self.weapon, list(self.inventory))

    def add_item(self, item):
        self.inventory.append(item)

    def set_health(self, health):
        self.health = health

    def print_stats(self):
        print(f"{self.type} | [Health: {self.health}, Speed: {self.speed}, Armored: {self.armored}, Weapon: {self.weapon}, Inventory: {self.inventory}]")

class EnemyRegistry:
    def __init__(self):
        self._prototypes = {}

    def register(self, key, protoype):
        self._prototypes[key] = protoype

    def get(self, key):
        prototype = self._prototypes.get(key)
        if prototype is None:
            raise ValueError(f"No protoype registered for {key}")
        return prototype.clone()


if __name__ == "__main__":
    registry = EnemyRegistry()
    registry.register("flying", Enemy("FlyingEnemy", 100, 12.0, False, "Laser", ["Speed Boost"]))
    registry.register("armored", Enemy("ArmoredEnermy", 100, 46.0, True, "Canon", ["Shiled,  Helmet"]))

    e1 = registry.get("flying")
    e2 = registry.get("flying")
    e2.set_health(10)
    e2.add_item("Bomb")

    e3 = registry.get("armored")
    e1.print_stats()
    e2.print_stats()
    e3.print_stats()