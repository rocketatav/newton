def f_prime(x):
    return 12 - 12 * x ** 3 - 12 * x ** 5


def f_double_prime(x):
    return - 3 * x ** 2 - 60 * x ** 4


def newtons_method(tolerance, starting_point):
    k = 0
    x = starting_point
    while True:
        new_x = x - (f_prime(x)/f_double_prime(x))
        x = new_x
        k += 1

        print("#########################", "\n", "iter:", k, "\n", "value:", x)

        if abs(f_prime(x)) < tolerance:
            print("optimality found within", k, "iterations", "\n", "optimal value :", x)
            return x


newtons_method(tolerance=0.00001, starting_point=1)

