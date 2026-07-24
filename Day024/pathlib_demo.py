import os
from pathlib import Path

for p in Path().iterdir():
    print(p)

my_dir = Path("Directory_1")
my_file = Path("file_1_.txt")

new_file = my_dir / "new_file.txt"
new_file2 = my_dir.joinpath("new_file2.txt")

print(my_dir.exists())
print(my_file.exists())

print(my_dir.stem)
print(my_file.stem)

print(my_dir.suffix)
print(my_file.suffix)

print(new_file)
print(new_file2)