"""
give arithmetic expression with + and * calculate result
"""

def arithmetic(expr):
    parts = expr.split('+')
    s = 0
    for part in parts:
        s += reduce(lambda x,y: x*y, [int(a) for a in part.split('*')])

    return s


print arithmetic('1+2*3+4')