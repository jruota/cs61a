n = 7

def f(x):
    n = 8
    return x + 1

def g(x):
    n = 9
    def h():
        return x + 1
    return h

def f(f, x):
    return f(x + n)

f = f(g, n)
g = (lambda y: y())(f)


################################################################################


"""
Note: RV = return value


Global frame
n   -------------->     7
f   -------------->     function f(x) [parent: Global]      SHADOWED!
g   -------------->     function g(x) [parent: Global]      SHADOWED!
f   -------------->     function f(f, x) [parent: Global]   SHADOWED!
f   -------------->     function h() [parent: f2]
g   -------------->     15


f1 f(f, x) [parent: Global]
f   -------------->     function g(x) [parent: Global]
x   -------------->     7
RV  -------------->     function h() [parent: f2]


f2 g(x) [parent: Global]
x   -------------->     14
n   -------------->     9
h   -------------->     function h() [parent: f2]
RV  -------------->     function h() [parent: f2]


f3 lambda<line 17> [parent: Global]
y   -------------->     function h() [parent: f2]
RV  -------------->     15


f4 function h() [parent: f2]
RV  -------------->     15
"""
