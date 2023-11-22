def succ(Z):
    return Z + 1
def pred(Z): 
    if Z >= 1:
        return Z - 1
    else:
        return 0


""" Sesion 8-E6-b): Construir un PW que compute f(X)=2^X. Empleando macros: suma y asignacion """ 
# Pasar f como argumento las k varibles (X1, X2, ...Xk)  del programa while k variables construido
def pw(X1,X2,X3):
    """X1 viene el argumento de entrada(input) es decir la x
    X2 vamos iterar de 1.asfsafsdaffsdfsaf.X
    X3 calculamos 2^x
    """
    X3 = 1
    while(X2!= X1):
        """Calculo la nueva potencia de 2 usando la anterior
           2^x = 2^(x-1) + 2^(x-1)"""
        X3 = X3 + X3
        X2 = succ(X2)
    X1 = X3
    return X1


def doselevX(X):
  return print(pw(X,0,0))

# Para probar el programa, invocar a doselevX
doselevX(3)
