print("Welcome to the factor quadratics when a = 1 program!")
print("Enter your quadratic below. Enter the value of b and c.")
print("For example, if your quadratic is x^2 + 6x + 8 = 0," +  
"you would enter 6 for b and 8 for c.")

# Get user input 
b = int(input("What is the value of b? "))
c = int(input("What is the value of c? "))

# What we need to do is find the factors of c
i = 1
sum_factors = 0
if b > 0 and c > 0:
    while i < c:
        factor_rem = c % i
        if factor_rem == 0:
            sum_factors = i + (c / i)
            if sum_factors == b:
                x1 = str(i)
                x2 = str(int(c / i))
                i = c
        i = i + 1
elif b < 0 and c > 0:
    i = -1
    c = -1 * c
    while i > c:
        factor_rem = c % i
        if factor_rem == 0:
            sum_factors = i + (-1 * c / i)
            if sum_factors == b:
                x1 = str(i)
                x2 = str(int(-1 * c / i))
                i = c
        i = i - 1
elif c < 0:
    i = -1
    while i > c:
        factor_rem = c % i
        if factor_rem == 0:
            sum_factors = c / i + i
        if sum_factors == b:
            x1 = str(i)
            x2 = str(int(c / i))
            i = c
        i = i - 1

if sum_factors != b:
    print("This quadratic is not factorable.")
else:
    print("The quadractic factors to " +
    "(x + " + x1 + ")(x + " + x2 + ").")

# TODO handle exceptions
# TODO deal with one negative and one positive factor - 2nd type
