def do_it(funcs):
    num1, num2, op = funcs
    if op == '+':
        return int(num1) + int(num2)
    elif op == '-':
        return int(num1) - int(num2)
    elif op == '/':
        return int(num1) / int(num2)
    elif op == '*':
        return int(num1) * int(num2)