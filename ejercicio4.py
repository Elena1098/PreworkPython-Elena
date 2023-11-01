## EJERCICIOS NIVEL MEDIO
# 14. Ejercicio:  Define una función que reciba una lista de palabras y un entero n, y retorne la lista de palabras que son más largas que n. 
def filtrar_palabras(lista_de_palabras, n):
  return [palabra for palabra in lista_de_palabras if len(palabra) > n]
print(filtrar_palabras(["Estoy", "eliptico", "comarca", "amor"], 4)) 

# 15. Ejercicio:  Define una función que tome un número y calcule su serie de Fibonacci. 
def serie_fibonacci(n):
  fib = [0, 1]
  if n <= 0:
    return []
  elif n == 1:
    return [0]
  while len(fib) < n:
    fib.append(fib[-1] + fib[-2])
  return fib

print(serie_fibonacci(20))

# 16. Ejercicio:  Define una función que tome una lista de números y retorne el número más grande de la lista. 
def maximo(lista): 
  return max(lista)
lista = [27, 85, 33, 2, 11]
print(maximo(lista))

# 17. Ejercicio:  Define una función que reciba un número y retorne la suma de sus dígitos al cubo. 
def suma_cubos_digitos(n):
  return sum(int(digit)**3 for digit in str(n))

print(suma_cubos_digitos(26))

# 18. Ejercicio:  Define una función que reciba una lista de números y retorne el segundo número más grande de la lista. 
def segundo_maximo(lista):
  return sorted(set(lista), reverse=True)[1]

    ## La función sorted() ordena por defecto de menor a mayor. Para que realice lo contrario, que ordene de mayor a menor, se puede indicar con el reverse=True. 
    ## Luego se pide el segundo elemento, por lo que usas [1]. Recuerda que el primer elemento de una lista se accede por el indice 0, por eso usas el indice 1, para acceder al segundo elemento

print(segundo_maximo([58, 37, 21, 13, 8, 99]))

# 19. Ejercicio:  Define una función que tome dos listas y retorne True si tienen al menos un miembro en común, de lo contrario, retorne False. 

def tienen_comun(lista1, lista2):
  return bool(set(lista1) & set(lista2))

lista1 = [1, 2, 3, 4]
lista2 = [4, 5, 6, 7]
print(tienen_comun(lista1, lista2)) 

# 20. Ejercicio:  Define una función que tome una lista y retorne una nueva lista con los elementos de la lista original en orden inverso. 
def invertir_lista(lista):
  return lista[::-1]

print(invertir_lista([8, 9, 10, 11, 12])) 

# 21. Ejercicio:  Define una función que reciba una cadena y cuente el número de dígitos y letras que contiene.
def contar_digitos_letras(cadena):
  digitos = sum(c.isdigit() for c in cadena)
  letras = sum(c.isalpha() for c in cadena)
  return digitos, letras

print(contar_digitos_letras("Hola, es la casa 13")) 

#22. Ejercicio:  Define una función que reciba una lista de números y retorne la suma acumulada de los números 
def suma_acumulada(lista):
  suma = 0 
  suma_acumulada = []
  for numero in lista:
    suma += numero
    suma_acumulada.append(suma)
  return suma_acumulada
lista = [1, 2, 3, 4, 5]
print(suma_acumulada(lista))

#23. Ejercicio:  Define una función que encuentre el elemento más común en una lista.

from collections import Counter 
        #Python cuenta con una clase llamada Counter dentro de collections que te permite contar las repeticiones dentro de un iterable, así como ofrecerte información relevante sobre ellos. La función Counter(lista).most_common() devuelve una lista de tuplas.
def elemento_mas_comun(lista):
  return Counter(lista).most_common(1)[0][0] 
        ##el numero (1) es pq queremos el elemento más común, si queremos los dos más comunes pondríamos un 2
        ##Al hacer Counter(lista).most_common(1)[0] nos devolverá el valor del primer indice de la lista → (“manzana”,3)
        ## Al hacer Counter(lista).most_common(1)[0][0] nos devolverá el valor del primer indice de la tupla → “manzana”, que es lo que queremos
lista = ['manzana', 'pera','manzana','naranja','pera','manzana']
print(elemento_mas_comun(lista))
      
# 24. Ejercicio:  Define una función que tome un número y retorne un diccionario con la tabla de multiplicar de ese número del 1 al 10. 
def tabla_de_multiplicar(numero):
  return {i: numero * i for i in range(1, 11)}
 
print(tabla_de_multiplicar(7))

# 25. Ejercicio:  Define una función que tome una cadena y retorne un diccionario con la cantidad de apariciones de cada caracter en la cadena. 
def contar_caracteres(cadena):
  return {caracter: cadena.count(caracter) for caracter in cadena}

print(contar_caracteres("Todos los días."))

# 26. Ejercicio:  Define una función que tome dos listas y retorne la lista de elementos que no están en ambas listas. 
def elementos_no_comunes(lista1, lista2):
  return list(set(lista1) ^ set(lista2))  ## ese símbolo ^, python lo interpreta internamente como diferencia simétrica, es decir aquellos elementos que estén en un conjutno pero no en otro, que es lo que pide el ejercicio.

print(elementos_no_comunes([18, 19, 20, 21], [21, 22, 23, 24]))

# 27. Ejercicio:  Define una función que tome una lista y retorne la lista sin duplicados.
def eliminar_duplicados(lista):
  return list(set(lista))

print(eliminar_duplicados([18, 19, 19, 20, 20, 21]))

# 28. Ejercicio:  Define una función que reciba un número entero positivo y retorne la suma de los cuadrados de todos los números pares menores o iguales a ese número. 
def suma_cuadrados_pares(n):
  return sum(i**2 for i in range(2, n+1, 2))

print(suma_cuadrados_pares(8))

# 29. Ejercicio:  Define una función que reciba una lista de números y retorne el promedio de los números en la lista. 
def promedio(lista):
  return sum(lista) / len(lista)

print(promedio([10, 15, 20, 25, 30]))

# 30. Ejercicio:  Define una función que reciba una lista de cadenas y retorne la cadena más larga en la lista. 
def cadena_mas_larga(lista):
  return max(lista, key=len)  

print(cadena_mas_larga(["como", "pasaste", "ayer"]))

# 31. Ejercicio: Define una función que reciba un número entero n y retorne una lista con los n primeros números primos. 
def es_primo(num): 
  if num < 2:
    return False
  else:
    for i in range(2, int(num ** 0.5) + 1): 
      if num % i == 0: 
        return False 
      else:
        return True

def primeros_n_primos(n):
  primos = []
  numero = 2
  while len(primos) < n:
    if es_primo(numero):
      primos.append(numero)
    numero += 1
  return primos

print(primeros_n_primos(5))

# 32. Ejercicio: Define una función que reciba una cadena y retorne la misma cadena pero con las palabras en orden inverso. 
def invertir_palabras(cadena): 
  return ' '.join(cadena.split()[::-1]) 

print(invertir_palabras("No, quiero ir."))

# 33. Ejercicio: Escribe una función que reciba una lista de tuplas y retorne una lista ordenada basada en el último elemento de cada tupla. 
def ordenar_por_ultimo_elemento(tuplas):
  return sorted(tuplas, key=lambda x: x[-1]) 

print(ordenar_por_ultimo_elemento([(5, 7), (8, 6), (9, 1)])) 
    ## Explicación: Lamda es una forma alternativa de definir una función en python (de forma anónima, sin nombre). Esta compuetas de: 
          # lambda → Palabra reservada para crear este tipo de funciones
          # x → Parametro de la funcion
          # : x[-1] → El codigo de la funcion
          # Es como hacer def sin_nombre(x): return x[-1]
          # x[-1] no hace el inverso, es otra forma de expresar el indice de una lista. Tienes dos formas de indicar indices, la tradicional: 0,1,2,3,… (de izquierda a derecha) o con números negativos: -1,-2,-3,… (de derecha a izquierda). Al poner -1 empieza por la derecha y obtienes el primer elemento (mirando desde la derecha recuerda). Como se expresa para x, es decir, para cada tupla, obtendra el primer valor desde la derecha: (5,7) → 7 , (8,6) → 6, …


# 34. Ejercicio: Define una función que reciba una cadena y retorne la cantidad de letras vocales en la cadena. 
def contar_vocales(cadena):
  suma = 0
  for letra in cadena.lower():
    if letra in 'aeiou':
      suma += 1
  return suma

print(contar_vocales("Estoy estudiando")) 

# 35. Ejercicio: Define una función que reciba un número entero y retorne True si es un número primo, de lo contrario retorne False. 
def es_primo(num): 
  if num < 2:
    return False 
  for i in range(2, int(num ** 0.5) + 1):  ## num ** 0.5 hace referencia a la raíz cuadrada de un numero
    if num % i == 0: 
      return False 
    else:
     return True 
print(es_primo(8))

## Lo de usar la raiz cuadra es por temas de eficiencia, si un número no es primo, al menos uno de sus divisores debe ser menor o igual a su raíz cuadrada