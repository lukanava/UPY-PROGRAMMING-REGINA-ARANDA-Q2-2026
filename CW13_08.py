import math
class InvalidMethodError(Exception):
    pass


# INPUT
try:

    a = input("Write the left endpoint of the interval: ")
    b = input("Write the right endpoint of the interval: ")
    f_x = input("Write the function to integrate: ")
    method = input("Write the integration method (LRM,RRM,MRM,TRAP): ").upper()

    try:
        if "pi" in a:
            a = eval(a.replace("pi", str(math.pi)))
        else:
            a = float(a)

        if "pi" in b:
            b = eval(b.replace("pi", str(math.pi)))
        else:
            b = float(b)

    except ValueError:
        raise ValueError("The interval values must be numeric.")

    valid_methods = ["LRM", "RRM", "MRM", "TRAP"]

    if method not in valid_methods:
        raise InvalidMethodError("Invalid integration method.")

# PROCESS
    n = 1000
    h = (b - a) / n
    area = 0.0
    shift = 0
    constant = 0
    variable = 0

    if method == "RRM":
        shift = 1

    if method == "MRM":
        constant = h / 2
        
    try:

        if method == "TRAP":
            variable = 1
            f_0 = f_x.replace("x", str(a))
            area += (h / 2) * eval(f_0)

            for i in range(variable, n):
                xi = a + i * h
                f_xi = f_x.replace("x", str(xi))
                area += (h / 2) * 2 * eval(f_xi)

            f_xn = f_x.replace("x", str(b))
            area += (h / 2) * eval(f_xn)

        else:
            for i in range(0 + shift, n + shift):
                xi = a + i * h
                height = f_x.replace("x", str(xi + constant))
                area += h * eval(height)

    except Exception:
        raise ValueError("The mathematical function is invalid.")

# DISPLAY
    print(f"The integration of {f_x} is {area}")

except InvalidMethodError as e:
    print(e)

except ValueError as e:
    print(e)