# A package is a folder used to organize related Python modules (Python files)
# into a structured folder

# Packages help keep large projects organized by seperating related code into 
# different modules and folders.

# 1. First Way

from ecommerce import shipping
shipping.calc_shipping()

# 2. Second Way

from ecommerce.shipping import calc_shipping


