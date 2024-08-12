from math import inf


def divide(first, second):
  if second == 0 or second == '0':
    return inf
  else:
    return first / second
