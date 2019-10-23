import math
print(math.ceil(2.3))
print(math.floor(2.3))
print(math.copysign(1.0, -0.0))#Return a float with the magnitude (absolute value) of x but the sign of y.
#Return the absolute value of x.
print(math.fabs(-2.3))
print(math.factorial(10))
print(math.fmod(20, 10))

#Return an accurate floating point sum of values in the iterable. Avoids loss of precision by tracking multiple intermediate partial sums:
print(math.fsum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1]))

print(math.gcd(3,4))