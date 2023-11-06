from pyscript import Element


def add(numbers, sum=0):
    for number in numbers:
        sum += number

    return sum


def subtract(numbers, difference=0):
    for number in numbers:
        difference += number

    return difference


input = Element("input")
button = Element("button")


def hello_world(input):
    input.write(f"Hello world")


hello_world(input)
