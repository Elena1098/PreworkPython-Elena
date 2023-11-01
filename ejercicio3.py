## EJERCICIOS NIVEL MEDIO
# 1. Ejercicio: Define una función que utilice un bucle para imprimir los primeros n números de la serie de Fibonacci. 
  # **La serie de Fibonacci es una secuencia de números enteros que comienza con 0 y 1, y en la que cada término siguiente se obtiene sumando los dos términos anteriores. Es decir, que el tercer término es la suma de los dos primeros (0 + 1 = 1), el cuarto término es la suma del segundo y el tercer término (1 + 1 = 2), y así sucesivamente.

def fibonacci(n): 
  if n < 2:
    return n
  else:
    return fibonacci(n-1) + fibonacci(n-2)

for n in range(2,10):
  print(fibonacci(n))

#OTRA OPCIÓN
def fibonacci(numero):
  if numero == 0:  
   return  0 
  elif numero == 1:
    return 1 
  else:
   return fibonacci(numero - 1 ) + fibonacci(numero -2)

num = int(input('Ingrese el numero:'))

print('Los numeros de fibonacci son:')

for a in range(0,num):
 print (fibonacci(a))

# 2. Ejercicio: Define una función que tome un número y retorne una lista de sus divisores. 
#contador = 0
def divisores(num):
  return [a for a in range(1, num + 1) if num% a == 0]
print(divisores(10))

# 3. Ejercicio: Define una función que tome una lista y retorne una nueva lista con los elementos únicos de la lista original. 
def elementos_unicos(lista):
  return list(set(lista)) # set en Python solo muestra valores únicos
lista = [5,27,19,5,49,27]
print(elementos_unicos(lista))

# 4. Ejercicio: Define una función que tome un número y retorne la suma de sus dígitos. 
def sumar_digitos(numero):
  numero = str(numero)
  suma = 0
  for i in numero:
    suma += int(i)
  return suma

num = int(input('Ingrese el numero:'))
print('La suma de los digitos es:', sumar_digitos(num))

# 5. Ejercicio: Define una función que tome una cadena y cuente el número de vocales en la cadena. 
def contar_vocales(cadena):
  contador = 0
  for letra in cadena:
    if letra.lower() in 'aeiou':
      contador += 1
  return contador

cadena = "Hola mundo, como estas"
print(f"En la cadena {cadena} hay, {contar_vocales(cadena)} vocales") 

# 6. Ejercicio: Define una función que tome una lista y un número n, y retorne los primeros n elementos de la lista. 
def primeros_de_la_lista(lista, n):
  return lista[:n]
lista = [12,13,14,15,16]
print(f"Los primeros elementos de la lista son", primeros_de_la_lista(lista, 4)) #4 indica los primeros 4 elementos de la lista, esto lo elegimos nosotros

# 7. Ejercicio:  Define una función que tome una cadena y retorne la cantidad de letras mayúsculas y minúsculas en la cadena.
def contar_mayusculas_minusculas(cadena):

  mayusculas = sum(1 for letra in cadena if letra.isupper())      
  minusculas = sum(1 for letra in cadena if letra.islower())      
  return mayusculas, minusculas
cadena = "Soy Elena Bravo"
print(f"En la frase Soy Elena Bravo, hay {contar_mayusculas_minusculas(cadena)}, mayusculas y minusculas respectivamente")

# 8. Ejercicio:  Define una función que tome un número y retorne True si es un número perfecto, False en caso contrario. 
    #   Un número perfecto es aquel que es igual a la suma de sus divisores propios positivos. Por ejemplo, 6 es un número perfecto porque sus divisores son 1, 2 y 3, y 6 = 1 + 2 + 3. 

def es_perfecto(num):
  suma = 0
  for i in range(1,num):
    if num % i == 0:
      suma += i
  return suma == num #aquí estamos preguntando si la suma es igual al numero, si es true quiere decir q el num es perfecto

print(es_perfecto(6)) #debe dar true 

# 9. Ejercicio:  Define una función que reciba un número y retorne su representación en binario. 
def a_binario(n):
  return bin(n).replace("0b", "") #En Python se utiliza 0b para identificar el numero como binario
print(a_binario(9))

# 10. Ejercicio: Define una función que reciba dos listas y retorne la intersección de ambas (los elementos que están en las dos listas).
def interseccion(list1, list2):
  return list(set(list1) & set(list2))

list1 = [22, 15, 125, 18]
list2 = [18, 15, 45, 79]
print(interseccion(list1, list2))

# 11. Ejercicio:  Define una función que tome una cadena y determine si es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda). 
def es_palindromo(cadena):
  return cadena == cadena[::-1]
print(es_palindromo("radar")) #dará True

# 12. Ejercicio:  Escribe un programa que imprima los números del 1 al 50, pero para múltiplos de tres imprima “Fizz” en lugar del número y para los múltiplos de cinco imprima “Buzz”. Para números que son múltiplos de tanto tres como cinco imprima “FizzBuzz”. 

for a in range(1, 51): 
  if a % 3 == 0 and a % 5 == 0:          
    print("FizzBuzz")      
  elif a % 3 == 0:          
      print("Fizz")      
  elif a % 5 == 0:          
      print("Buzz")      
  else:
      print(a)
      
# 13. Ejercicio:  Define una función que tome una lista y retorne la lista ordenada en orden ascendente.
def ordenar_lista(lista):
  return sorted(lista)   
lista = [8, 15, 24, 52, 182, 75, 33, 49, 8, 1, 37]
print(ordenar_lista(lista))
