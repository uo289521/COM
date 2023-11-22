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
 

""" PW-E8: 8.	Calcule las funciones semanticas unaria y binaria, asi
como la secuencia de computacion con entrada (2,2), para el siguiente programa while
 
begin
while (X1!=X3) do
    begin
	X1:=pred(X1);
	X3:=succ(X3);
    end
X1:=succ(X3);
while (X1!=X4) do
    begin
	X1:=resta(X1,X2);
	X5:=succ(X5);	
    end
X1:=pred(X5)
end

"""


def pw(X1,X2,X3,X4,X5):
    while (X1!=X3):
        X1=pred(X1) 
        X3=succ(X3)
    X1=succ(X3)
    while (X1!=X4):
        X1=resta(X1,X2)
        X5=succ(X5) 
    X1=pred(X5)
    return  X1


def f_1(X):
  return print(pw(X,0,0,0,0))

def f_2(X,Y):
  return print(pw(X,Y,0,0,0))

# f(X)? 
print("f(X)")
# Si te ayuda, puedes probar con distintos valores de X, cambiando en la siguiente instruccion la X por su valor
f_1(X)

        
# f(X,Y)? 
print("f(X,Y)")
# Si te ayuda, puedes probar con distintos valores de X e Y, cambiando en la siguiente instruccion X e Y por su valor
f_2(X,Y)

"""
Secuencia de computacion con input (2,2). Completa la secuencia de computacion
a0  ____________           
A1  ____________
...
"""




