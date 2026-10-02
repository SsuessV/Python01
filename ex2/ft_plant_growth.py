class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age_days = age

    def grow(self):
        self.height += 0.8
    
    def age(self):
        self.age_days += 1

print("=== Garden Plant Growth ===")

rose = Plant("Rose", 25.0, 30)

print(f"{rose.name}: {round(rose.height, 1)}cm, {rose.age_days} days old")

starting_height = rose.height

for day in range(1, 8):
    print(f"=== Day {day} ===")
    rose.grow()
    rose.age()
    print(f"{rose.name}: {rose.height:.1f}cm, {rose.age_days} days old")

total_growth = rose.height - starting_height
print(f"Growth this week: {round(total_growth, 1)}cm")