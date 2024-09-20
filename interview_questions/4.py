#filter() and map()
numbers = [4, 2, 1, 6, 9, 7]
def square(x):
    return x*x

result = list(map(square, numbers))
print(result)


results = [square(x) for x in numbers]
print(results)
