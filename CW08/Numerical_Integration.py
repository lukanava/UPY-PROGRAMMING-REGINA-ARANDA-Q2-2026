import math
class InvalidValor (Exception):
    pass
try:
      a=input("Write the left endpoint of the interval: ")
      if a.isalpha()==True and a!="pi":
          raise TypeError ("El valor debe ser numerico")
      b=input("Write the right endpoint of the interval: ")
      if b.isalpha()==True and b!="pi":
          raise TypeError ("El valor debe ser numerico")
      f_x=input("Write the functtion to integrate: ")
      method=input("Writhe the integration method (LRM,RRM,MRM,TRAP)")
except TypeError as e:
    print(e)    
else:      
    if "pi" in a:
        a = eval(a.replace("pi", str(math.pi)))
    if "pi" in b:
        b = eval(b.replace("pi", str(math.pi)))
                       
    n=1000
    h=(b-a)/n
    area=0.0
    shift=0
    constant=0
    variable=0

    if method=="RRM":
        shift=1
    if method=="MRM":
        constant= h/2
    if method=="TRAP":
        variable=1
        f_0=f_x.replace("x",str(a))
        area += (h/2)* eval(f_0)
    
        for i in range (variable, n):
            xi = a + i * h
            f_xi = f_x.replace ("x", str(xi))
            area += (h/2) * 2 * eval(f_xi)
        f_xn=f_x.replace("x",str(b))
        area += (h/2) * eval(f_xn)
    else:   
        for  i in range (0 + shift,n + shift):
            xi = a + i * h
            height=f_x.replace("x", str(xi + constant))
            area +=h * eval (height)

#DISPLAY 
    print(f"The integration of {f_x} is {area}")
