def create_function(poly):
    def function(x):
        result = 0
        for term in poly:
            result += term['m'] * (x ** term['p'])

        return result

    return function


# مثال
# m = multiplier, p = power
poly = [{'m': 1, 'p': 2}, {'m': 2, 'p': 1}, {'m': 1, 'p': 0}]

f = create_function(poly)
answer = f(5)

print(answer)
