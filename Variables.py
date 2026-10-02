# No se que estoy haciendo
# Que es una variable? Es la representación de un objeto. 
# Vamos a crear una variable  
nombre = "Juan"
print(nombre)
print(type(nombre)) 
nombre2 = 1234
print(nombre2)
print(type(nombre2))
# Las comillas dejan de escribir en una linea, si se ponen 3 se puede escribir en varias lineas
"AJAJJAJAJA"
"""Ahora puedo escribir en varias lineas
y no afecta el codigo, WOOOW"""

# Las comillas dejan escribir codigo, pero el lenguaje lo leerá

variable = 123456
print(type(variable)) 
variable = 1234.56
print(type(variable))
a = "Luis Raymundo"
b = 20265220 # Las variables tienen que tener un proposito y sentido, también "varian" de ahi el nombre
# El codigo es secuencial, si no esta arriba, los de abajo no saben que existen.
""" El tipo de datos en pyton es dinamico, dependiendo de lo que se le ponga 
es el valor que toma, no es necesario declarar el tipo de dato.
Es sumamente recomendablle poner nombres con sentido a las variables y no "A, B, J, etc". """

monto = 100
cobrarle = True
print(type(cobrarle))
Monto_a_cobrar = monto * cobrarle
print(Monto_a_cobrar)
""" El bool multiplicado por una variable de numero no da error, porque es un numero True es 1 y False es 0,
 por lo que al multiplicar por True se obtiene el mismo valor de la variable y al multiplicar por False se obtiene 0."""
# Incluso si se multiplica por un string, el resultado seria la palabra repetida el numero de veces por el cual se multiplica
# Si se suma, ahi si da error, pero un texto + texto los concatena

andrea = 25.25
carlitos = andrea
andrea = 14.23
# carlitos = andrea. Si lo dejamos asi no va a funcionar como suma, me dara el valor nuevo
# Lo que se tiene que hacer es sumarle otro carlitos para que tome su valor anterior
carlitos = carlitos + andrea
print(round(carlitos, 2))


compras = 134.23
compras += 200 # el "+=" es igual a sumarlo por si mismo. Ayuda a procesos reitativos
print(compras, compras) # La coma es para separar los valores, si tuviera varios me arrojaria los 2
# El orden es el siguiente "función(argumento(argumentos))", el print seria la funcion


Compra = 15.50
usuario = "Aracely"
texto = "le compro a Carlitos"
print(usuario, texto, Compra)  
""" si lo sumara daria error, no se puede combinar 2 tipos de datos, 
en cambio si decido usar la suma, pero con datos iguales si funcionaria la suma (+)"""
# Puedo combinar tipos de variables usando f-strings, que es una forma de formatear texto y variables
print(f"{usuario} le compro a Carlitos ${round(Compra * 1.10, 2)}") # Al poner los corchetes es una forma de poner "codigo" dentro de un texto
#Round es una funcion que redondea el numero a la cantidad de decimales que le indiquemos, en este caso 2
""" Hay argumentos que tienen valores por defecto, como el round, el cual, si no le pongo nada,
me pone 0. """