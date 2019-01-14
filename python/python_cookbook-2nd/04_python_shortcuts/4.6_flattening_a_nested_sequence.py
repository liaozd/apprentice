def list_or_tuple(x):
    return isinstance(x, (list, tuple))


def flatten(sequence, to_expand=list_or_tuple):
    """递归实现"""
    for item in sequence:
        if to_expand(item):
            for subitem in flatten(item, to_expand):
                yield subitem
        else:
            yield item


def flatten_nonrecursive(sequence, to_expand=list_or_tuple):
    """非递归实现"""
    iterators = [iter(sequence)]
    while iterators:
        # loop on the currently most-nested(last) iterator
        for item in iterators[-1]:
            if to_expand(item):
                # subsequence found, go loop on iterator on subsequence
                iterators.append((iter(item)))
                break
            else:
                yield item
        else:
            # most-nested iterator exhausted, go back, loop on its parent
            iterators.pop()


if __name__ == '__main__':
    sequence = [1, 2, [3, [], 4, [5, 6], 7, [8, ], ], 9]
    print('flatten')
    for i in flatten(sequence):
        print(i, ', ', end='')

    print('\nflatten_nonrecursive')
    for i in flatten_nonrecursive(sequence):
        print(i, ', ', end='')
