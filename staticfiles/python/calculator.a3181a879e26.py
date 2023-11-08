from pyscript import document, display


def q(selector, root=document):
    return root.querySelector(selector)


memory = []

input = q("#input")
button = q("#button")
calc_display = q("#display")

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
expression_string = q("#expressionString")


def enter_number(e):
    value = e.target.value
    calc_display.value = calc_display.value + e.target.value
    memory.append(value)
    print(memory)


def clear_memory(e):
    calc_display.value = ""
    display(f"", target="expressionString", append=False)
    memory.clear()


def enter_operand(e):
    operand = e.target.value
    memory.append(operand)
    calc_display.value = ""
    print(memory)


def calculate(e):
    expression_str = "".join(memory)

    print(f" {str(expression_str)} ")

    try:
        result = eval(expression_str)
        print(expression_str)
        calc_display.value = result
        display(f"{expression_str}", target="expressionString")
        memory.clear()
        memory.append(str(result))

    except Exception as e:
        calc_display.value = "err"
        print(f"Error: {str(e)}")
