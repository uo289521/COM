def succ(Z):
    return Z+1
def pred(Z): 
    if Z>=1:
        return Z-1
    else:
        return 0
def resta(X,Y):
    Z=0;
    while Z!=Y:
        X=pred(X)
        Z=succ(Z)
    return X
"""
Sesion 8-E7: 7.    Dado el siguiente programa while, calculense:
F(1)(x), F(2)(x,y), F(3)(x,y,z). 
Ademas, construyase una secuencia de computacion con entrada (0,2,1)

begin
while (X1>X4) do
    begin
    X2:=X2+X2;
    X4:=succ(X4);
    end
X1:=X2;
while (X3!=0) do
    begin
    X1:=succ(X1);
    X3:=pred(X3);    
    end
end

"""


def pw(X1,X2,X3,X4,X5,X6):
    X5 = resta(X1,X4)
    X6 = 0
    while (X5!=X6): # X4 vale 0
        X2=X2+X2
        X4=succ(X4)
        #Recalculamos la expresion asociada al test
        X5 = resta(X1, X4)
        X6 = 0

    X1=X2

    while (X3!=X6):
        X1=succ(X1)
        X3=pred(X3)
    return  X1

def f_1(X):
  return print(pw(X,0,0,0,0,0))

def f_2(X,Y):
  #(2^X1)*X2
  return print(pw(X,Y,0,0,0,0))


def f_3(X,Y,Z):
    #(2^X1)*X2 + z
  return print(pw(X,Y,Z,0,0,0))



# F(X)? 0. Con un argumento se ejecuta sólo el primer bucle, pues X3 es 0
print ("F(X)")
# Si te ayuda, puedes probar con distintos valores de X, cambiando en la siguiente instruccion la X por su valor f(X)
f_1(4)
        
# F(X,Y)? 
print ("F(X,Y)")
# Si te ayuda, puedes probar con distintos valores de X e Y, cambiando en la siguiente instruccion X e Y por su valor
f_2(2,5)

print("F(X,Y,Z)")
# Si te ayuda, puedes probar con distintos valores de X, Y y Z,  cambiando en la siguiente instruccion X, Y y Z por su valor 
f_3(2,5,2)

"""
Secuencia de computacion con entrada (0,2,1). Completa la secuencia
a0 (0,2,1,0)
A1 X1>X4 
a1 (0,2,1,0)     
.....
"""