
def my_func(*args, **kwargs):

    for i, arg in enumerate(args):
        print('args[{}] = {}'.format(i, args[i]))

    for k,v in kwargs.items():
        print('kwargs[\'{}\'] = {}'.format(k,v))


if __name__ == '__main__':
    my_func(1, 2, 3, in_place=True, verbose=False)