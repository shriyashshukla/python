# this is for enumerate() instead of range()
#Why enumerate() is better:
# Readability: It directly gives you both index and value, making the code simpler and more readable.
# Efficiency: You don’t need to use range(len()) to get the index, which is especially useful when you don't care about just the index.

number = [45,22,14,65,97,72]
for i, num in enumerate(number):
    if num % 3 == 0 and num % 5 == 0:
        number[i] = 'fizzbuzz'
    elif num % 3 == 0:
        number[i] = 'fizz'
    elif num % 5 == 0:
        number[i] = 'buzz'
print(number)



numbers = [45,22,14,65,97,72]
for i in range(len(numbers)):
    if numbers[i] % 3 == 0 and numbers[i] % 5 == 0:
        numbers[i] = 'fizzbuzz'
    elif numbers[i] % 3 == 0:
        numbers[i] = 'fizz'
    elif numbers[i] % 5 == 0:
        numbers[i] = 'buzz'
print(numbers)