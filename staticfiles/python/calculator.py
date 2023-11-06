from pyscript import window, document


def add(numbers, sum=0):
    for number in numbers:
        sum += number

    return sum


def subtract(numbers, difference=0):
    for number in numbers:
        difference += number

    return difference


input = document.querySelector("input")
button = document.querySelector("button")

print(input)
