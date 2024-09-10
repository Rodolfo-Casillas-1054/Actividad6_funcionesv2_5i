print("Mas sobre funciones")
# Aqui se escriben las funciones
def suma_ab(a,b):
    s=a+b
    return s

def resta_ab(a,b):
    s=a-b
    return s

def multi_ab(a,b):
    s=a*b
    return s

def div_ab(a,b):
    s=a/b
    return s

#Lamadas a funciones
print("Calculando suma")
s1=int (input("Ingresa el primer numero "))
s2=int (input("Ingresa el segundo numero "))
suma=suma_ab(s1,s2)
print(f"La suma de {s1} y {s2} da: {suma}")

print("Calculando resta")
r1=int (input("Ingresa el primer numero "))
r2=int (input("Ingresa el segundo numero "))
resta=resta_ab(r1,r2)
print(f"La resta de {r1} y {r2} da: {resta}")

print("Calculando multiplicaciones")
m1=int (input("Ingresa el primer numero "))
m2=int (input("Ingresa el segundo numero "))
multi=multi_ab(m1,m2)
print(f"La multiplicacion de {m1} y {m2} da: {multi}")

print("Calculando divisiones")
d1=int (input("Ingresa el primer numero "))
d2=int (input("Ingresa el segundo numero "))
div=div_ab(d1,d2)
print(f"La multiplicacion de {d1} y {d2} da: {div}")