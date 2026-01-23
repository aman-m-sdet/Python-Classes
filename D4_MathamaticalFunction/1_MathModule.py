#Various possible ways to import module
#Mathamaticql Function from Math Module

import math
print(math.sqrt(4))   # 2.0

# Importan mOdels in Math Modele
# functions: sqrt(x) , floor(r), celi(r), pow(r)
# variable: pi,e,inf,nan

import math
print(dir(math)) 
#['__doc__', '__loader__', '__name__', '__package__', '__spec__', 
# 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 
# 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 
# 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 
# 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma',
#  'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow',
#  'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc',
#  'ulp']

print(math.sqrt(10))
print(math.pi)
print(math.floor(3.9))
print(math.ceil(3.9))
print(math.pow(3,2)) 

#when Module is Bigger Then use
import math as m
print(m.pi)
print(m.sqrt(9))

from math import *
print(sqrt(144))   #12

from math import sqrt as s
print(s(144))   #12