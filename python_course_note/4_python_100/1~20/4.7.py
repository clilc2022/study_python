"""depth and shadow copy"""
import copy

a = [[_ for _ in range(5)], [_ for _ in range(3)]]
b = a[:]
c = a.copy()
d = copy.deepcopy(a)
print("---This is a---")
print(id(a))
print(id(a[0]))
print(id(a[1]))
print("---This is b---")
print(id(b))
print(id(b[0]))
print(id(b[1]))
print("---This is c---")
print(id(c))
print(id(c[0]))
print(id(c[1]))
print("---This is d---")
print(id(d))
print(id(d[0]))
print(id(d[1]))