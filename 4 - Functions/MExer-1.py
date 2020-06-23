def calculate(type, thing):
    if type == 'int':
        thing = int(thing)
        print(thing*2)
    elif type == 'real':
        thing = float(thing)
        print(f'{thing*1.5:.2f}')
    elif type == 'string':
        print(f'${thing}$')


thing_type = input()
thingy = input()
calculate(thing_type, thingy)
