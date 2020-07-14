def func1(x):
    return x * 2


def func3(*args):
    return [x * 2 for x in args]


def a(**var):
    """

    :type var: dict
    """
    for i in var:
        print(f'{i} = ', var[i])

print(func1(13))
print(func3(1, 2, 3, 7, 12))

vars = dict(one=1, two=2, zero=0)
#a(one=4, two=2, zero=0)
a(**vars)

# enumerate([])
