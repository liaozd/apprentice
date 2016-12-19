CONDITIONS = [(lambda i: i % 4 == 0, "four"),
              (lambda i: i % 6 == 0, "six"),
              (lambda i: i % 7 == 0, "seven")]


def apply_conditions(i):
    for condition, replacement in CONDITIONS:
        if condition(i):
            return replacement
    return None

ar = map(apply_conditions, range(0, 10))

print filter(None, ar)
print ar
