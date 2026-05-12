#Bienvenida en print

#Ingreso de datos de productos: El sistema debe permitir ingresar 
# datos básicos de los productos: nombre, categoría, y 
# precio (sin centavos).
#  Estos datos deben almacenarse en una lista, donde cada producto sea
#  representado/a como una sublista de tres elementos (nombre, categoría, y precio).

#Visualización de productos registrados: El programa debe incluir 
# una funcionalidad para mostrar en pantalla todos los productos 
# ingresados. La información debe presentarse de manera ordenada y 
# legible, con cada producto numerado.

#Eliminación de productos: El sistema debe permitir eliminar 
# un producto de la lista, identificándolo por su posición (número)
#  en la lista.

#Búsqueda de productos: El sistema debe permitir buscar productos 
# por su nombre. Si encuentra coincidencias, debe mostrar la 
# información completa de los productos que coincidan. Si no hay 
# coincidencias, debe informar que no se encontraron resultados.


""""
Requisitos

Usar listas para almacenar y gestionar los datos. 

Incorporar bucles while y for según corresponda. 

Validar entradas del usuario o usuaria, asegurándote de que no
 se ingresen datos vacíos o incorrectos.

Utilizar condicionales para gestionar las opciones del menú y 
las validaciones necesarias.

Presentar un menú que permita elegir entre las funcionalidades 
disponibles: agregar productos, visualizar productos, buscar productos
 y eliminar productos.

El programa debe continuar funcionando hasta que se elija una opción
 para salir.
"""

""""
Consejos

Usá lo aprendido sobre listas y bucles para gestionar los datos 
y recorrerlos.

Recordá validar las entradas utilizando condicionales.

 Utilizá las herramientas vistas para organizar y presentar la 
 información de manera clara.
"""



import time


salir = False
allitems= []
categorielist = ["frutas y verduras", "Almacen", "Carnicería", "ferretería", "Mascotas","otros"]
#bucle principal
while not salir:

    #Bienvenida en print
    print(" _____________________")
    print("|Bienvenido al sistema|")
    print("|Seleccione una opción|")
    print("|                     |")
    print("|1 - agregar producto |")
    print("|2 - ver productos    |")
    print("|3 - borrar productos |")
    print("|4 - buscar productos |")
    print("|5 - salir            |")
    print("|_____________________|")
    option = input ("Seleccione opción").strip()
    print(f"Elegiste: {option}")
    name = ""
    categorie = ""
    cost = ""


    match option:

        #agregar productos
        case "1":
            print("Agregar producto")
            name = input ("Ingrese Nombre del Producto").strip()
            while len(name) < 3:
                print (f"'{name}' es muy corto")
                name = input ("Ingrese Nombre del Producto").strip().capitalize()
            print(" ________________________")
            print("|seleccione una categoría|")
            print("|1 - frutas y verduras   |")
            print("|2 - almacen             |")
            print("|3 - Carnicería          |")
            print("|4 - Ferretería          |")
            print("|5 - mascotas            |")
            print("|6 - otros               |")
            print("|________________________|")
            categorie = input ().strip()
            if categorie.isnumeric():
                categorie = int(categorie)

            while categorie < 1 or categorie > len(categorielist):
                categorie = input("poné solo el número").strip()
                if categorie.isnumeric():
                    categorie = int (categorie)
            print (f"seleccionaste la categoría {categorielist[categorie-1]}")
           
           
            price = input("Ingrese Precio").strip()
            while not price.isnumeric() or int(price) < 1:
                price = input("Ingrese un precio válido").strip()

            price = int(price)

            individualproduct = [name, categorie, price]
            allitems.append(individualproduct)

            



            
            




        # ver productos
        case "2":
            print("Ver productos")
            for numero, i in enumerate(allitems):
                print(numero + 1, i, categorielist[i[1]-1])
        

        # Borrar productos
        case "3":
            print("Borrar productos")
            errase = input ("ingrese el número del producto a borrar").strip()
            if errase.isnumeric() :
                errase = int (errase)
                if 1 <= errase <= len(allitems):
                    print(f"Borrando producto {errase}: {allitems[errase-1]}")
                    confirm = input ("Confirmar? Y/N").strip().capitalize()
                    if confirm == "Y":
                        print (f"Borrando{allitems[errase-1]}")
                        allitems.pop(errase-1)
                    else:
                        print ("Seleccionaste una opción distinta a Y, volviendo a menú principal")
                        continue
                elif int(errase) > len(allitems):
                    print ("El número es mas grande de lo debido, volviendo a menú principal") 
            else:
                print ("Selección inválida, volviendo a menú principal")

        case "4":



            # Buscar productos

            print ("Buscar Productos!")
            search = input("ingresá el producto a buscar!").strip().capitalize()
            found = False

            for numero, i in enumerate(allitems):
                if search in i[0].capitalize():
                    print (numero + 1, i[0])
                    found = True

            if not found:
                print ("Producto no encontrado!")

            """print("Buscar productos")

            search = input("Ingrese nombre a buscar: ").strip().lower()

            found = False

            for numero, i in enumerate(allitems):

                if search in i[0].lower():

                    print(
                    numero + 1,
                    i[0],
                    categorielist[i[1]-1],
                    i[2]
                     )

                found = True

            if not found:
                print("No se encontraron productos")

"""
        case "5":
            salir = True
            
        case _:
            print("Opción inválida")






print ("Hasta luego!")
time.sleep (3)