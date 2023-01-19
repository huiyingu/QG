a = input()
b = input()
c = input()
if a > b:
    if b > c:
        print(f'{c}<{b}<{a}')
    elif a > c:
        print(f'{b}<{c}<{a}')
    else:
        print(f'{b}<{a}<{c}')
else:
    if a > c:
        print(f'{c}<{a}<{b}')
    elif b > c:
        print(f'{a}<{c}<{b}')
    else:
        print(f'{a}<{b}<{c}')
