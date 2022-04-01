# Funciones con Parámetros
def print_param(daddy):
    print(daddy)
    print(daddy)

# No es necesario que el nombre del objeto que vamos a pasar como argumento sea el mismo que el nombre del parámetro
print_param(77)

singer = "marcianeke"
print_param(singer)

# Volumen de una esfera que recibe un parámetro que es el radio
# Fórmula 4/3 pi r3
def volume(radio): 
  result = 4/3 * 3.1416 * radio ** 3  
  print(result)

big = 7 
small = 2
volume(big)
volume(small)

def multiply_by_2(number):
    number = number * 2
    print(number)

multiply_by_2(big)
print(big)    

# Función de dos parámetros

def concat_strings(str1,str2):
    longstr = str1 + " " + str2
    print(longstr)

text1 = "pasito a pasito"
text2 = "suave suavecito"
concat_strings(text1,text2)