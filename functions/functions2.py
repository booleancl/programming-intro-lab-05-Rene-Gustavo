# Nuestra primera funcion
def songs():
    print("No te pares frente a mi")
    print("con esa mirada tan hiriente")


songs()
print(type(songs))

# Las funciones, también se pueden usar dentro de otras funciones
def chorus():
    songs()
    songs()

chorus()