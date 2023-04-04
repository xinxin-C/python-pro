def add(*args):
    sum = 0
    for n in args:
        sum += n
    print(sum)


add(33, 2, 45, 775, 3, 4)

def calculate(**kwargs):
    print(kwargs)