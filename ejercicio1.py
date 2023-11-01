
# VARIABLES Y OPERADORES

# 1. Ejercicio: Crea una variable llamada nombre y asígnale tu nombre como valor. Luego, imprime la variable. 
nombre = 'Elena'
print(nombre)

#2. Ejercicio: Crea dos variables, a y b, y asígnales los valores 5 y 10 respectivamente. Luego, imprime la suma de a y b

a = 5
b= 10

suma = a + b
print(suma)

#3. Ejercicio: Calcula el área de un triángulo con base 10 y altura 5. 
base = 10
height = 5

Area = (base*height)/2
print(Area)

#4. Ejercicio: Calcula el resto de dividir 17 entre 3.
resto = 17/3
print(resto)


## CONDICIONALES

# 1. Ejercicio: Dado un número, imprime si es positivo o negativo. 

x = -5
if x > 0:
  print("x es positivo")
else:
  print("x no es positivo")

# 2. Ejercicio: Dado un número, imprime si es par o impar. 
x = 2
if x % 2 == 0:
  print(x,"es par")
else:
  print(x,"es impar")

# 3. Ejercicio: Dado tres números, encuentra y muestra el mayor de ellos. 
A = 5
B = 7
C = 2
if(A > B and A > C):
 print("El numero mayor es ", A)
else:
 if(B > A and B > C):
  print("El numero mayor es ", B)
 else:
  print("El numero mayor es ", C)
  


## BUCLES
# 1. Ejercicio: Imprime los números del 1 al 10 usando un bucle for. 
numeros = [1,2,3,4,5,6,7,8,9,10]
for numero in numeros:
  print(numero)
  
# 2. Ejercicio: Imprime los números pares del 1 al 20 usando un bucle while.
i = 1 
while i <= 20:
  print(i)     
  i += 1 
  
# 3. Ejercicio: Usa un bucle para calcular la suma de los números del 1 al 100.
i = 1
suma = 0
while i <=100:
  suma = suma + i
  i += 1
print("La suma de los números del 1 al 100 es:", suma)

## FUNCIONES
# 1. Ejercicio: Define una función que tome dos números y retorne su suma. 
def suma(a,b):
  return a + b
resultado = suma(3,5)
print(resultado)

# 2. Ejercicio: Define una función que tome un número y retorne su factorial. 
def factorial(n):
  if n < 0:
    return "ERROR"
  if n== 0 or n == 1:
    return 1
  for i in range (1,n):
    n = n*i
  return n
x = 5
f = factorial(x)
print("El factorial de 5 es", f)

# 3. Ejercicio: Define una función que tome un número y determine si es primo. 
def es_primo(n):
  if n == 1:
    return False 
  elif n == 2:
    return True
  else:
    for i in range (2,n):
      if n % i== 0:
        return False
    return True
for i in range (1,11):
  print(i,es_primo(i))
      

# 4. Ejercicio: Define una función que reciba una lista de números y retorne la suma de ellos. 

def suma_lista(numeros):
  suma = 0
  for numero in numeros:
    suma += numero
  return suma
mi_lista = [1, 2, 3, 4, 5]
print(suma_lista(mi_lista))

# 5. Ejercicio: Define una función que reciba una cadena de texto y retorne la cadena en reversa (invertida).

cadena = "hola"
cadena_invertida = cadena[::-1]
print(cadena_invertida)