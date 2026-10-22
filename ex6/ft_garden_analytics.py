class Plant:

    class Statistics:
        
        
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = height
        self._age_days = age

    def show(self) -> None:
        print(f"{self._name}: "
              f"{round(self._height, 1)}cm, {self._age_days} days old")

    @staticmethod
        def valid_age(age: int) -> None:
            if age > 365:
                print(f"Is {age} days more than a year? -> True")
            else:
                print(f"Is {age} days more than a year -> False")

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

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter}cm")

    def produce_shade(self) -> None:
        print(f"Tree {self._name} now produces a shade of "
              f"{self._height}cm long and {self._trunk_diameter}cm wide.")


def print_stats(plant: Plant) -> None:
    print(f" [statistics for {plant.name}]")
    print(f"Stats: {plant._} grow, {plant._age_count} age, {plant._show_count} show")



print("=== Garden statistics ===")
print("=== Check year-old")
Plant.check_age(30)
Plant.check_age(400)
print()
print("=== Flower")
flower = Flower("Rose", 15.0, 10, "red")
flower.show()
print(" Rose has not bloomed yet")

print("[asking the rose to grow and bloom]")
