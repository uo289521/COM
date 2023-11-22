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


	
""" PW-E6-d): Construir un PW que compute f(X)=log_10(X). Empleando macros: producto, resta y asignacion """ 
# Pasar a f como argumento las k varibles (X1, X2, ...Xk)  del programa while k variables construido
def pw(...):


    return X1

def log_b10(X):
  return print(pw(X,...))

# Para probar el programa, invocar  log_b10
# Probar que sucede para varios valores de X: 10, 100, 150, 1 ...
# Probar que cuando X==0 --> Indeterminacion
log_b10(...)

	