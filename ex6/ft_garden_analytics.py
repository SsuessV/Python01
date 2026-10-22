class Plant:

    class Statistics:
        def __init__(self) -> None:
            self._grow_count = 0
            self._age_count = 0
            self._show_count = 0
        
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = height
        self._age_days = age
        self._stats = Plant.Statistics()

    def show(self) -> None:
        print(f"{self._name}: "
              f"{round(self._height, 1)}cm, {self._age_days} days old")
        self._stats._show_count += 1

    @staticmethod
    def valid_age(age: int) -> None:
        if age > 365:
            print(f"Is {age} days more than a year? -> True")
        else:
            print(f"Is {age} days more than a year -> False")

    @classmethod
    def create_instance(cls) -> "Plant":
        anonymous = cls("Unknown plant", 0.0, 0)
        return anonymous


    def grow(self) -> None:
        self._height += 2.1
        self._stats._grow_count += 1

    def age(self) -> None:
        self._age_days += 1
        self._stats._age_count += 1


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color = color

    def show(self) -> None:
        super().show()
        print(f" Color: {self._color}")

    def bloom(self) -> None:
        print(f" {self._name} is blooming beautifully!")


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age, color)
        self._seed_count = 0

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self._seed_count}")

    def bloom(self) -> None:
        print(f" {self._name} is blooming beautifully!")

class Tree(Plant):
    def __init__(self, name: str, height: float,
                 age: int, trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter
        self._shade_count = 0

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter}cm")

    def produce_shade(self) -> None:
        self._shade_count += 1
        print(f"Tree {self._name} now produces a shade of "
              f"{self._height}cm long and {self._trunk_diameter}cm wide.")


def print_stats(plant: Plant) -> None:
    print(f" [statistics for {plant._name}]")
    print(f"Stats: {plant._stats._grow_count} grow, "
          f"{plant._stats._age_count} age, "
          f"{plant._stats._show_count} show")


print("=== Garden statistics ===")
print("=== Check year-old")
Plant.valid_age(30)
Plant.valid_age(400)
print()
print("=== Flower")
flower = Flower("Rose", 15.0, 10, "red")
flower.show()
print(" Rose has not bloomed yet")
print_stats(flower)
print("[asking the rose to grow and bloom]")
for i in range(4):
    flower.grow()
flower.show()
flower.bloom()
print_stats(flower)
print()
print("=== Tree")
tree = Tree("Oak", 200.0, 365, 5.0)
tree.show()
print_stats(tree)
print(f"{tree._shade_count} shade")
print("[asking the oak to produce shade]")
tree.produce_shade()
print_stats(tree)
print(f"{tree._shade_count} shade")
print()
print("=== Seed")
seed = Seed("Sunflower", 80.0, 45, "yellow")
print("Sunflower has not bloomed yet")

print("[make sunflower grow, age and bloom]")

print("Sunflower is blooming beautifully!")

print()
print("=== Anonymous")
anonymous = Plant.create_instance()
anonymous.show()