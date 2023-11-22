def succ(Z):
    return Z + 1
def pred(Z): 
    if Z >= 1:
        return Z - 1
    else:
        return 0

""" PW-E5: Construyase un programa while equivalente a la siguiente sentencia. 
Las unicas macros permitidas son los macro test
if X1!=X2: 
    X1=X1+X2
"""

# Pasar al pw como argumento las k varibles (X1, X2, ...Xk) del programa while k variables construido
def pw(X1,X2):
    X3 = 0
    X3 = succ(X3)
    while(X1 != X2) and  (X3 != 0):
        X4 = 0
        while X4 != X2:
            X1 = succ(X1)
            X4 = succ(X4)
        X3 = 0

    return X1

def f(X,Y):
	return print(pw(X,Y))
    


# Para probar el programa, invocar a f
# Probar que funciona cuando el test (X1!=X2) se evalua a cierto y a falso
f(4,3)

