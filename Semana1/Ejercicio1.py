# Declaramos variabe tipo entero
var_int = 50
# declaramos variable de tipo float, double
var_pi = 3.1416
# declaramos variable de tipo cadena de texto
var_str = "Grupo_58"
# declaramaos variable de tipo boolean
var_bo = False
# declaramos variable tipo diccionario (Array)
var_dict = {
    "nombre": "Juliana",
    "apellido": "Correa",
    "edad": 37
}
# modificar campo del diccionario
var_dict["nombre"] = "Juan M"
# agregar campo al diccionario
var_dict["Peso"] = 75.5
# eliminar campo del diccionario, elimina el campos segun KEY y retorna el valor
var_dict.pop("apellido")

# imprimir valores
print("El nombre de la persona es " +  var_dict["nombre"] + " y tiene la edad de " + str(var_dict["edad"]))
print("El nombre de la persona es " +  var_dict["nombre"] + " y tiene la edad de", var_dict["edad"])
# Se puede imprimir de la siguiente manera usando corchetes "Interpolation" y comilla sencilla (nunca se puede usar comilla doble dentro de otra comilla doble y viceversa)
# aparte usando la funcion "f-string" al principio del str "string"
print(f"El nombre de la persona es {var_dict['nombre']} y tiene la edad de {var_dict['edad']}")
# funcion "f-string"
print(f"Variable string {var_str} variable entera {var_int} variable float {var_pi}")
# funcion .format
print("El nombre de la persona es {} y tiene la edad de {}".format(var_dict["nombre"],var_dict["edad"]))