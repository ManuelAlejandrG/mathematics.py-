from sympy import *
a = Rational(1,2)

print(a**2)
x = Symbol('x')
solve(39*x+5, x)
x = Symbol('x')
y = Symbol('y')
print(expand((x+y)**3))
print(expand(x+y, complex=True) )
