def succ(Z):
    return Z + 1
def pred(Z): 
    if Z >= 1:
        return Z - 1
    else:
        return 0

		
"""
x1 < la entrada
x2 < iterar de 1
x3 < calcular el factorial
x4 < calculamos el sumatorio        
            caso especial 
                sum 1=0 (0!) = 1
"""
def pw(X1,X2,X3,X4):
    X3 = 1  # caso especial
    X4 = 1  # sum X=0..0 (0!) = 1
    while X2 != X1:
        X2 = succ(X2)
        X3 = X3 * X2
        X4 = X4 + X3
    X1 = X4
    return X1

def sum_fact(X):
  return print(pw(X,0,0,0))


# Para probar el programa, invocar a sum_fact	
# Probar que sucede para varios valores de X: 0, 1, 2, ...
sum_fact(5)



"""
begin 
    X5 = X1
    Pfact
    X6 = X1
    while X7 != X5 do
    begin  
        X7: succ(X7)
        #Preparo vector estado para el fact 
        X1 = X7
        X2 = 0
        X3 = 0
        Pfact;
        X6 = X6 + X1
    end
    X1=X6 
    return X1;     
"""
