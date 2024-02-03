a = 1


def f(g):
    a = 2
    return lambda y: a * g(y)


print(f(lambda y: a + y)(a))


################################################################################

"""
This environment diagram is not 100% correct, compare with
https://pythontutor.com/render.html#code=a%20%3D%201%0A%0Adef%20f%28g%29%3A%0A%20%20%20%20a%20%3D%202%0A%20%20%20%20return%20lambda%20y%3A%20a%20*%20g%28y%29%0A%0Af%28lambda%20y%3A%20a%20%2B%20y%29%28a%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false


Global frame
a           -------------------->   1
f           -------------------->   function f(g) [parent: Global]

f1 f [parent: Global]
g           -------------------->   function lambda(y) [parent: Global]
a           -------------------->   2
returnVal   -------------------->   function lambda(y) [parent: f1] *

lambda2 [parent: f1]
y           -------------------->   1
a           -------------------->   2
returnVal   -------------------->   4

lambda1 [parent: Global]
a           -------------------->   1
y           -------------------->   1
returnVal   -------------------->   2


* The lambda expression in the call to function f is a global espression, but it
is immediately passed as an argument to the function f, there is no reference to
it in the Global frame. It can therefore only be referred to in the function f
by its formal parameter g.
"""
