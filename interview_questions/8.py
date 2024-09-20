#Sort Complex Lists With sorted()

animals = [
    {"type": "dog", "name": "buddy", "age": 5},
    {"type": "cat", "name": "kitty", "age": 3},
    {"type": "dog", "name": "rocky", "age": 7},
    {"type": "fish", "name": "goldie", "age": 1},

]

sorted_animals = sorted(animals, key=lambda x: x['age'])
print(sorted_animals)