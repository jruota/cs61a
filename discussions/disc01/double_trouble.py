def double(x):
    return x * 2


def triple(x):
    return x * 3


hat = double
double = triple


"""
Global frame
double  ----------------->  func triple(x) [parent=Global]
triple  ----------------->  func triple(x) [parent=Global]
hat     ----------------->  func double(x) [parent=Global]
"""