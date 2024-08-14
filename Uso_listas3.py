#crear para un almacen un sistema que permita almacenar los datos de sus productos y cantidades
import os
#Crear una lista
productos=[]
precio=[]


while True:
    os.system("cls")
    print("\t \tMenu de opciones\t\n")
    print("1, Ingresar producto......:")
    print (" 2,Mostrar producto.......:")
    print("3, Buscar producto......:")
    print(" 4, Modificar producto......:")
    print(" 5, Eliminar producto......:")
    print("6, Salir de la aplicacion......:" )
    opc=int(input("Seleccione la operacion......:"))
    #Valida la opcion
    if opc==1:
        os.system("cls")
        print("1, modulo ingresar producto\n")
        print("****en constitucion****")
        print("*******************")
        #captura de datos
        pro=input("Ingrese producto............:")
        pre=float(input("Ingresar el precio....:"))
        #asignar a lista
        productos.append(pro)
        precio.append(pre)
        #confirmar
        print("Producto registrado correctamente")
        print("****************")
        os.system("pause")
    elif opc==2:
        os.system("cls")
        print("2, modulo mostrar producto")
        print("*** En construccion***")
        print("**************")
        if productos:
            print("***Reporte de productos*****")
            #recorrer lista
            for t in range(len(productos)): 
                print(f" producto.....:{productos[t]}${precio[t]}")
        else:
            print("**** No hay productos ingresados****")
        
        os.system("pause")
    elif opc==3:
        os.system("cls")
        print("3, modulo buscar producto")
        print("*** En construccion***")
        print("**************")
        buzz=input("Producto A Buscar.......:")
        meg=False
        for t in range(len(productos)):
            if productos[t]==buzz:
                print("producto si existe......")
                print(f" producto.....:{productos[t]}${precio[t]}")
                existe=True
                break
        if not existe:
            print("***La lista esta vacia o \nel producto no esta registrado****")    
        os.system("pause")
    elif opc==4:
        os.system("cls")
        print("4, modulo modificar producto")
        print("*** En construccion***")
        os.system("pause")
    elif opc==5:
        os.system("cls")
        print("5, modulo eliminar producto")
        print("*** En construccion***")
        os.system("pause")
    elif opc==6:
        os.system("cls")
        print("6, modulo salir de la aplicacion")
        break
        os.system("pause")
    else:
        os.system("cls")
        print("selecciono una opcion invalida\n")
        print("*** en construccion****")
        os.system("pause")
