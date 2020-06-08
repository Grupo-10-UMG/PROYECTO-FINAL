while True:
    import os
    os.system("cls")
    print("**********BIENVENIDO AL PROGRAMA**********")
    print("*****SELECCIONA UNA OPCION*****")
    print("1. MODULO INVENTARIO")
    print("2. MODULO COMPRAS")
    print("3. MODULO CLIENTES")
    print("4. MODULO VENTAS")
    print("5. MODULO FACTURACION")
    print("6. SALIR")
    opcion=int(input("INGRESE LA OPCION QUE DESEA: "))
    os.system("cls")
    if opcion==1:

        #-----------------------------------------------------------------------------------------------------------
        #--------------Elaborado por José Francisco Armas Sosa---------------------
        #--------------Carnet 1990 00 2168 ---------------------
        #--------------Universidad Mariano Galvez---------------------
        #--------------Programacion 1 seccion "A"---------------------
        #--------------Modulo de inventarios---------------------
        #--------------Este modulo no contempla la actualizacion del campo cantidad para evitar que se hagan operaciones turbias ---------------------
        #-----------------------------------------------------------------------------------------------------------

        import sqlite3

        import os

        import pprint

        #-----------------------------------------------------------------------------------------------------------

        #--------------insertar registros INVENTARIO  ---------------------

        #-----------------------------------------------------------------------------------------------------------



        def pr_inserta_datos():

            miConexion=sqlite3.connect("Vehiculos")



            # para crear tabla se crea cursor

            miCursor=miConexion.cursor()



            miCursor.execute("CREATE TABLE IF NOT EXISTS INVENTARIO (cod_vehiculo integer PRIMARY KEY AUTOINCREMENT, marca varchar, modelo varchar, anio number(4), descripcion varchar(255), Cantidad number, precio_compra number, precio_venta number)")



            #Codigo 

            #Marca

            #Modelo

            #Año

            #Descripción

            #Cantidad

            #Precio Compra

            #Precio Venta



            #v_cod_vehiculo = int(input(f"Ingrese codigo vehiculo: "))

            v_marca = (input(f"Ingrese marca vehiculo: "))

            v_modelo = (input(f"Ingrese modelo vehiculo: "))

            v_anio = int(input(f"Ingrese anio vehiculo: "))

            v_descripcion = (input(f"Ingrese descripcion vehiculo: "))

            v_cantidad = int(input(f"Ingrese cantidad vehiculo: "))

            v_precio_compra = float(input(f"Ingrese precio de compra vehiculo: "))

            v_precio_venta = float(input(f"Ingrese precio de venta vehiculo: "))


            miCursor.execute(f"""insert into INVENTARIO Values(NULL,

            '{v_marca}',

            '{v_modelo}',

            {v_anio},

            '{v_descripcion}',

            {v_cantidad},

            {v_precio_compra}, 

            {v_precio_venta} )""")



            miConexion.commit()

            print("Datos guardados exitosamente! \n")

            miConexion.close()



        #-----------------------------------------------------------------------------------------------------------

        #-------------- Listar Registros ---------------------

        #-----------------------------------------------------------------------------------------------------------

        def pr_listar():

            print("Lista de Existencias de Vehiculos")

            miConexion=sqlite3.connect("Vehiculos")

            # para crear tabla se crea cursor

            miCursor=miConexion.cursor()



            miCursor.execute("Select * from INVENTARIO")

            

            listado_inventario=miCursor.fetchall()

            #pprint.pprint(listado_inventario)

            print( "Codigo, Marca, Modelo, Año, Descripción, Cantidad, Precio Compra, Precio Venta")

            for ls_vehiculos in listado_inventario:

                print(ls_vehiculos)

            #    pprint.pprint(ls_vehiculos)

            print("Fin del listado" + '\n')

            v_continuar = input("presione ENTER para continuar... ")

            v_continuar = v_continuar+"null" # solo lo puse para que no marque feo



            miConexion.commit()

            miConexion.close()

        #-----------------------------------------------------------------------------------------------------------

        #-------------- Actualizar Registros ---------------------

        #-----------------------------------------------------------------------------------------------------------

        def pr_actualiza():

            pr_listar()

            miConexion=sqlite3.connect("Vehiculos")

            # para crear tabla se crea cursor

            miCursor=miConexion.cursor()

            v_cod_vehiculo = int(input("Ingrese el codigo del vehiculo que desea modificar o '0' para salir: "))

            if v_cod_vehiculo != 0:

                v_marca = (input(f"Ingrese marca vehiculo: "))

                v_modelo = (input(f"Ingrese modelo vehiculo: "))

                v_anio = int(input(f"Ingrese anio vehiculo: "))

                v_descripcion = (input(f"Ingrese descripcion vehiculo: "))

                v_cantidad = int(input(f"Ingrese cantidad vehiculo: "))

                v_precio_compra = float(input(f"Ingrese precio de compra vehiculo: "))

                v_precio_venta = float(input(f"Ingrese precio de venta vehiculo: "))

                miCursor.execute(f"""UPDATE INVENTARIO SET

                    marca = '{v_marca}',

                    modelo = '{v_modelo}',

                    anio ={v_anio},

                    descripcion = '{v_descripcion}',

                    Cantidad = {v_cantidad},

                    precio_compra = {v_precio_compra}, 

                    precio_venta = {v_precio_venta} where cod_vehiculo = {v_cod_vehiculo}""")

            miConexion.commit()

            print("Datos guardados exitosamente! \n")

            miConexion.close()

        #-----------------------------------------------------------------------------------------------------------

        #-------------- Busca Registros ---------------------

        #-----------------------------------------------------------------------------------------------------------

        def pr_busqueda():

            print("Lista de Existencias de Vehiculos")

            print("Criterios de busqueda: ")

            print("1. Codigo de Vehiculo")

            print("2. Marca de Vehiculo")

            print("3. Modelo de Vehiculo")

            print("4. Año de Vehiculo")

            print("5. Descripcion de Vehiculo")

            print("6. Precio de Compra de Vehiculo")

            print("7. Precio de Venta")

            

            v_criterio=int(input("Ingrese el numero del campo para el criterio de busqueda: "))

            v_valor_busqueda=""

            v_valor_busqueda=(input(f"Ingrese el valor de busqueda: "))

            if v_criterio == 1:

                v_where = (f"cod_vehiculo = {v_valor_busqueda} ")

            elif v_criterio == 2:

                v_where = (f"marca like '%{v_valor_busqueda}%'")

            elif v_criterio == 3:

                v_where = (f"Modelo like '%{v_valor_busqueda}%'")

            elif v_criterio == 4:

                v_where = (f"Año = {v_valor_busqueda} ")

            elif v_criterio == 5:

                v_where = (f"Descripcion = '%{v_valor_busqueda}%'")

            elif v_criterio == 6:

                v_where = (f"precio_compra = {v_valor_busqueda} ")

            elif v_criterio == 4:

                v_where = (f"precio_venta = {v_valor_busqueda} ")

            

            

            miConexion=sqlite3.connect("Vehiculos")

            

            miCursor=miConexion.cursor()



            miCursor.execute(f"Select * from INVENTARIO WHERE {v_where} " )

            

            listado_inventario=miCursor.fetchall()

            #pprint.pprint(listado_inventario)

            print( "Codigo, Marca, Modelo, Año, Descripción, Cantidad, Precio Compra, Precio Venta")

            for ls_vehiculos in listado_inventario:

                print(ls_vehiculos)

            #    pprint.pprint(ls_vehiculos)

            print("Fin del listado" + '\n')

            miConexion.commit()

            miConexion.close()

            v_continuar = input("presione ENTER para continuar... ")

            v_continuar = v_continuar+"null" # solo lo puse para que no marque feo vscode


        #-----------------------------------------------------------------------------------------------------------

        #--------------Menu principal de Inventario---------------------

        #-----------------------------------------------------------------------------------------------------------

        v_opcion=0

        while True:

            #os.system("cls")



            print("Menu principal Modulo de Inventarios:" + '\n' )

            print("1. Ingreso de datos al modulo" + '\n' )

            print("2. Modificacion de registros" + '\n' )

            print("3. Reporte de existencias" + '\n' )

            print("4. Busquedas de existencias" + '\n' )

            print("5. Salir" + '\n' )

            

            while True:

                try:

                    v_opcion = int(input("ingrese opcion: "))

                    break

                except ValueError:

                    print("Error de ingreso pruebe nuevamente")



            if v_opcion == 5:

                break

            #print("el valor es" + v_opcion)


            if v_opcion == 1:

                pr_inserta_datos()

            elif v_opcion == 2:

                    pr_actualiza()

            elif v_opcion == 3:

                pr_listar()

            elif v_opcion == 4:

                pr_busqueda(    )

    elif opcion==2:
        

        #-----------------------------------------------------------------------------------------------------------

        #--------------INSERTAR DATOS DE COMPRA---------------------

        #-----------------------------------------------------------------------------------------------------------


        # WILLIAM ABELARDO SATZ MONTOYA
        # 1990-19-23607
        # Ing. en sistemas Sección "A"


        import sqlite3

        import os

        import pprint

        def inserta_compra():

            os.system("cls")

            miConexion=sqlite3.connect("Vehiculos")



            # creacion de tabla de compras

            miCursor=miConexion.cursor()

            miCursor.execute("CREATE TABLE IF NOT EXISTS COMPRAS (Cod_Compra integer PRIMARY KEY, Fecha varchar, Proveedor varchar, Cod_Vehiculo integer, Marca varchar, Modelo varchar, Anio number(4), Descripcion varchar(255), Cantidad number, Precio_Compra number, Precio_Venta number)")

            miCursor.execute("CREATE TABLE IF NOT EXISTS INVENTARIO (Cod_Vehiculo PRIMARY KEY, Marca varchar, Modelo varchar, Anio number(4), Descripcion varchar(255), Cantidad number, Precio_Compra number, Precio_Venta number)")

            

            #RECIBE LOS DATOS QUE SE GUARDAN EN LA BASE DE DATOS

            print("INGRESE LOS DATOS DE LA COMPRAS \n")

            c_num = int((input(f"Ingrese Numero de Compra: ")))

            c_fecha = (input(f"Ingrese Fecha de Compra: "))

            c_proveedor = (input(f"Ingrese el Proveedor: "))

            c_codigo = int(input(f"Codigo del vehiculo: "))

            c_marca = (input(f"Ingrese marca vehiculo: "))

            c_modelo = (input(f"Ingrese modelo vehiculo: "))

            c_anio = int(input(f"Ingrese anio vehiculo: "))

            c_descripcion = (input(f"Ingrese descripcion vehiculo: "))

            c_cantidad = int(input(f"Ingrese cantidad vehiculo: "))

            c_precio_compra = float(input(f"Ingrese precio de compra vehiculo: "))

            c_precio_venta = float(input(f"Ingrese precio de venta vehiculo: "))



            #INSERTAMOS LOS DATOS EN LA TABLA DE COMPRAS

            miCursor.execute(f"""insert into COMPRAS Values({c_num},

            '{c_fecha}',

            '{c_proveedor}',

            {c_codigo},

            '{c_marca}',

            '{c_modelo}',

            {c_anio},

            '{c_descripcion}',

            {c_cantidad},

            {c_precio_compra},
            
            {c_precio_venta})""")

            miConexion.commit()

            print("Datos guardados exitosamente! \n")

            miConexion.close()



            #INSERTAMOS LOS DATOS EN LA TABLA DE INVENTARIO

            miConexion=sqlite3.connect("Vehiculos")

            miCursor=miConexion.cursor()

            miCursor.execute(f"""insert into INVENTARIO Values({c_codigo},

            '{c_marca}',

            '{c_modelo}',

            {c_anio},

            '{c_descripcion}',

            {c_cantidad},

            {c_precio_compra}, 

            {c_precio_venta})""")

            miConexion.commit()

            print("Datos guardados exitosamente! \n")

            miConexion.close()

            os.system("pause")



        #FUNCION PARA ACTUALIZAR LOS DATOS DE UNA COMPRA EN ESPECIFICO

        def actualiza_compra():

            os.system("cls")

            print("Actualizar datos de Compras")

            c_codigo = int(input("Ingrese el Numero de Compra que se Modificara: "))

            if c_codigo != 0:

                c_fecha = (input(f"Ingrese Fecha de Compra: "))

                c_proveedor = (input(f"Ingrese el Proveedor: "))

                c_marca = (input(f"Ingrese marca vehiculo: "))

                c_modelo = (input(f"Ingrese modelo vehiculo: "))

                c_anio = int(input(f"Ingrese anio vehiculo: "))

                c_descripcion = (input(f"Ingrese descripcion vehiculo: "))

                c_cantidad = int(input(f"Ingrese cantidad vehiculo: "))

                c_precio_compra = float(input(f"Ingrese precio de compra vehiculo: "))

                c_precio_venta = float(input(f"Ingrese precio de venta vehiculo: "))

                

                #ACTUALIZAMOS LOS DATOS EN LA TABLA DE VEHICULOS

                miConexion=sqlite3.connect("Vehiculos")

                miCursor=miConexion.cursor()

                miCursor.execute(f"""UPDATE COMPRAS SET

                    Fecha = '{c_fecha}',

                    Proveedor = '{c_proveedor}',

                    Marca = '{c_marca}',

                    Modelo = '{c_modelo}',

                    Anio ={c_anio},

                    Descripcion = '{c_descripcion}',

                    Cantidad = {c_cantidad},

                    Precio_Compra = {c_precio_compra} where Cod_Compra = {c_codigo},
                    
                    Precio_Venta = {c_precio_venta}""")

                miConexion.commit()

                print("Datos Actualizados exitosamente! \n")

                miConexion.close()



                #ACTUALIZAMOS TAMBIEN LOS DATOS EN LA TABLA INVENTARIO

                miConexion=sqlite3.connect("Vehiculos")

                miCursor=miConexion.cursor()

                miCursor.execute(f"""UPDATE INVENTARIO SET

                    Marca = '{c_marca}',

                    Modelo = '{c_modelo}',

                    Anio ={c_anio},

                    Descripcion = '{c_descripcion}',

                    Cantidad = {c_cantidad},

                    Precio_Compra = {c_precio_compra}, 

                    Precio_Venta = {c_precio_venta} where Cod_Vehiculo = {c_codigo}""")

                miConexion.commit()

                print("Datos Actualizados exitosamente! \n")

                miConexion.close()

            os.system("pause")



        #FUNCION PARA MOSTRAS TODAS LAS COMPRAS REALIZADAS

        def lista_compra():

            os.system("cls")

            print("Listado Completo de Compras \n \n")

            miConexion=sqlite3.connect("Vehiculos")

            miCursor=miConexion.cursor()

            miCursor.execute("Select * from COMPRAS")

            lista_compras=miCursor.fetchall()

            print( "Num_Compra, Fecha, Proveedor, Codigo_Vehiculo, Marca, Modelo, Anio, Descripcion, Cantidad, Precio Compra, Precio_venta ")

            for ls_compras in lista_compras:

                print(ls_compras)

            print("\n ----------- Fin del listado -----------" + '\n')

            miConexion.commit()

            miConexion.close()

            os.system("pause")



        #FUNCION PARA BUSCAR COMPRAS EN ESPECIFICO

        def buscar_compra():

            os.system("cls")

            print("Busqueda de Compras \n")

            print("Criterios de busqueda: ")

            print("1. Codigo de Vehiculo")

            print("2. Marca de Vehiculo")

            print("3. Modelo del Vehiculo")



            #PEDIMOS LOS DATOS POR LOS CUALES DESEA BUSCAR LA COMPRA REALIZADA

            c_opcion=int(input("Ingrese el numero del campo para el criterio de busqueda: "))

            c_buscar=(input(f"Ingrese el valor de busqueda: "))

            if c_opcion == 1:

                c_where = (f"cod_vehiculo = {c_buscar} ")

            elif c_opcion == 2:

                c_where = (f"marca like '%{c_buscar}%'")

            elif c_opcion == 3:

                c_where = (f"Modelo like '%{c_buscar}%'")

            

            #REALIZAMOS LA CONSULTA A LA BASE DE DATOS PARA MOSTRAR LA COMPRA QUE SE ESTA BUSCANDO

            miConexion=sqlite3.connect("Vehiculos")

            miCursor=miConexion.cursor()

            miCursor.execute(f"Select * from COMPRAS WHERE {c_where} " )

            lista_compras=miCursor.fetchall()

            print( "Num_Compra, Fecha, Proveedor, Codigo_Vehiculo, Marca, Modelo, Anio, Descripcion, Cantidad, Precio Compra, Precio_Venta ")

            for ls_compras in lista_compras:

                print(ls_compras)

            print("\n ----------- Fin del listado -----------" + '\n')

            miConexion.commit()

            miConexion.close()

            os.system("pause")



        #FUNCION PARA ELIMINAR DATOS DE LA COMPRA

        def eliminar_compra():

            os.system("cls")

            print("Eliminar Compra")



            c_codigo = int(input("Ingrese el Numero De La Compra a Eliminar: "))

            confirmar = int(input(f"\n ADVERTENCIA!: Se eliminaran tambien los registro de Inventario \n \n Seguro Eliminara el Registro No. {c_codigo}: (1=Si / 2=No): "))



            if confirmar == 1:

                #ELIMINAMOS LOS DATOS DE LA TABLA DE COMPRAS

                miConexion=sqlite3.connect("Vehiculos")

                miCursor=miConexion.cursor()

                miCursor.execute(f"""delete from COMPRAS where Cod_Compra = {c_codigo}""")

                miConexion.commit()

                print("Datos Eliminados exitosamente! \n")

                miConexion.close()

                

                #ELIMINAMOS LOS DATOS DE LA TABLA DE INVENTARIO

                miConexion=sqlite3.connect("Vehiculos")

                miCursor=miConexion.cursor()

                miCursor.execute(f"""delete from INVENTARIO where Cod_Vehiculo = {c_codigo}""")

                miConexion.commit()

                print("Datos Eliminados exitosamente! \n")

                miConexion.close()

                os.system("pause")

            elif confirmar == 2:

                print("Cancelando Operacion")

                os.system("pause")

            elif confirmar < 1 or confirmar > 2:

                print("Opcion Incorrecta")

                os.system("pause")

                eliminar_compra()



        # ESTA ES LA FUNCION DEL MENU PRINCIPAL DEL PROGRAMA

        def menu():

            while True:

                os.system("cls")

                print("\n       MODULO DE COMPRAS \n")

                print("  1. Ingreso de Compras")

                print("  2. Modificar Compra")

                print("  3. Muestra Todas las Compras")

                print("  4. Muestra por Criterios")

                print("  5. Eliminar Compra")

                print("  6. Salir")

                print("  Seleccione Opcion")

                opcion = int(input("  "))

                if opcion == 1:

                    inserta_compra()

                elif opcion == 2:

                    actualiza_compra()

                elif opcion == 3:

                    lista_compra()

                elif opcion == 4:

                    buscar_compra()

                elif opcion == 5:

                    eliminar_compra()

                elif opcion == 6:

                    print("Saliendo")
                    break
                    #os.system("pause")

                    #os.system(exit())

                elif opcion < 1 or opcion > 6:

                    print("Opcion Incorrecta")

                    os.system("pause")


        #LLAMAMOS A LA FUNCION MENU PARA QUE SE EJECUTE CUANDO INICE EL PROGRAMA
        menu()

        
        #-----------------------------------------------------------------------------------------------------------

        #--------------insertar registros Clientes  ---------------------

        #-----------------------------------------------------------------------------------------------------------

        #ADOLFO RAFAEL VELÁSQUEZ PAJARITO
        #1990-19-10701
        #INGENIERIA EN SISTEMAS
        #SECCION "A"
    elif opcion==3:
        
        import sqlite3

        import os

        import pprint

        import msvcrt


        def inserta_datos():

            miConexion=sqlite3.connect("Vehiculos")


            # para crear tabla se crea cursor

            miCursor=miConexion.cursor()


            miCursor.execute('''

                CREATE TABLE IF NOT EXISTS CLIENTES (

                ID_CLIENTE INTEGER PRIMARY KEY AUTOINCREMENT, 

                NOMBRE VARCHAR(50), 

                APELLIDO VARCHAR(50),

                DIRECCION VARCHAR(50),

                TELEFONO NUMBER, 

                NIT INTEGER)

            ''')


            #v_cod_vehiculo = int(input(f"Ingrese codigo vehiculo: "))

            c_nombre = (input(f"Ingrese nombre de cliente: "))

            c_apellido = (input(f"Ingrese apellido de cliente: "))

            c_direccion = (input(f"Ingrese direccion de cliente: "))

            c_telefono = (input(f"Ingrese telefono de cliente: "))

            c_nit = int(input(f"Ingrese NIT de cliente: "))


            miCursor.execute(f"""INSERT INTO CLIENTES VALUES(NULL,

            '{c_nombre}',

            '{c_apellido}',

            '{c_direccion}',

            {c_telefono},

            {c_nit} )""")



            miConexion.commit()

            print("Datos guardados exitosamente! \n")

            miConexion.close()



        #-----------------------------------------------------------------------------------------------------------

        #-------------- Busca Registros CLIENTES ---------------------

        #-----------------------------------------------------------------------------------------------------------

        def listar():

            miConexion=sqlite3.connect("Vehiculos")

            # para crear tabla se crea cursor

            miCursor=miConexion.cursor()



            miCursor.execute("SELECT * FROM CLIENTES")

            

            listado_clientes=miCursor.fetchall()

            #pprint.pprint(listado_clientes)

            print( "Codigo, Nombre, Apellido, Dirección, Telefono, NIT")

            for ls_clientes in listado_clientes:

                print(ls_clientes)

            #    pprint.pprint(ls_clientes)

            print("Fin del listado" + '\n')

            #miConexion.close()

            
            c_cod_cliente = int(input("Ingrese el codigo del cliente que desea modificar o '0' para salir: "))

            if c_cod_cliente != 0:

                c_nombre = (input(f"Ingrese Nombre de Cliente: "))

                c_apellido = (input(f"Ingrese Apellido de Cliente: "))

                c_direccion = (input(f"Ingrese Direccion de Cliente: "))

                c_telefono = (input(f"Ingrese Telefono de Cliente: "))

                c_nit = int(input(f"Ingrese NIT de Cliente: "))

                

                miCursor.execute(f"""UPDATE CLIENTES SET

                    NOMBRE = '{c_nombre}',

                    APELLIDO = '{c_apellido}',

                    DIRECCION = '{c_direccion}',

                    TELEFONO = {c_telefono},

                    NIT = {c_nit} WHERE ID_CLIENTE = {c_cod_cliente}""")



                miConexion.commit()

                print("Datos guardados exitosamente! \n")

        #Buscar CLIENTE POR NIT

        def buscar():

            miConexion=sqlite3.connect("Vehiculos")

            # para crear tabla se crea cursor

            miCursor=miConexion.cursor()

            b_nit = int(input(f"Ingrese NIT de Cliente: "))

            if not b_nit:

                    print("Búsqueda inválida")

                    exit()



            sentencia = "SELECT * FROM CLIENTES WHERE NIT LIKE ?;"



            miCursor.execute(sentencia, [ "%{}%".format(b_nit) ])

            clientes=miCursor.fetchall()

            

            print(clientes)

            



            miConexion.commit()

            print("Presione una tecla para continuar...")

            msvcrt.getch()

            miConexion.close()

        #Eliminar CLIENTE

        def eliminar():

            miConexion=sqlite3.connect("Vehiculos")

            # para crear tabla se crea cursor

            miCursor=miConexion.cursor()

            sentencia = "SELECT *,rowid FROM CLIENTES;"

        

            miCursor.execute(sentencia)

            

            clientes=miCursor.fetchall()

            

            print(clientes)

            
            #Pedir id del cliente a editar

            id_cliente = int(input("\nEscribe el id del cliente que quieres eliminar: "))

            if not id_cliente:

                    print("No escribiste nada")

                    exit()

            #Sentencia para eliminar

            sentencia = "DELETE FROM CLIENTES WHERE rowid = ?;"


            #Eliminar el cliente

            miCursor.execute(sentencia, [id_cliente])

            miConexion.commit()

            print("Eliminado con éxito")

            print("Presione una tecla para continuar...")

            msvcrt.getch()

            miConexion.close()

        #-----------------------------------------------------------------------------------------------------------

        #--------------Menu principal MODULO DE CLIENTES---------------------

        #-----------------------------------------------------------------------------------------------------------

        c_opcion=0

        while True:

            os.system("cls")



            print("Menu Modulo de Clientes:" + '\n' )

            print("1. Ingreso de Nuevo Cliente" + '\n' )

            print("2. Modificacion de Registros" + '\n' )

            print("3. Busqueda por NIT" + '\n' )

            print("4. Eliminar Cliente" + '\n' )

            print("5. Salir" + '\n' )



            c_opcion = int(input("ingrese opcion: "))



            if c_opcion == 5:

                break

            #print("el valor es" + c_opcion)


            if c_opcion == 1:

                inserta_datos()

            elif c_opcion == 2:

                listar()

            elif c_opcion == 3:

                    buscar()

            elif c_opcion == 4:

                eliminar()

        #-----------------------------------------------------------------------------------------------------------

        #--------------Menu principal MODULO DE VENTAS---------------------

        #-----------------------------------------------------------------------------------------------------------

    elif opcion==4:

        #BAYRON POYON CHICOL

        #Carnet: 1990-19-23087

        #PROGRAMACION 1 SECCION A



        import sqlite3

        import os

        import pprint

        import msvcrt



        #MODULO VENTAS

        def registra_ventas():

            print("*****INGRESO DE NUEVA VENTA*****")

            miConexion=sqlite3.connect("Vehiculos")


        
            #PARA CREAR TABLA SE CREA CURSOR

            miCursor=miConexion.cursor()



            miCursor.execute('''

                CREATE TABLE IF NOT EXISTS VENTAS (

                CODIGO_VENTA INTEGER PRIMARY KEY AUTOINCREMENT,

                FECHA NUMBER(10),

                COD_INV INTEGER,

                CANTIDAD NUMBER,

                COD_CLIENTE INTEGER)

            ''')



            #v_cod_venta = int(input(f"Ingrese codigo venta: "))

            v_fecha = (input(f"INGRESA LA FECHA: "))

            print("\n")

            print("*****QUE VEHICULO DESEA ADQUIRIR*****")

            miCursor.execute("Select cod_vehiculo, marca, modelo, anio, descripcion, Cantidad, precio_venta from INVENTARIO WHERE CANTIDAD > 0")

            

            listado_inventario=miCursor.fetchall()

            #pprint.pprint(listado_inventario)

            print( "Codigo, Marca, Modelo, Año, Descripción, Cant_Disp, Precio Venta")

            for ls_vehiculos in listado_inventario:

                print(ls_vehiculos)

            #    pprint.pprint(ls_vehiculos)

            print("Fin del listado" + '\n')



            v_cod_inv = (input(f"Ingresa el codigo de inventario: "))



            if not v_cod_inv:

                    print("El codigo de producto aun no existe")

                    exit()

            

            sentencia = "SELECT cod_vehiculo, marca, modelo, anio, descripcion, Cantidad, precio_venta FROM INVENTARIO WHERE cod_vehiculo LIKE ?;"

            

            miCursor.execute(sentencia, [ "%{}%".format(v_cod_inv) ])

            productos=miCursor.fetchone()

            print( "Codigo, Marca, Modelo, Año, Descripción, Cant_Disp, Precio Venta")

            print(productos)



            v_cantidad_prod = int(input(f"CUANTOS DESEA ADQUIRIR: "))

            print("\n")

            print("*****QUIEN ES EL CLIENTE*****")

            miCursor.execute("SELECT * FROM CLIENTES")

            

            listado_clientes=miCursor.fetchall()

            #pprint.pprint(listado_clientes)

            print( "Codigo, Nombre, Apellido, Dirección, Telefono, NIT")

            for ls_clientes in listado_clientes:

                print(ls_clientes)

            #    pprint.pprint(ls_clientes)

            print("Fin del listado" + '\n')



            v_cod_cliente = int(input(f"Selecciona el codigo del cliente: "))

            if not v_cod_cliente:

                print("El cliente no existe")

                exit()

            

            sentencia = "SELECT * FROM CLIENTES WHERE ID_CLIENTE LIKE ?;"

            miCursor.execute(sentencia, [ "%{}%".format(v_cod_cliente) ])

            clientes=miCursor.fetchone()

            print(clientes)



            miCursor.execute(f"""INSERT INTO VENTAS VALUES(NULL,

            '{v_fecha}',

            {v_cod_inv},

            {v_cantidad_prod},

            {v_cod_cliente} )""")



            print("LA VENTA SE HA GUARDADO EXITOSAMENTE, LOS DATOS \n")

            miConexion.commit()

            v_continuar = input("presione ENTER para continuar... ")

            v_continuar = v_continuar+"null" # solo lo puse para que no marque feo

            miConexion.close()



        def lista_registos():

            print("LISTA DE LOS REGISTROS DE VENTA")

            miConexion=sqlite3.connect("Vehiculos")

            # para crear tabla se crea cursor

            miCursor=miConexion.cursor()



            miCursor.execute("""select 

                                a.CODIGO_VENTA, a.Fecha, b.nombre, 

                                b.APELLIDO, c.cod_vehiculo, c.marca, 

                                c.modelo, c.anio, c.descripcion, a.Cantidad, 

                                c.precio_venta 

                                from ventas a, clientes b, INVENTARIO c

                                where a.COD_INV = c.cod_vehiculo

                                and a.COD_CLIENTE = b.ID_CLIENTE

                                order by a.CODIGO_VENTA""")

            

            listado_ventas=miCursor.fetchall()

            #pprint.pprint(listado_ventas)

            print( "CODIGO_VENTA, FECHA, NOMBRE, APELLIDO, CODIGO VEHICULO, MARCA, MODELO, AñO, DESCRIPCION, CANTIDAD, PRECIO VENTA")

            for ls_ventas in listado_ventas:

                print(ls_ventas)

            #    pprint.pprint(ls_venta)



            print("Fin del listado" + '\n')

            v_continuar = input("presione ENTER para continuar... ")

            v_continuar = v_continuar+"null" # solo lo puse para que no marque feo

            miConexion.commit()

            miConexion.close()





        def modificar_registro():

            print("*****MODIFICACION DE LOS REGISTROS DE VENTA*****")

            lista_registos()

            miConexion=sqlite3.connect("Vehiculos")

            miCursor=miConexion.cursor()

            v_cod_venta = int(input("Ingresa el codigo de la venta que desea modoficar o '0' para salir: "))

            if v_cod_venta != 0:

                v_fecha = (input(f"INGRESA LA FECHA: "))

                print("\n")

                print("*****CUAL ES EL VEHICULO QUE VA ADQUIRIR AHORA*****")

                miCursor.execute("Select cod_vehiculo, marca, modelo, anio, descripcion, Cantidad, precio_venta from INVENTARIO")

            

                listado_inventario=miCursor.fetchall()

                #pprint.pprint(listado_inventario)

                print( "Codigo, Marca, Modelo, Año, Descripción, Cant_Disp, Precio Venta")

                for ls_vehiculos in listado_inventario:

                    print(ls_vehiculos)

                #    pprint.pprint(ls_vehiculos)

                print("Fin del listado" + '\n')



                v_cod_inv = (input(f"Ingresa el codigo de inventario: "))



                if not v_cod_inv:

                        print("El codigo de producto aun no existe")

                        exit()

            

                sentencia = "SELECT * FROM INVENTARIO WHERE cod_vehiculo LIKE ?;"

            

                miCursor.execute(sentencia, [ "%{}%".format(v_cod_inv) ])

                productos=miCursor.fetchone()

                print(productos)



                v_cantidad_prod = int(input(f"CUANTOS DESEA ADQUIRIR: "))

                print("\n")

                print("*****QUIEN ES EL CLIENTE*****")

                miCursor.execute("SELECT * FROM CLIENTES")

            

                listado_clientes=miCursor.fetchall()

                #pprint.pprint(listado_clientes)

                print( "Codigo, Nombre, Apellido, Dirección, Telefono, NIT")

                for ls_clientes in listado_clientes:

                    print(ls_clientes)

                #    pprint.pprint(ls_clientes)

                print("Fin del listado" + '\n')



                v_cod_cliente = int(input(f"Selecciona el codigo del cliente: "))

                if not v_cod_cliente:

                    print("El cliente no existe")

                    exit()

            

                sentencia = "SELECT * FROM CLIENTES WHERE ID_CLIENTE LIKE ?;"

                miCursor.execute(sentencia, [ "%{}%".format(v_cod_cliente) ])

                clientes=miCursor.fetchone()

                print(clientes)

                #v_fecha = (input(f"Ingresa la fecha: "))

                #v_cod_inv = int(input(f"Ingresa el codigo de inventario: "))

                #v_cantidad_prod = int(input(f"Ingresa La cantidad: "))

                #v_cod_cliente = int(input(f"Ingresa el codigo del cliente: "))

                

                miCursor.execute(f"""UPDATE VENTAS SET

                    FECHA = '{v_fecha}',

                    COD_INV = {v_cod_inv},

                    CANTIDAD = {v_cantidad_prod},

                    COD_CLIENTE = {v_cod_cliente} WHERE CODIGO_VENTA = {v_cod_venta}""")

                

                print("Se ha modificado correctamente \n")

                v_continuar = input("presione ENTER para continuar... ")

                v_continuar = v_continuar+"null" # solo lo puse para que no marque feo

                miConexion.commit()

                miConexion.close()



        def eliminar_registro():

            print("*****ELIMINACION DE LOS REGISTROS DE VENTA*****")

            miConexion=sqlite3.connect("Vehiculos")

            # para crear tabla se crea cursor

            miCursor=miConexion.cursor()

            sentencia = """select 

                        a.CODIGO_VENTA, a.Fecha, b.nombre, b.APELLIDO, c.cod_vehiculo, c.marca, c.modelo, c.anio, c.descripcion, a.Cantidad, c.precio_venta, a.rowid from ventas a, clientes b, INVENTARIO c

                        where a.COD_INV = c.cod_vehiculo

                        and a.COD_CLIENTE = b.ID_CLIENTE

                        and not exists (select 1 from FACTURAS f where a.CODIGO_VENTA = f.COD_VENTA)

                        order by a.CODIGO_VENTA"""

        

            miCursor.execute(sentencia)

            

            ventas=miCursor.fetchall()

            print("CODIGO_VENTA, FECHA, NOMBRE, APELLIDO, CODIGO VEHICULO, MARCA, MODELO, AñO, DESCRIPCION, CANTIDAD, PRECIO VENTA")

            for datos in ventas:

                

                print(datos)

            

            #Pedir codigo de venta a eliminar

            cod_venta = int(input("\nEscribe el codigo de la venta que quieres eliminar: "))

            if not cod_venta:

                    print("No escribiste un codigo valido")

                    exit()

        

            #Sentencia para eliminar

            sentencia = "DELETE FROM VENTAS WHERE rowid = ?;"

        

            #Eliminar el cliente

            miCursor.execute(sentencia, [cod_venta])

            

            print("Eliminado con éxito")

            v_continuar = input("presione ENTER para continuar... ")

            v_continuar = v_continuar+"null" 

            miConexion.commit()

            #msvcrt.getch()

            miConexion.close()



        def busqueda_registro():

            print("*****BUSQUEDA EN EL REGISTRO DE VENTAS*****")

            miConexion=sqlite3.connect("Vehiculos")

            # para crear tabla se crea cursor

            miCursor=miConexion.cursor()



            cod_venta = int(input(f"Ingrese CODIGO DE VENTA: "))

            

            if not cod_venta:

                    print("Búsqueda inválida")

                    exit()



            sentencia = "SELECT a.CODIGO_VENTA, a.FECHA, b.NOMBRE, b.APELLIDO, c.cod_vehiculo, c.marca, c.modelo, c.anio, c.descripcion, a.CANTIDAD, c.precio_venta FROM VENTAS a, CLIENTES b, INVENTARIO c WHERE COD_INV=cod_vehiculo and COD_CLIENTE=ID_CLIENTE and CODIGO_VENTA LIKE ?;"



            miCursor.execute(sentencia, [ "%{}%".format(cod_venta) ])

            listado_ventas=miCursor.fetchall()

            print("CODIGO_VENTA, FECHA, NOMBRE, APELLIDO, CODIGO VEHICULO, MARCA, MODELO, AñO, DESCRIPCION, CANTIDAD, PRECIO VENTA")

            for ls_ventas in listado_ventas:

                print(ls_ventas)

            

            miConexion.commit()

            print("Presione ENTER para continuar...")

            msvcrt.getch()

            miConexion.close()

        v_op=0

        while True:

            os.system("cls")



            print("*****SUBMENU DE MODULO VENTAS***** \n")

            print("1. Ingreso de Nueva Venta \n")

            print("2. Lista de Ventas \n")

            print("3. Modificacion de Registro \n")

            print("4. Busqueda en Registro \n")

            print("5. Eliminar Registro \n")

            print("6. Salir \n")

            v_op = int(input("Ingrese Opcion: "))



            if v_op == 6:

                break

            if v_op == 1:

                registra_ventas()

            elif v_op == 2:

                    lista_registos()

            elif v_op == 3:

                modificar_registro()

            elif v_op == 4:

                busqueda_registro()

            elif v_op == 5:

                eliminar_registro()


    elif opcion==5:
        
        #-----------------------------------------------------------------------------------------------------------

        #--------------Elaborado por José Francisco Armas Sosa---------------------

        #--------------Carnet 1990 00 2168 ---------------------

        #--------------Universidad Mariano Galvez---------------------

        #--------------Programacion 1 seccion "A"---------------------

        #--------------Modulo de Facturacion---------------------

        #--------------Este modulo no contempla actualizar registrso de facturas por motivos legales ---------------------

        #-----------------------------------------------------------------------------------------------------------



        import sqlite3

        import os

        import pprint



        #-----------------------------------------------------------------------------------------------------------

        #--------------insertar registros  ---------------------

        #-----------------------------------------------------------------------------------------------------------



        def pr_inserta_datos():



            print("  INGRESO DE FACTURAS  ")

            v_fecha = (input(f"INGRESA LA FECHA: "))

            miConexion=sqlite3.connect("Vehiculos")



            # para crear tabla se crea cursor

            miCursor=miConexion.cursor()



            miCursor.execute("""CREATE TABLE IF NOT EXISTS FACTURAS (

                                codigo_factura INTEGER NOT NULL,

                                cod_venta INTEGER NOT NULL,

                                fecha datetime,  

                                Total number,

                                PRIMARY KEY (codigo_factura, cod_venta),

                                FOREIGN KEY (cod_venta) REFERENCES VENTAS (cod_venta))""")

            

            ##################################################Solicita cliente#################################################

            print("***** INGRESE EL CODIGO DEL CLIENTE *****")

            miCursor.execute("SELECT * FROM CLIENTES")



            listado_clientes=miCursor.fetchall()

            #pprint.pprint(listado_clientes)

            print( "Codigo, Nombre, Apellido, Dirección, Telefono, NIT")

            for ls_clientes in listado_clientes:

                print(ls_clientes)

            #    pprint.pprint(ls_clientes)

            print("Fin del listado" + '\n')



            while True:

                try:

                    v_cod_cliente = int(input("ingrese opcion: "))

                    break

                except ValueError:

                    print("El cliente no existe")

            

            sentencia = "SELECT * FROM CLIENTES WHERE ID_CLIENTE LIKE ?;"

            miCursor.execute(sentencia, [ "%{}%".format(v_cod_cliente) ])

            clientes=miCursor.fetchall()

            print(clientes)

            

            #################################################solicita venta######################################################







            print("\n")

            v_correlativo_factura = ''

            # inicio ciclo para guardar varias ventas en una factura

            while True:

                print("*****INGRESE LAS VENTAS PENDIENTES A FACTURAR*****")

                miCursor.execute(f"""select a.CODIGO_VENTA, a.Fecha, b.nombre, 

                                    b.APELLIDO, c.cod_vehiculo, c.marca, 

                                    c.modelo, c.anio, c.descripcion, a.Cantidad, 

                                    c.precio_venta, 

                                    a.Cantidad * c.precio_venta  

                                    from ventas a, clientes b, INVENTARIO c

                                    where a.COD_INV = c.cod_vehiculo

                                    and a.COD_CLIENTE = b.ID_CLIENTE

                                    and b.ID_CLIENTE = {v_cod_cliente}

                                    and not exists (select 1 from FACTURAS F where a.codigo_venta=f.cod_venta) 

                                    order by a.codigo_venta""")

                listado_ventas=miCursor.fetchall()

                #pprint.pprint(listado_inventario)

                print( "CODIGO_VENTA, FECHA, NOMBRE, APELLIDO, COD VEHICULO, MARCA, MODELO, AñO, DESCRIPCION, CANTIDAD, PRECIO VENTA, TOTAL")

                for ls_ventas in listado_ventas:

                    print(ls_ventas)

                print("Fin del listado" + '\n')

                while True:

                        try:

                            v_cod_venta = int(input("Ingresa el codigo de venta: "))

                            break

                        except ValueError:

                            print("El ingreso no existe")

                if v_correlativo_factura == '':

                    miCursor.execute("Select max(codigo_factura) + 1 from FACTURAS")

                    sql_corr_fac=(miCursor.fetchall())

                    v_correlativo_factura = (sql_corr_fac[0][0])

                    #print(int(sql_corr_fac[0][0]))

                    if v_correlativo_factura == '':

                        v_correlativo_factura=1

                

                miCursor.execute(f"""insert into FACTURAS Values('{v_correlativo_factura}',

                                '{v_cod_venta}',

                                '{v_fecha}',

                                '0')""")

                miConexion.commit()

                print("Datos guardados exitosamente! \n")



                v_pide_mas = (input("Desea ingresar mas ventas? SI/NO: "))

                if v_pide_mas == 'NO':

                    break

            ############################### impresion de factura ########################################   

            #MOSTRAR PRIMERO EL CLIENTE

            print("\n")

            print("\n")

            print(f"IMPRESION DE FACTURA NUMERO {v_correlativo_factura}")

            print("\n")

            print("AUTOVENTAS LA HUESERA")

            print("DETALLE DEL CLIENTE: ")

            print("Codigo, Nombre, Apellido, Dirección, Telefono, NIT")

            print(clientes)

            print("\n")

            print("DETALLE DE COMPRA:")

            print("CODIGO_VENTA, FECHA, CODIGO VEHICULO, MARCA, MODELO, AñO, DESCRIPCION, CANTIDAD, PRECIO VENTA, TOTAL")

            miCursor.execute(f"""select a.CODIGO_VENTA, a.Fecha, c.cod_vehiculo, c.marca, 

                                c.modelo, c.anio, c.descripcion, a.Cantidad, 

                                c.precio_venta, 

                                a.Cantidad * c.precio_venta  

                                from ventas a, clientes b, INVENTARIO c

                                where a.COD_INV = c.cod_vehiculo

                                and a.COD_CLIENTE = b.ID_CLIENTE

                                and exists (select 1 from FACTURAS F where a.codigo_venta=f.cod_venta and f.codigo_factura = {v_correlativo_factura} ) 

                                order by a.codigo_venta""")

            sql_detalle=(miCursor.fetchall())        

            for ls_det in sql_detalle:

                print(ls_det)

            miConexion.commit()

            miCursor.execute(f"""SELECT SUM(a.cantidad*c.precio_venta) 

                                from ventas a,  INVENTARIO c

                                where a.COD_INV = c.cod_vehiculo

                                and exists (select 1 from FACTURAS F 

                                                where a.codigo_venta=f.cod_venta 

                                                and f.codigo_factura = {v_correlativo_factura} ) 

                                """)

            sql_total=(miCursor.fetchall())

            v_gran_total=float(sql_total[0][0])

            print("\n")

            print(f"SU TOTAL A CANCELAR ES DE: {v_gran_total:,.2f} " )

            print("GRACIAS POR SU COMPRA")

            v_continuar = input("presione ENTER para continuar... ")

            v_continuar = v_continuar+"null" # solo lo puse para que no marque feo

            miConexion.commit()

                

            miCursor.execute(f"""UPDATE""")



            miConexion.close()

            ######################################################################################################################



        #-----------------------------------------------------------------------------------------------------------

        #--------------lista registros  ---------------------

        #-----------------------------------------------------------------------------------------------------------



        def pr_listar():

            miConexion=sqlite3.connect("Vehiculos")

            miCursor=miConexion.cursor()

            print("*****INGRESE LAS VENTAS PENDIENTES A FACTURAR*****")

            miCursor.execute(f"""select f.codigo_factura, f.fecha, a.CODIGO_VENTA, a.Fecha, b.nombre, 

                                b.APELLIDO, b.nit, c.cod_vehiculo, c.marca, 

                                c.modelo, c.anio, c.descripcion, a.Cantidad, 

                                c.precio_venta, 

                                a.Cantidad * c.precio_venta  

                                from ventas a, clientes b, INVENTARIO c, FACTURAS F

                                where a.COD_INV = c.cod_vehiculo

                                and a.COD_CLIENTE = b.ID_CLIENTE

                                and a.codigo_venta=f.cod_venta 

                                order by a.codigo_venta""")

            

            listado_ventas=miCursor.fetchall()

            print( "CODIGO FACTURA, FECHA FACTURA, CODIGO_VENTA, FECHA V, NOMBRE, APELLIDO, NIT, COD VEHICULO, MARCA, MODELO, AñO, DESCRIPCION, CANTIDAD, PRECIO VENTA, TOTAL")

            for ls_ventas in listado_ventas:

                print(ls_ventas)



            print("Fin del listado" + '\n')

            miConexion.commit()

            miConexion.close()    

            v_continuar = input("presione ENTER para continuar... ")

            v_continuar = v_continuar+"null" # solo lo puse para que no marque feo





        #-----------------------------------------------------------------------------------------------------------

        #--------------Busca registros  ---------------------

        #-----------------------------------------------------------------------------------------------------------

        def pr_busqueda():

            v_op_busqueda=0

            v_criterio_busqueda = ''

            while True:

                print("  BUSQUEDA DE FACTURAS   ")

                print("Criterios de busqueda: ")

                print("1. POR NIT DEL CLIENTE")

                print("2. POR NOMBRE DEL CLIENTE")

                print("3. POR APELLIDO DEL CLIENTE")

                print("4. POR RANGO DE FECHA")

                print("5. SALIR")

                while True:

                    try:

                        v_op_busqueda = int(input("ingrese opcion: "))

                        break

                    except ValueError:

                        print("Error de ingreso pruebe nuevamente")



                if v_op_busqueda == 5:

                    break

        

                if v_op_busqueda == 1:

                    while True:

                        try:

                            v_valor_busqueda = (input("ingrese b.nit: "))

                            v_criterio_busqueda = (f"and b.nit LIKE '%{v_valor_busqueda}%' ")

                            break

                        except ValueError:

                            print("Error de ingreso pruebe nuevamente")

                elif v_op_busqueda == 2:

                    while True:

                        try:

                            v_valor_busqueda = (input("ingrese nombre: "))

                            v_criterio_busqueda = (f"and b.nombre LIKE '%{v_valor_busqueda}%' ")

                            break

                        except ValueError:

                            print("Error de ingreso pruebe nuevamente")

                elif v_op_busqueda == 3:

                    while True:

                        try:

                            v_valor_busqueda = (input("ingrese Apellido: "))

                            v_criterio_busqueda = (f"and b.apellido LIKE '%{v_valor_busqueda}%' ")

                            break

                        except ValueError:

                            print("Error de ingreso pruebe nuevamente")

                elif v_op_busqueda == 4:

                    while True:

                        try:

                            v_valor_busqueda = (input("ingrese fehca inicial: "))

                            v_valor_busqueda_b = (input("ingrese fehca final: "))

                            v_criterio_busqueda = (f"and f.fecha between '{v_valor_busqueda}' and '{v_valor_busqueda_b}' ")

                            break

                        except ValueError:

                            print("Error de ingreso pruebe nuevamente")



                miConexion=sqlite3.connect("Vehiculos")

                miCursor=miConexion.cursor()

                print("*****INGRESE LAS VENTAS PENDIENTES A FACTURAR*****")

                miCursor.execute(f"""select f.codigo_factura, f.fecha, a.CODIGO_VENTA, a.Fecha, b.nombre, 

                                    b.APELLIDO, b.nit, c.cod_vehiculo, c.marca, 

                                    c.modelo, c.anio, c.descripcion, a.Cantidad, 

                                    c.precio_venta, 

                                    a.Cantidad * c.precio_venta  

                                    from ventas a, clientes b, INVENTARIO c, FACTURAS F

                                    where a.COD_INV = c.cod_vehiculo

                                    and a.COD_CLIENTE = b.ID_CLIENTE

                                    and a.codigo_venta=f.cod_venta 

                                    {v_criterio_busqueda}

                                    order by a.codigo_venta""")

                

                listado_ventas=miCursor.fetchall()

                print( "CODIGO FACTURA, FECHA FACTURA, CODIGO_VENTA, FECHA V, NOMBRE, APELLIDO, NIT, COD VEHICULO, MARCA, MODELO, AñO, DESCRIPCION, CANTIDAD, PRECIO VENTA, TOTAL")

                for ls_ventas in listado_ventas:

                    print(ls_ventas)



                print("Fin del listado" + '\n')

                miConexion.commit()

                miConexion.close()    

                v_continuar = input("presione ENTER para continuar... ")

                v_continuar = v_continuar+"null" # solo lo puse para que no marque feo

        #-----------------------------------------------------------------------------------------------------------

        #--------------MENU PRINCIPAL   ---------------------

        #-----------------------------------------------------------------------------------------------------------



        v_opcion=0

        while True:

            #os.system("cls")



            print("Menu principal Modulo de Facturación:" + '\n' )

            print("1. Creacion de facturas" + '\n' )

            print("2. Reporte de facturación" + '\n' )

            print("3. Busquedas de facturas" + '\n' )

            print("4. Salir" + '\n' )

            

            while True:

                try:

                    v_opcion = int(input("ingrese opcion: "))

                    break

                except ValueError:

                    print("Error de ingreso pruebe nuevamente")



            if v_opcion == 4:

                break

            #print("el valor es" + v_opcion)





            if v_opcion == 1:

                pr_inserta_datos()

            elif v_opcion == 2:

                pr_listar()

            elif v_opcion == 3:

                pr_busqueda()

    elif opcion==6:
            break
            
