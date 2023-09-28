import math
import random
#HOMEWORK: INTRODUCCION A PYTHON
#En estas primeras 6 preguntas, utiliza print() para la respuesta.
#Crea una variable "string", puede contener lo que quieras:
nombre = "Antonio Arzate"
print (nombre)

# Crea una variable numérica, puede ser cualquier número:
num = 4
print(num)

# Crea una variable booleana:
verdadero = True
falso = False
print (verdadero, falso)

# Resuelve el siguiente problema matemático; 5 - 7:
a = 5
b = 7
c = b-a
print(c)

# Resuelve el siguiente problema matemático; 40 * 5:
x = 40
y = 5
z = x*y
print(z)

# Resuelve el siguiente problema matemático; nuevoModulo = 21 % 5:
g = 21
h = 5
i = g % h
print(i)

#Los próximos 22 problemas, deberás completar la función.
#Tu código irá dentro de la función.
#Asegúrate que usas "return" cuando la función te lo pida.
#Pista: "print()" NO fucionará.
#No cambies los nombres de las funciones.

def devolverString(str):
  ## "Return" la string provista: str
    return str
resultado = devolverString(str)


def suma(x, y):
  # "x" e "y" son números
  # Suma "x" e "y" juntos y devuelve el valor
    resultadosuma = x + y
    return resultadosuma


def resta(x, y):
  # Resta "y" de "x" y devuelve el valor
    resultadoresta = x - y
    return resultadoresta


def multiplica(x, y):
  # Multiplica "x" por "y" y devuelve el valor
    resultadomul = x * y
    return resultadomul

def divide(x, y):
  # Divide "x" entre "y" y devuelve el valor
    resultadodiv = x / y
    return resultadodiv


def sonIguales(x, y):
  # Devuelve "true" si "x" e "y" son iguales
  # De lo contrario, devuelve "false"
    if x == y:
        return True
    else:
        return False


def tienenMismaLongitud(str1, str2):
  # Devuelve "true" si las dos strings tienen la misma longitud
  # De lo contrario, devuelve "false"
    if str1 == str2:
        return True
    else:
        return False


def menosQueNoventa(num):
  # Devuelve "true" si el argumento de la función "num" es menor que noventa
  # De lo contrario, devuelve "false"
    if num > 90:
        return True
    else:
        return False

def mayorQueCincuenta(num):
  # Devuelve "true" si el argumento de la función "num" es mayor que cincuenta
  # De lo contrario, devuelve "false"
    if num < 50:
        return True
    else:
        return False


def obtenerResto(x, y):
  # Obten el resto de la división de "x" entre "y"
    return x % y

def esPar(num):
  # Devuelve "true" si "num" es par
  # De lo contrario, devuelve "false"
    if num / 2 == 0:
        return True
    else:
        return False

def esImpar(num):
  # Devuelve "true" si "num" es impar
  # De lo contrario, devuelve "false"
    if num / 2 != 0:
        return True
    else:
        return False


def elevarAlCuadrado(num):
  # Devuelve el valor de "num" elevado al cuadrado
  # ojo: No es raiz cuadrada!
    return num ** 2


def elevarAlCubo(num):
  # Devuelve el valor de "num" elevado al cubo
    return num ** 3

def elevar(num, exponent):
  # Devuelve el valor de "num" elevado al exponente dado en "exponent"
    return num ** exponent

def redondearNumero(num):
  # Redondea "num" al entero más próximo y devuélvelo
    return round(num)

def redondearHaciaArriba(num):
  # Redondea "num" hacia arriba (al próximo entero) y devuélvelo
    return math.ceil(num)

def numeroRandom():
  #Generar un número al azar entre 0 y 1 y devolverlo
  #Pista: investigá qué hace el método Math.random()
    return random.random()
#La función random.random() de Python genera un número decimal aleatorio en el rango [0, 1).
#Esto significa que el número puede ser igual a 0 pero nunca igual a 1.

def esPositivo(numero):
  # La función va a recibir un entero. Devuelve como resultado una cadena de texto que indica si el número es positivo o negativo.
  # Si el número es positivo, devolver ---> "Es positivo"
  # Si el número es negativo, devolver ---> "Es negativo"
  # Si el número es 0, devuelve false
  
    if numero > 0:
        return "Es positivo"
    elif numero < 0:
        return "Es negativo"
    else:
        return False

def agregarSimboloExclamacion(str):
  #Agrega un símbolo de exclamación al final de la string "str" y devuelve una nueva string
  #Ejemplo: "hello world" pasaría a ser "hello world!"
    return str + "!"


def combinarNombres(nombre, apellido):
  # Devuelve "nombre" y "apellido" combinados en una string y separados por un espacio.
  # Ejemplo: "Eres", "Nombre"
    return nombre + "," + apellido


def obtenerSaludo(nombre):
  # Toma la string "nombre" y concatena otras string en la cadena para que tome la siguiente forma:
  # "Martin" -> "Hola Martin!"
    saludo = "¡Hola" + nombre +"!"
    return saludo

def obtenerAreaRectangulo(alto, ancho):
  # Retornar el area de un rectángulo teniendo su altura y ancho
    area = alto * ancho
    return area


def retornarPerimetro(lado):
  #Escibe una función a la cual reciba el valor del lado de un cuadrado y retorne su perímetro.
    perimetro = lado + lado + lado + lado
    return perimetro


def areaDelTriangulo(base, altura):
  #Desarrolle una función que calcule el área de un triángulo.
    area = base * altura / 2
    return area


def deEuroAdolar(euro):
  #Supongamos que 1 euro equivale a 1.20 dólares. Escribe un programa que reciba
  #como parámetro un número de euros y calcule el cambio en dólares.
    cambio_euro = 1.20
    dolar = euro * cambio_euro
    return dolar


def esVocal(letra):
  #Escribe una función que reciba una letra y, si es una vocal, muestre el mensaje “Es vocal”. 
  #Verificar si el usuario ingresó un string de más de un carácter, en ese caso, informarle
  #que no se puede procesar el dato mediante el mensaje "Dato incorrecto".
  # Si no es vocal, tambien debe devolver "Dato incorrecto".
  
        # Verificar si la entrada es un string de un solo carácter
    if len(letra) != 1:
        return "Dato incorrecto"
    
    # Convertir la letra a minúsculas para una comparación mayúsculas/minúsculas
    letra = letra.lower()

    # Verificar si la letra es una vocal
    if letra in "aeiou":
        return "Es vocal"
    else:
        return "Dato incorrecto"
#Esta función primero verifica si la entrada
#letra es un string de un solo carácter utilizando la función len()
