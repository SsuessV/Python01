class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age_days = age

    def show(self) -> None:
        print(f"{self.name}: "
              f"{round(self.height, 1)}cm, {self.age_days} days old")


plants = [
    Plant("Rose", 14.0, 26),
    Plant("Dandelion", 20.1, 30),
    Plant("Moogunghwa", 10.10, 100),
    Plant("Mokhwa", 5.7, 29),
    Plant("Gaenari", 50.4, 20)
]

print("=== Plant Factory Output ===")
for item in plants:
    print("Created:", end=" ")
    item.show()
