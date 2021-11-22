import math


def add(a, b) -> int:#probando si linting sigue funcionado
    return math.floor(a + b)


def to_sentence(s) -> str:
    s = s.capitalize()

    if s.endswith('.'):
        return s
    else:
        return s + '.'
