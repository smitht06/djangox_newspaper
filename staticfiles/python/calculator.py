from pyweb import pydom


def add(numbers, sum=0):
    for number in numbers:
        sum += number

    return sum
