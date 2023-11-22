def succ(Z):
    return Z + 1
def pred(Z): 
    if Z >= 1:
        return Z - 1
    else:
        return 0
		
		
# macro resta acotada	
def resta(X,Y):
    Z=0;
    while Z!=Y:
        X=pred(X)
        Z=succ(Z)
    return X

""" PW-E4: Construir un PW sin macro-tests equivalente a este 
begin
Z:=succ(X)
while (X!=Y) or (Z<T) do
    begin
      Y:=succ(Y);
      Z:=pred(Z);
    end
end
"""

# Pasar al pw como argumento las k varibles (X1, X2, ...Xk) del programa while k variables construido
def pw(X,Y,T):
    Z = succ(X)
    U = resta(Y,X)
    V = resta(X,Y)
    U = U + V
    V = resta(T,Z)
    U=U*V
    V = 0

    while U != V:
        Y = succ(Y)
        Z = pred(Z)

        U = resta(Y,X)

        V = resta(X,Y)
        U = U+V
        V=0



    return X

# Para probar el programa, invocar el main con k argumentos
# Probar que funciona cuando el macro test (X!=Y) or (Z<T) se evalua a cierto y a falso
print(pw(1,1,0))

