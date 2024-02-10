def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)


fact(3)

################################################################################

"""
Note: RV = return value


Global
fact        -------------->     function fact(n) [parent: Global]


f1 fact [parent: Global]
n           -------------->     3
RV          -------------->     6


f2 fact [parent: Global]
n           -------------->     2
RV          -------------->     2


f3 fact [parent: Global]
n           -------------->     1
RV          -------------->     1


f4 fact [parent: Global]
n           -------------->     0
RV          -------------->     1


Interactive output would be:
>>> fact(3)
"""
