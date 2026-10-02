class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")

plants = [
    Plant("Rose", 14.0, 26),
    Plant("Dandelion", 20.1, 30),
    Plant("Moogunghwa", 10.10, 100),
    Plant("Mokhwa", 5.7, 29),
    Plant("Gaenari", 50.4, 20)
]

print("=== Plant Factory Output ===")
for plant in plants:
    print("Created:", end=" ")
    plant.show()