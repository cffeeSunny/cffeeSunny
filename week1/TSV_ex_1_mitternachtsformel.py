def mitternachtsformel(a, b, c):
    x = (-b + (b**2 -4*a*c)**(1/2))/(2*a)
    y =(-b - (b**2 -4*a*c)**(1/2))/(2*a)
    if x >= y : return round (x,2)
    else : return round(y,2)