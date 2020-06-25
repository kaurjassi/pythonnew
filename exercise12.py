numbers = list(range(1,21))


def square_list(l):
    square = []
    for i in l:
        square.append(i**2)
    return square

print(square_list(numbers))