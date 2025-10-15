import os
from time import sleep

#EJERCICIO FINAL MODULO 1 - CRUD EMPRESAS
#NOMBRE : HEINZ VICTOR ROQUE TRUJILLO


dic_empresas = {
    '201323818318':{
        'razon_social': 'MICKI SAC',
        'direccion_fiscal':'CALLE LOS ALAMOS 123',
    }
}

ANCHO = 60

while(True):
    os.system("clear")
    print("="*ANCHO)
    print(" " * 10 + "GESTIÓN DE EMPRESAS")
    print("="*ANCHO)
    print("""
         [1] REGISTRAR EMPRESA
         [2] MOSTRAR EMPRESAS
         [3] ACTUALIZAR EMPRESA
         [4] ELIMINAR EMPRESA
         [5] SALIR
          """)
    print("=" * ANCHO)
    opcion = int(input("INGRESE OPCION : "))
    os.system("clear")
    if opcion == 1:
        print("=" * ANCHO)
        print(" " * 10 + "REGISTRAR EMPRESA")
        print("=" * ANCHO)

        ruc = input("Ingrese RUC: ")
        razon_social = input("Ingrese Razon Social: ")
        direccion_fiscal = input("Ingrese Direccion Fiscal: ")
        dic_nuevo_empresa = {
            'razon_social': razon_social,
            'direccion_fiscal': direccion_fiscal
        }
        dic_empresas[ruc] = dic_nuevo_empresa
        print("Empresa registrada exitosamente.")
    elif opcion == 2:
        print("=" * ANCHO)
        print(" " * 10 + "MOSTRAR EMPRESAS")
        print("=" * ANCHO)
        
        for ruc,info in dic_empresas.items():
            print(f"RUC : {ruc}")
            print(f"Razon Social : {info['razon_social']}")
            print(f"Direccion Fiscal : {info['direccion_fiscal']}")
            print("*"*ANCHO)
    elif opcion == 3:
        print("=" * ANCHO)
        print(" " * 10 + "ACTUALIZAR EMPRESA")
        print("=" * ANCHO)
        ruc = input("Ingrese RUC de la empresa a actualizar: ")
        if ruc in dic_empresas:
            print(f"Empresa encontrada: {dic_empresas[ruc]['razon_social']}")
            nuevo_razon_social = input("Ingrese nueva razon social (dejar en blanco para no cambiar): ")
            nuevo_direccion_fiscal = input("Ingrese nueva direccion fiscal (dejar en blanco para no cambiar): ")
            if nuevo_razon_social:
                dic_empresas[ruc]['razon_social'] = nuevo_razon_social
            if nuevo_direccion_fiscal:
                dic_empresas[ruc]['direccion_fiscal'] = nuevo_direccion_fiscal

            print("Empresa actualizada exitosamente.")
        else:
            print("Empresa no encontrada.")
    elif opcion == 4:
        print("=" * ANCHO)
        print(" " * 10 + "ELIMINAR EMPRESA")
        print("=" * ANCHO)
        ruc = input("Ingrese RUC de la empresa a eliminar: ")
        if ruc in dic_empresas:
            del dic_empresas[ruc]
            print("Empresa eliminada exitosamente.")
        else:
            print("Empresa no encontrada.")
        
    elif opcion == 5:
        print("=" * ANCHO)
        print(" " * 10 + "SALIENDO DEL SISTEMA...")
        print("=" * ANCHO)
        sleep(2)
        break
    
    input("Presione ENTER para continuar...")