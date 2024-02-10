def print_sums(x):
    print(x)
    def next_sum(y):
        return print_sums(x+y)
    return next_sum

print_sums(1)(3)(5)

################################################################################

"""
Note: RV = return value


Global
print_sums  -------------->     function print_sums(x) [parent: Global]


f1 print_sums [parent: Global]
x           -------------->     1
next_sum    -------------->     function next_sum(y) [parent: f1]
RV          -------------->     function next_sum(y) [parent: f1]


f2 next_sum [parent: f1]
y           -------------->     3
RV          -------------->     function next_sum(y) [parent: f3]


f3 print_sums [parent: Global]
x           -------------->     4
next_sum    -------------->     function next_sum(y) [parent: f3]
RV          -------------->     function next_sum(y) [parent: f3]


f4 next_sum [parent: f3]
y           -------------->     5
RV          -------------->     function next_sum(y) [parent: f5]


f5 print_sums [parent: Global]
x           -------------->     9
next_sum    -------------->     function next_sum(y) [parent: f5]
RV          -------------->     function next_sum(y) [parent: f5]


Interactive output would be:
>>> print_sums(1)(3)(5)
1
4
9
function print_sums
"""

