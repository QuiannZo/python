'''

Syntaxis of python. 2025

'''

# 1. Variables y Tipos de Datos
x = 10        # Entero
pi = 3.14     # Flotante
name = "Juan" # Cadena de texto
is_valid = True  # Booleano

# 2. Operadores
sum_result = 5 + 3  # Suma
mult_result = 5 * 3 # Multiplicación
div_result = 10 / 2 # División real (5.0)
mod_result = 10 % 3 # Módulo (1)
exp_result = 2 ** 3 # Exponente (8)

# 3. Estructuras de Control
# Condicionales
if x > 5:
    print("Mayor a 5")
elif x == 5:
    print("Es 5")
else:
    print("Menor a 5")

# Bucles
for i in range(5):  # 0 a 4
    print(i)

while x > 0:
    print(x)
    x -= 1

# 4. Listas y Tuplas
lista_vacia = [] # crea una lista vacia
my_list = [1, 2, 3, 4, 5] # List are mutable after their creation.
my_tuple = (1, 2, 3) # Tuples are NOT mutable after their creating, meaning you can't add elements.
my_list.append(6)  # Agregar elemento
print(my_list[0])  # Acceder al primer elemento

# 5. Diccionarios (Key - Value)
my_dict = {"nombre": "Juan", "edad": 25}
print(my_dict["nombre"])  # Acceder a un valor
my_dict["edad"] = 26      # Modificar valor

# 6. Funciones
def saludar(nombre):
    return f"Hola, {nombre}!"
print(saludar("Ana"))

# 7. Clases y Objetos
class Persona:
    def __init__(self, nombre, edad): # Constructor
        self.nombre = nombre
        self.edad = edad
    
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

persona1 = Persona("Carlos", 30)
persona1.mostrar_info()

# 8. Manejo de Excepciones
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("No se puede dividir por cero.")
finally:
    print("Fin del bloque try-except.")

# 9. Manipulación de Archivos
with open("archivo.txt", "w") as f:
    f.write("Hola, mundo!")

with open("archivo.txt", "r") as f:
    contenido = f.read()
    print(contenido)

# 10. Programación Funcional
cuadrados = list(map(lambda x: x ** 2, [1, 2, 3, 4]))
pares = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4]))
print(cuadrados, pares)

# 11. Módulos y Librerías
import math
print(math.sqrt(16))  # Raíz cuadrada

# 12. Decorators. They add functionality to a function without modifying the base function.
def decorador(func): # We define a decorator.
    def wrapper():   # Original function.
        print("Antes de la función")
        func() # The decorator added fn.
        print("Después de la función")
    return wrapper

@decorador
def mensaje(): # This function will substitute "func()" inside "wrapper".
    print("Hola!")

mensaje() # Executes wrapper with "func()" being "mensaje".

# 13. Asyncronic programming. Allows to run second hand operations, like getting I/O without stopping the main program.
import asyncio
async def hola(): #  Asyncronic function. Declared with "async def".
    await asyncio.sleep(1)
    print("Hola Asíncrono")
asyncio.run(hola())

# 13.1. Parallel programming
async def tarea(n):
    print(f"Iniciando tarea {n}")
    await asyncio.sleep(2)
    print(f"Tarea {n} completada")

async def main():
    await asyncio.gather(tarea(1), tarea(2), tarea(3)) # Executes 3 instances of the function "tarea(n)" in parallel.

asyncio.run(main())

'''
📌 Salida (todas las tareas inician casi al mismo tiempo y terminan juntas en 2s):

Iniciando tarea 1
Iniciando tarea 2
Iniciando tarea 3
Tarea 1 completada
Tarea 2 completada
Tarea 3 completada
'''

# 14. List Comprehensions
cuadrados = [x**2 for x in range(10)] # Prints each member squared
print(cuadrados)

# 15. JSON management
import json
data = {"nombre": "Ana", "edad": 22}
data_json = json.dumps(data)  # Convertir a JSON
print(json.loads(data_json))  # Convertir de JSON a diccionario

###########################################
## String functions
###########################################

# Lista de funciones de cadenas en Python con ejemplos de salida
s = "  Hello, World!  "

# strip() - Elimina espacios en blanco al inicio y al final
print(s.strip())  # "Hello, World!"
# lower() - Convierte la cadena a minúsculas
print(s.lower())  # "  hello, world!  "
# upper() - Convierte la cadena a mayúsculas
print(s.upper())  # "  HELLO, WORLD!  "
# replace(old, new) - Reemplaza una subcadena por otra
print(s.replace("Hello", "Hi"))  # "  Hi, World!  "
# split(delimiter) - Divide la cadena en una lista
print(s.split(","))  # ['  Hello', ' World!  ']
# join(iterable) - Une una lista de cadenas en una sola cadena
words = ["Hello", "World"]
print(" ".join(words))  # "Hello World"
# find(sub) - Devuelve la primera posición de la subcadena, -1 si no existe
print(s.find("World"))  # 9
# count(sub) - Cuenta cuántas veces aparece una subcadena
print(s.count("o"))  # 2
# startswith(prefix) - Comprueba si la cadena comienza con un prefijo
print(s.startswith("  Hello"))  # True
# endswith(suffix) - Comprueba si la cadena termina con un sufijo
print(s.endswith("!  "))  # True
# capitalize() - Convierte la primera letra en mayúscula y el resto en minúscula
print("hello world".capitalize())  # "Hello world"
# title() - Convierte la primera letra de cada palabra en mayúscula
print("hello world".title())  # "Hello World"
# swapcase() - Invierte mayúsculas y minúsculas
print("Hello World".swapcase())  # "hELLO wORLD"
# isalpha() - Verifica si la cadena contiene solo letras
print("Hello".isalpha())  # True
# isdigit() - Verifica si la cadena contiene solo dígitos
print("12345".isdigit())  # True
# isalnum() - Verifica si la cadena contiene solo letras y/o números
print("Hello123".isalnum())  # True
# isspace() - Verifica si la cadena contiene solo espacios en blanco
print("   ".isspace())  # True
# len() - Obtener la longitud del string
length = len(s)
# sorted(str) - Ordenar string alfabeticamente
sorted = "".join(sorted(s)) # esa forma es para que sea string y no lista

###########################################
## Data structures
###########################################

############################
### Lists
############################

# crea una lista vacia
lista_vacia = []

len(my_list)        # Obtiene la longitud de la lista (cantidad de elementos) → 6
sum(my_list)        # Suma los elementos (si son numéricos) → 23
min(my_list)        # Obtiene el valor mínimo → 1
max(my_list)        # Obtiene el valor máximo → 9
sorted(my_list)     # Retorna una nueva lista ordenada → [1, 1, 3, 4, 5, 9]
list(reversed(my_list))  # Retorna una nueva lista con el orden invertido → [9, 5, 1, 4, 1, 3]

## Add elements
my_list.append(6)      # Agrega un elemento al final → [3, 1, 4, 1, 5, 9, 6]
my_list.insert(2, 99)  # Inserta '99' en la posición 2 → [3, 1, 99, 4, 1, 5, 9]
my_list.extend([7, 8]) # Agrega múltiples elementos al final → [3, 1, 99, 4, 1, 5, 9, 7, 8]

## Delete elements
my_list.remove(1)   # Elimina la primera aparición de '1' → [3, 99, 4, 1, 5, 9, 7, 8]
my_list.pop()       # Elimina el último elemento y lo retorna → 8 (lista queda sin el 8)
my_list.pop(2)      # Elimina el elemento en la posición 2 → [3, 99, 1, 5, 9, 7]
my_list.clear()     # Elimina todos los elementos → []

## Search elements
my_list = [3, 1, 4, 1, 5, 9]
my_list.index(4)    # Retorna el índice donde aparece el 4 → 2
my_list.count(1)    # Cuenta cuántas veces aparece '1' → 2

## Sort elements
my_list.sort()       # Ordena la lista en orden ascendente (modifica la lista)
my_list.sort(reverse=True)  # Ordena en orden descendente
my_list.reverse()    # Invierte el orden de los elementos

############################
### Hash Maps
############################

# Crear un HashMap (diccionario clave - valor)
mapa = {}
# Agregar un elemento
mapa["clave"] = "valor"
# Obtener un valor
valor = mapa.get("clave")  # Devuelve el valor si existe, sino None
# Actualizar un valor
mapa["clave"] = "nuevo_valor"
# Eliminar un elemento
del mapa["clave"]
# Verificar si una clave existe
existe = "clave" in mapa  # Devuelve True o False
# Recorrer todas las claves
for k in mapa:
    print(k)
# Recorrer todas las claves y valores
for k, v in mapa.items():
    print(f"{k}: {v}")
# Obtener todas las claves
claves = mapa.keys()
# Obtener todos los valores
valores = mapa.values()
# Obtener todos los pares clave-valor
pares = mapa.items()
# Eliminar y obtener un valor
valor_eliminado = mapa.pop("clave", "No encontrado")  # Si la clave no existe, devuelve "No encontrado"
# Eliminar todos los elementos
mapa.clear()
# Obtener tamaño del diccionario
tamaño = len(mapa)
# Copiar un diccionario
nuevo_mapa = mapa.copy()

############################
### Sets
############################

# Crear un set
conjunto = set()

# Agregar elementos
conjunto.add("elemento1")
conjunto.add("elemento2")

# Eliminar un elemento (arroja error si no existe)
conjunto.remove("elemento1")

# Eliminar un elemento sin error si no existe
conjunto.discard("elemento1")

# Verificar si un elemento existe
existe = "elemento2" in conjunto  # Devuelve True o False

# Obtener la cantidad de elementos
tamaño = len(conjunto)

# Recorrer elementos del set
for elemento in conjunto:
    print(elemento)

# Unir dos sets
otro_conjunto = {"elemento3", "elemento4"}
union = conjunto.union(otro_conjunto)  # Combina ambos sets

# Intersección (elementos comunes)
interseccion = conjunto.intersection(otro_conjunto)

# Diferencia (elementos en conjunto que no están en otro_conjunto)
diferencia = conjunto.difference(otro_conjunto)

# Diferencia simétrica (elementos únicos en cada set)
dif_simetrica = conjunto.symmetric_difference(otro_conjunto)

# Eliminar todos los elementos
conjunto.clear()

# Copiar un set
nuevo_conjunto = conjunto.copy()

############################
### Queue (FIFO)
############################

# Crear una cola vacía
queue = deque()

# Agregar elementos a la cola (enqueue)
queue.append("A")
queue.append("B")
queue.append("C")

# Eliminar el primer elemento de la cola (dequeue)
primero = queue.popleft()  # "A"

############################
### Stack (FILO)
############################

# Crear una pila vacía (usando lista)
stack = []

# Agregar elementos a la pila (push)
stack.append(1)
stack.append(2)
stack.append(3)

# Eliminar el último elemento de la pila (pop)
ultimo = stack.pop()  # 3

# Ver el último elemento sin eliminarlo
ultimo = stack[-1]  # 2