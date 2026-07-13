import math
try:
    a = input("Write the left endpoint of the interval: ").strip()
    b = input("Write the left endpoint of the interval: ").strip()
    f_x = input("Write the function to integrate: ").strip()
    method = input("Write the integration method(LRM/RRM/MRM/TRAP): ").strip().upper()
    if "pi" in a: a = a.replace("pi", str(math.pi))
    if "pi" in b: b = b.replace("pi", str(math.pi))
    try:
        a = float(eval(a) if ("/" in a or "math.pi" in a) else a)
    except (ValueError, SyntaxError, NameError):
        print("El límite inferior debe ser numérico")
        exit()
    else:
        try:
            b = float(eval(b) if ("/" in b or "math.pi" in b) else b)
        except (ValueError, SyntaxError, NameError):
            print("El límite superior debe ser numérico")
            exit()
        else:
            if not f_x or "^" in f_x:
                print("La función ingresada no es válida")
                exit()
            elif 'y' in f_x or 'z' in f_x:
                print("La función debe estar escrita en términos de x")
                exit()
            elif a >= b:
                print("El límite inferior debe ser menor que el límite superior")
                exit()
            else:
                if method == "TM": 
                    method = "TRAP"   
                if method not in ["LRM", "RRM", "MRM", "TRAP"]:
                    print("El método de integración no es válido. Usa LRM, RRM, MPM o TM")
                    exit()
except Exception:
    print("La función ingresada no es válida")
    exit()
n = 1000
h = (b - a) / n
area = 0.0
shift = 0
constant = 0
variable = 0
try:
    if method == "TRAP":
        variable = 1
        f_0 = f_x.replace("x", f"({a})")
        area += (h / 2) * eval(f_0)
        
        for i in range(variable, n):
            xi = a + i * h
            f_xi = f_x.replace("x", f"({xi})")
            area += (h / 2) * 2 * eval(f_xi)
            
        f_xn = f_x.replace("x", f"({b})")
        area += (h / 2) * eval(f_xn)  
    else:
        if method == "RRM":
            shift = 1   
        if method == "MRM":
            constant = h / 2    
        for i in range(0 + shift, n + shift):
            xi = a + i * h
            height = f_x.replace("x", f"({xi + constant})")
            area += h * eval(height)
except ZeroDivisionError:
    print("La función no está definida en algún punto del intervalo")
    exit()
except (NameError, AttributeError):
    print("La función ingresada no es válida")
    exit()
else:
    print(f"The integration of ({f_x}) is {area}")