# There are two ways to import a module
# 1. First Way

import converters
print(converters.kg_to_lbs(70))

# 2. Second Way

from converters import kg_to_lbs
print(kg_to_lbs(100))

# Another example

from utils import find_max

numbers = [10, 3, 6, 2]
maximum = find_max(numbers)
print(maximum)

