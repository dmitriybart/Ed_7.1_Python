from pathlib import Path
def write_data(num1, num2, oper):
    d = Path('bd_calc.txt')
    with open (d, 'w', encoding="UTF-8") as data:
        data.write(f'{num1} {num2} {oper}')

def read_data():
    d = Path('bd_calc.txt')
    with open (d, 'r') as data:
         return data.readline().split()

def write_data_res(res):
    d = Path('bd_res.txt')
    with open (d, 'w') as data:
        data.write(res)