def do_it(funcs):
    num1, num2, op = funcs
    if op == '+':
        return str(int(num1) + int(num2))
    elif op == '-':
        return str(int(num1) - int(num2))
    elif op == '/':
        return str(int(num1) / int(num2))
    elif op == '*':
        return str(int(num1) * int(num2))