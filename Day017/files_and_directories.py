from pathlib import Path

path = Path("ecommerce")
print(path.exists())

path = Path()
for file in path.glob("*.py"):
    print(file)

for file in path.glob("*"):
    print(file)