def team(work):
    return t(work) - 1

def dream(work, s):
    if work(s-2):
        t = not s
    return not t

work, t = 3, abs
team = dream(team, work + 1) and t


################################################################################


"""
Note: RV = return value


Global frame
team    -------------->     function team(work) [parent: Global] SHADOWED!
dream   -------------->     function dream(work, s) [parent: Global]
work    -------------->     3
t       -------------->     function abs(...)
team    -------------->     function abs(...)


f1 dream [parent: Global]
work    --------------->    function team(work) [parent: Global]
s       --------------->    4
t       --------------->    False
RV      --------------->    True


f2 function lambda(horse) [parent: Global]
work    --------------->    2
RV      --------------->    1
"""