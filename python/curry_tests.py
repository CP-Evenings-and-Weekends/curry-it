from curry import batting_average


print(batting_average("Ohtani")(8)(7)(20))
print(batting_average("Trout")(10)(9)(30))
print(batting_average("Betts")(15)(12)(45))

lopez = batting_average("Lopez")(162)
print(lopez(45)(150))
print(lopez(38)(120))
print(lopez(60)(200))

# Didn't get to the examples below, I was just trying to get it to click

# def add3(a, b, c):
#     return a + b + c


# def mul2(a, b):
#     return a * b


# def add4(a, b, c, d):
#     return a + b + c + d


# curried_add = curry(add3)
# print(curried_add(1)(2)(3) == 6)
# print(curried_add(10)(20)(30) == 60)
# print(curried_add(-5)(5)(0) == 0)

# curried_mul = curry(mul2)
# print(curried_mul(4)(5) == 20)
# print(curried_mul(0)(100) == 0)

# curried_add4 = curry(add4)
# print(curried_add4(1)(2)(3)(4) == 10)
