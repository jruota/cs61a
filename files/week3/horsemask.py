def horse(mask):
    horse = mask
    def mask(horse):
        return horse
    return horse(mask)


mask = lambda horse: horse(2)

horse(mask)


################################################################################


"""
Note: RV = return value


Global frame
horse   -------------->     function horse(mask) [parent: Global]
mask    -------------->     function lambda(horse) [parent: Global]


f1 horse [parent: Global]
mask    --------------->    function lambda(horse) [parent: Global] SHADOWED!
horse   --------------->    function lambda(horse) [parent: Global]
mask    --------------->    function mask(horse) [parent: f1]
RV      --------------->    2


f2 function lambda(horse) [parent: Global]
horse   --------------->    function mask(horse) [parent: f1]
RV      --------------->    2


f3 function mask(horse) [parent: f1]
horse   --------------->    2
RV      --------------->    2
"""
