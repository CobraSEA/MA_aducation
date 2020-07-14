word = 'Found name'
ids = dict(name='Alex', age=36)

def func(word, name, *args, age=None):
    print(word, name)
    print(f"Age: {age}")
    print(args)

func(word, **ids)

#func(word, ids['name'], *list(range(10)))