from pyscript import document
import math
import js


def q(selector, root=document):
    return root.querySelector(selector)


memory = []

input = q("#input")
button = q("#button")
display = q("#display")

button_1 = q("#btn1")
button_2 = q("#btn2")
button_3 = q("#btn3")
button_4 = q("#btn4")
button_5 = q("#btn5")
button_6 = q("#btn6")
button_7 = q("#btn7")
button_8 = q("#btn8")
button_9 = q("#btn9")
button_0 = q("#btn0")
button_clear = q("#btnClear")
button_plus = q("#btnPlus")
button_minus = q("#btnMinus")
button_multiply = q("#btnMultiply")
button_divide = q("#btnDivide")
button_equals = q("#btnEquals")


def enter_number(e):
    value = e.target.value
    display.value = display.value + e.target.value
    memory.append(value)
    print(memory)


def clear_memory(e):
    display.value = ""
    memory.clear()


def enter_operand(e):
    operand = e.target.value
    memory.append(operand)
    display.value = ""
    print(memory)


def calculate(e):
    expression_str = "".join(memory)
    expression_string = q("#expressionString")
    print(f" {str(expression_str)} ")

    try:
        result = eval(expression_str)
        print(expression_str)
        display.value = result
    except Exception as e:
        display.value = "err"
        print(f"Error: {str(e)}")
