def succ(Z):
    return Z + 1
def pred(Z): 
    if Z >= 1:
        return Z - 1
    else:
        return 0

# macro resta acotada
def resta(X,Y):
    Z=0
    while Z!=Y:
        X=pred(X)
        Z=succ(Z)
    return X
 
""" Sesion 8-E3: Calculese para cada caso, la expresion algebraica ET, 
tal que tenga valor mayor que 0 cuanto T sea verdadero, y el valor 0 cuando T sea falso.
a)(x!=y) and (z>y)
b)(x<=y) or (z<x)

"""


def E_test_a(X,Y,Z):
    print("------Quitamos macro-test a)((X!=Y) and (Z>Y))")
    
	# Calcula aqui la expresion ET para el T=((X!=Y) and (Z>Y))
	# Si te resulta mas comodo, puedes construir poco a poco la expresion ET, calculando las subexpresiones y
    # empleando para ello las variables U y V
    U = resta(Y,X)
    V = resta(X, Y)
    U += V
    #Expresion Z < Y
    V = resta(Z,Y)

    U = U * V
    print("a) (",X,"!=", Y,") and (", Z, ">", Y, ")",((X!=Y) and (Z>Y)), ", ET = ", U)
	 

def E_test_b(X,Y,Z):
    print("------Quitamos macro-test b)((X<=Y) or (Z<X))")


	# Calcula aqui la expresion ET para el T=((X<=Y) or (Z<X))
    U = resta(X,Y)
    U = resta(1,U)
    V = resta(X,Z)
    U = U + V
	# Si te resulta mas comodo, puedes construir poco a poco la expresion ET, calculando las subexpresiones y
    # empleando para ello las variables U y V
    print("b) (",X,"<=", Y,") or (", Z, "<", X, ")",((X<=Y) or (Z<X)), ", ET = ", U)


# Comprueba que funciona

E_test_a(1,2,3) # true
E_test_a(1,1,3) # falso
E_test_b(1,2,3) # true
E_test_b(5,1,6) # falso


