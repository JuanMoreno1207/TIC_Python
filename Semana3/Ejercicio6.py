#Construir diccionario

Tareas ={
    "01":{
        "Descripcion":"Ir a mercar",
        "Estado":"Pendiente",
        "Tiempo":60
    },
    "02":{
        "Descripcion":"Estudiar",
        "Estado":"Pendiente",
        "Tiempo":180
    },
    "03":{
        "Descripcion":"Hacer ejercicio",
        "Estado":"Pendiente",
        "Tiempo":60
    }
}

print("\n-- Aplicacion CRUD TareasPendientes --\n")
print("1. Adicionar tarea")
print("2. Consultar tarea")
print("3. Actualizar tarea")
print("4. Eliminar tarea")
print("5. Salir")

opcion=int(input("Seleccione la opcion a realizar: "))

#Agregar tarea (Create)
if opcion == 1:
    print()
    print("-->Creando Tarea")
    idproducto=input("Ingrese un idproducto: ")
    DescPro=input("Ingrese la descricpcion del producto: ")
    EstPro=input("ingrese el estado del producto: ")
    TiemPro=input("Ingrese el tiempo del producto: ")
    tareanueva = {
        "Descripcion":DescPro,
        "Estado":EstPro,
        "Tiempo":TiemPro
    }   
    Tareas[idproducto]=tareanueva
    for idproducto, diccionario in Tareas.items(): 
        print(idproducto, "-", end=" ")
        for Llave, valor in diccionario.items(): 
            print("",valor , end=" ,")
        print()
#Consultar tarea (Read)
#El parametro end : contiene la forma en como culmina el print(), por defecto es con una nueva linea
#.items convierte el diccionario en tuplas
elif opcion == 2:
    print()
    print("-->Consultando tareas")
    for idproducto, diccionario in Tareas.items(): 
        print(idproducto, "-", end=" ")
        for Llave, valor in diccionario.items(): 
            print("",valor , end=" ,")
        print()
#Actualizar tarea (Update)
elif opcion == 3:
    print()
    print("-->Actualizando tarea")
    IdProductoC=input("Ingrese un ID de tarea a modificar : ")
    NuDes=input("Nueva descripcion : ")
    NuEsta=input("Nuevo estado : ")
    NuTiem=input("Nuevo Tiempo : ")
    TareaAct={
        "Descripcion":NuDes,
        "Estado":NuEsta,
        "Tiempo":NuTiem
    }
    Tareas[IdProductoC]=TareaAct
    print("Tarea Actualizada")
    for idproducto, diccionario in Tareas.items(): 
        print(idproducto, "-", end=" ")
        for Llave, valor in diccionario.items(): 
            print("",valor , end=" ,")
        print()
#Eliminar tarea (Delete)
elif opcion == 4:
    print()
    print("-->Eliminando tarea")
    IdproductoD=input("Ingrese un ID de tarea a eliminar : ")
    Tareas.pop(IdproductoD)
    print("Tarea eliminada")
    for idproducto, diccionario in Tareas.items(): 
        print(idproducto, "-", end=" ")
        for Llave, valor in diccionario.items(): 
            print("",valor , end=" ,")
        print()
#Salir 
elif opcion == 5:
    print()
    print("-->Cerrando programa")

#print(Tareas.items())
