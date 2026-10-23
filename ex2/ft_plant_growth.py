class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age_days = age

    def show(self) -> None:
        print(f"{self.name}: "
              f"{round(self.height, 1)}cm, {self.age_days} days old")

    def grow(self) -> None:
        self.height += 0.8

    def age(self) -> None:
        self.age_days += 1


print("=== Garden Plant Growth ===")

rose = Plant("Rose", 25.0, 30)
rose.show()

starting_height = rose.height

for day in range(1, 8):
    print(f"=== Day {day} ===")
    rose.grow()
    rose.age()
    rose.show()

total_growth = rose.height - starting_height
print(f"Growth this week: {round(total_growth, 1)}cm")
