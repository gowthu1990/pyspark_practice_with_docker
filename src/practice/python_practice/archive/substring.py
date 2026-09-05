def to_proper_names():
    fruits = ["apple", "banana", "orange"]
    proper_fruits = [ fruit.upper() if fruit != "banana"  else fruit for fruit in fruits ]
    print(proper_fruits)
to_proper_names()

