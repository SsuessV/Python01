class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = height
        self._age_days = age

    def show(self) -> None:
        print(f"{self._name}: "
              f"{round(self._height, 1)}cm, {self._age_days} days old")

    def grow(self) -> None:
        self._height += 2.1

    def age(self) -> None:
        self._age_days += 1


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color = color

    def show(self) -> None:
        super().show()
        print(f" Color: {self._color}")

    def bloom(self) -> None:
        print(f" {self._name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, height: float,
                 age: int, trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter}cm")

    def produce_shade(self) -> None:
        print(f"Tree {self._name} now produces a shade of "
              f"{self._height}cm long and {self._trunk_diameter}cm wide.")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str, nutritional_value: int) -> None:
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self._harvest_season}")
        print(f" Nutritional value: {self._nutritional_value}")

    def age(self) -> None:
        super().age()
        self._nutritional_value += 1

    def grow(self) -> None:
        super().grow()


print("=== Garden Plant Types ===")
print("=== Flower")
flower = Flower("Rose", 15.0, 10, "red")
flower.show()
print(" Rose has not bloomed yet")
print("[asking the rose to bloom]")
flower.show()
flower.bloom()

print()
print("=== Tree")
tree = Tree("Oak", 200.0, 365, 5.0)
tree.show()
print("[asking the oak to produce shade]")
tree.produce_shade()
print()
print("=== Vegetable")
veggie = Vegetable("Tomato", 5.0, 10, "April", 0)
veggie.show()
print("[make tomato grow and age for 20 days]")
for _ in range(20):
    veggie.age()
    veggie.grow()
veggie.show()
