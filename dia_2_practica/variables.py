# 'Dia 2:30 dias de programacion en Python'
    # Declaracion de variables y asignacion de valores
First_name = 'Ignacio'  #nombre y valor
Last_name = 'Mendez'    #apellido y valor
Full_name = First_name + ' ' + Last_name    #nombre completo
Country = 'Mexico'  #pais
City = 'CDMX'      #ciudad
Age = 33         #edad
Year = 2026      #año
is_married = False  #casado o no
is_true = True    #verdadero o falso
is_light_on = True  #luz prendida o apagada

# Verificar tipos de datos
print(type(First_name))
print(type(Last_name))
print(type(Full_name))
print(type(Country))
print(type(City))
print(type(Age))
print(type(Year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

len_first_name = len(First_name)  #longitud del nombre
print(len_first_name)
len_Last_name = len(Last_name)    #longitud del apellido
print(len_Last_name)
compare_len = len_first_name > len(Last_name)  #comparar longitudes de nombre y apellido
print(compare_len)
num_one = 5 #numero uno
print(num_one)
num_two = 4 #numero dos
print(num_two)
total_suma = num_one + num_two #suma
print(total_suma)
diff = num_two - num_one #resta
print(diff)
prod = num_one * num_two #multiplicacion
print(prod)
div = num_two / num_one #division
print(div)
div_de_modulo = num_two % num_one #modulo
print(div_de_modulo)
exp = num_one ** num_two #exponenciacion
print(exp)
floor_div = num_two // num_one #division entera
print(floor_div)

#ejercicio adicional
radius = 30  #radio
pi = 3.14    #valor de pi
area_of_circle = pi * radius ** 2  #area del circulo
circum_of_circle = 2 * pi * radius  #circunferencia del circulo

    # 1. Pedimos el radio al usuario
# Usamos float() porque el radio puede tener decimales (ej. 10.5)
radio_usuario = float(input("Escribe el valor del radio: "))

    # 2. Definimos pi
pi = 3.14159

    # 3. Calculamos el área usando la potencia **
area_calculada = pi * (radio_usuario ** 2)

    # 4. Mostramos el resultado
print(f"Para un radio de {radio_usuario}, el área es: {area_calculada}")

# 1. Obtenemos los datos del usuario usando la función input()
first_name = input("Introduce tu nombre: ")
last_name = input("Introduce tu apellido: ")
country = input("¿En qué país vives?: ")

# 2. Convertimos la edad a entero (int) para poder hacer cálculos después
age = int(input("¿Cuál es tu edad?: "))

# 3. Mostramos un resumen para verificar que se guardaron bien
print("\n--- Registro Completado ---")
print(f"Usuario: {first_name} {last_name}")
print(f"País: {country}")
print(f"Edad: {age} años")

# FIN DIA 2