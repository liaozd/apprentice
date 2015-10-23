#!/usr/bin/env python


def expand(format, d, marker='"', safe=False):
    if safe:
        def lookup(w):
            return d.get(w, w.join(marker*2))
    else:
        def lookup(w):
            return d[w]
    parts = format.split('"')
    parts[1::2] = map(lookup, parts[1::2])
    return ''.join(parts)

if __name__ == '__main__':
    print expand('just "a" test "b" "c"', {'a': 'one'}, safe=True)

