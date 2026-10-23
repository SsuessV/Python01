class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = 0.0
        self._age_days = 0
        self.set_height(height)
        self.set_age(age)

    def show(self) -> None:
        print(f"{self._name}: "
              f"{round(self._height, 1)}cm, {self._age_days} days old")

    def set_height(self, height: float) -> None:
        if height >= 0:
            self._height = height
        else:
            print(f"{self._name}: Error, height can't be negative")

    def set_age(self, age: int) -> None:
        if age >= 0:
            self._age_days = age
        else:
            print(f"{self._name}: Error, age can't be negative")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age_days


plant = Plant("Rose", 15.0, 10)

print("=== Garden Security System ===")
print("Plant created:", end=" ")
plant.show()
print()
plant.set_height(25)
print(f"Height updated: {plant.get_height()}cm")
plant.set_age(30)
print(f"Age updated: {plant.get_age()} days")
print()
plant.set_height(-42)
print("Height update rejected")
plant.set_age(-18)
print("Age update rejected")
print()
print(f"Current state: {plant._name}: "
      f"{plant.get_height():.1f}cm, {plant.get_age()} days old")
