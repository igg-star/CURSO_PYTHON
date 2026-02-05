print ("Declara tu edad como variable entera (int) y luego imprime en la consola.")
age = 33

print('mi edad es:', age)

print("Declara tu altura como una variable flotante")
height = 1.75

print('mi altura es:', height)

print("Declara una variable que almacene un numero complejo")
cmplx_num = 3j

print('mi numero complejo es:', cmplx_num)

print("Escriba un script que solicite al usuario ingresar la base y altura de el triangulo y calcular el area de este triangulo (area = 0.5 x bxh)")

base = 20
print('base = 20')
height = 10
print('height = 10')
area_of_triangle = 0.5 * base * height
print('El area del triangulo es:', area_of_triangle)
print(input('Area del triangulo:'))
base = float(input('ingresa la base del triangulo: '))
height = float(input('ingresa la altura del triangulo: '))

print('Escribe un script que solicite al usuario ingresar los lados a, b y c de un triangulo. Calcula el perimetro del triangulo (perimetro = a + b + c)')

side_a = 5
side_b = 4
side_c = 3
perimeter_of_triangle = side_a + side_b + side_c
side_a = float(input('ingresa el lado a del triangulo: '))
side_b = float(input('ingresa el lado b del triangulo: '))
side_c = float(input('ingresa el lado c del triangulo: '))
print('El perimetro del triangulo es:', perimeter_of_triangle)

print('calcula el largo y el ancho de un rectangulo usando las instrucciones.' \
'calcula su area (area = largo x ancho) y perimetro (perimetro = 2 x (largo + ancho))')
largo = float(input('ingresa el largo del rectangulo: '))
ancho = float(input('ingresa el ancho del rectangulo: '))

area_of_rectangle = largo * ancho

perimeter_of_rectangle = 2 * (largo + ancho)

print('El area del rectangulo es:', area_of_rectangle)
print('El perimetro del rectangulo es:', perimeter_of_rectangle)

print('Obtén el radio de un círculo usando las instrucciones. ' \
'Calcula el área (área = pi x r x r) ' \
'y la circunferencia (c = 2 x pi x r), donde pi = 3,14.')

pi = 3.14
radius = float(input('ingresa el radio del circulo: '))
area = pi * radius * radius
circunferencia = 2 * pi * radius
print('El area del circulo es:', area)
print('La circunferencia del circulo es:', circunferencia)

print('Calcular la pendiente, ' \
'la intersección con el eje x y' \
' la intersección con el eje y de y = 2x -2')
m = 2  # pendiente
b = -2 # Intersección con el eje y
inter_x = -b / m
print('Pendiente (m):', m)
print('Intersección con el eje b:', b)
print('Intersección con el eje x:', inter_x)

print('La pendiente es (m = y² - y²/x² - x²).' \
'Halla la pendiente y la distancia euclidiana entre los puntos'
'(2, 2) y (6, 10).')
x1, y1 = 2, 2
x2, y2 = 6, 10
m = (y2 - y1) / (x2 - x1)
distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print('Pendiente es:', m)
print('Distancia euclidiana es:', distance)

print('Compare las pendientes en las tareas 8 y 9.')
pendiente_tarea_8 = 2
pendiente_tarea_9 = (10 - 2) / (6 - 2) # Esto da 2.0
son_iguales = pendiente_tarea_8 == pendiente_tarea_9
es_mayor = pendiente_tarea_9 > pendiente_tarea_8
son_diferente = pendiente_tarea_8 != pendiente_tarea_9
print('¿Las pendientes son iguales?:', son_iguales)
print('¿La pendiente 9 es mayor que la de la tarea 8?:', es_mayor)
print('¿Las pendientes son diferentes?:', son_diferente)

print('Calcula el valor de y (y = x^2 + 6x + 9).' \
' Intenta usar diferentes valores de x ' \
'y determina en qué valor de x y será 0.')
x = 0
y = x**2 + 6*x + 9
print('si x vale 0, y es:', y)

x = -2
y = x**2 + 6*x + 9
print('si x vale -2, y es:', y)

x = -3
y = x**2 + 6*x + 9
print('si x vale -3, y es:', y)

print("es Y igual a 0 cuando X es -3?:", y == 0)

print('Encuentra la longitud de python y dragon y haz una afirmación de comparación falsa')
len_python = len('python')
len_dragon = len('dragon')
print('Longitud de python:', len_python)
print('Longitud de dragon:', len_dragon)
false_aff = len_python > len_dragon
print('¿es la longitud de python mayor que la de dragon?:', false_aff)

en_python = 'on' in 'python'
en_dragon = 'on' in 'dragon'
res_final = en_python and en_dragon
print("esta 'on' en python?", en_python)
print("esta 'on' en dragon?", en_dragon)
print('¿está "on" en python y dragon?:', res_final)
 
print('Espero que este curso no esté lleno de jerga . Usa el operador "in" para comprobar si hay jerga en la oración.')
frase = 'Espero que este curso no esté lleno de jerga.'
hay_jerga = 'jerga' in frase
print('frase a revisar:', frase)
print('¿Hay jerga en la frase?:', hay_jerga)

print('No hay on tanto en dragon como en python')
word1 = 'dragon'
word2 = 'python'
si_esta_en_ambas = ('on' in word1) and ('on' in word2)
no_esta_en_ambas = not si_esta_en_ambas
print("'on' esta en ambas palabras?:", si_esta_en_ambas)
print("'on' no esta en ambas palabras?:", no_esta_en_ambas)

# Encuentra la longitud del texto de Python y convierte el valor a flotante y a cadena
texto = 'python'
longitud = len(texto)
flotante = float(longitud)
cadena = str(flotante)
print("Ejercicio 1:", cadena)
# Explicación: Medimos la palabra, la volvimos número con decimal y luego la "dibujamos" como texto.

# ¿Cómo se comprueba si un número es par o no con Python?
# Los números pares son divisibles por 2 y el resto es cero.
numero = 10
es_par = (numero % 2) == 0
print("¿Es 10 par?:", es_par)
# Explicación: El % busca lo que sobra. Si sobran 0 manzanas al repartir entre 2, es par.

# Comprueba si la división del piso de 7 por 3 es igual al valor int convertido de 2,7.
division_piso = 7 // 3
valor_int = int(2.7)
print("¿División de piso es igual a int(2.7)?:", division_piso == valor_int)
# Explicación: // quita decimales hacia abajo, int() solo los corta. Ambos dan 2.

# Comprueba si el tipo de '10' es igual al tipo de 10
comparacion_tipos = type('10') == type(10)
print("¿Tipo de '10' es igual al tipo de 10?:", comparacion_tipos)
# Explicación: Uno es texto (letras) y el otro es número real. No son iguales.

# Comprueba si int('9.8') es igual a 10
# Nota: int('9.8') da error directo, por eso usamos float primero
chequeo_9_8 = int(float('9.8')) == 10
print("¿int(float('9.8')) es igual a 10?:", chequeo_9_8)
# Explicación: '9.8' se vuelve 9.8, luego el int lo corta a 9. Y 9 no es 10.

# Script que solicita horas y tarifa para calcular el salario semanal
horas = float(input("Enter hours: "))
tarifa = float(input("Enter rate per hour: "))
salario = horas * tarifa
print("Your weekly earning is", salario)

# Script que solicita años y calcula segundos vividos (supón 100 años)
años_vividos = float(input("Enter number of years you have lived: "))
# Segundos en un año: 365 * 24 * 60 * 60
segundos = años_vividos * 31536000
print("You have lived for", int(segundos), "seconds.")

#FIN DEL DIA 3