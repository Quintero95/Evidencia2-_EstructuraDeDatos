# Evidencia 2, Estructura de datos y su procesamiento.

#aqui importamos las colecciones que necesitaremos 
from collections import namedtuple
from datetime import datetime
import os
import csv

def checarFecha(fecha):
    dia = fecha[0:2]
    mes = fecha[3:5]
    anio = fecha[6:10]
    fechaNuvoFormato = año + "-" + mes + "-" + dia
    return fechaNuvoFormato


#en esta parte tenemos el diccionario y lista que utilizamos para almacenar los datos de las ventas 
Venta = namedtuple('Ventas', ('descripcion', 'cantidadVenta', 'precioVenta', 'fechaVenta'))
DiccionarioVentas = {}
ListaVentas = []
separador = ('-' * 45)
subtotal = 0

print('Bienvenido(a) al negocio de ventas de computo')
print(separador)

#Aqui se ira construyendo la estructura del archivo csv, juntos con las filas que se van agregando
if os.path.exists('Ventas_Registradas.csv'):
    print('Ya existe un archivo \"Ventas_Registradas.csv" en el mismo directorio')
    with open('Ventas_Registradas.csv','r')as archivo:
        ContenidoArchivo = csv.reader(archivo)
        
        for fila in ContenidoArchivo: # Lector fila por fila del archivo
            contadorTamañoFila = 5
            detectoAlMenosUnElementoEnFila = False

            while True:
                if len(fila) == contadorTamañoFila: # Solo 1 elemento en fila
                    if detectoAlMenosUnElementoEnFila == True:
                    
                        folio = int(fila[0])
                        
                        buscadorTemporal = 21
                        datoExtraidoTemporal = fila[contadorInternoTamañoFila-4][buscadorTemporal:len(fila[contadorInternoTamañoFila-4])-1]
                        print("\nDescripción:", datoExtraidoTemporal)
                        descripcion = str(datoExtraidoTemporal)
                        
                        buscadorTemporal = 15
                        datoExtraidoTemporal = fila[contadorInternoTamañoFila-3][buscadorTemporal:len(fila[contadorInternoTamañoFila-3])]
                        print("Cantidad vendida:", datoExtraidoTemporal)
                        cantidadVenta = int(datoExtraidoTemporal)
                        
                        buscadorTemporal = 13
                        datoExtraidoTemporal = fila[contadorInternoTamañoFila-2][buscadorTemporal:len(fila[contadorInternoTamañoFila-2])]
                        print("Precio Venta:", datoExtraidoTemporal)
                        precioVenta = float(datoExtraidoTemporal)
                        
                        buscadorTemporal = 13
                        datoExtraidoTemporal = fila[contadorInternoTamañoFila-1][buscadorTemporal:len(fila[contadorInternoTamañoFila-1])-3]
                        print("Fecha venta:", datoExtraidoTemporal)
                        fecha = str(datoExtraidoTemporal)
                        
                        # Inyección de datos a Diccionario
                        organizacionVenta = Venta(descripcion,cantidadVenta, precioVenta, fecha)
                        ListaVentas.append(organizacionVenta)
                        DiccionarioVentas[folio] = ListaVentas
                        
                        break
                    
                    ListaVentas=[] # Limpieza de la lista

                    print("\n-- Venta ID: {} (se detectó solo 1 producto)".format(fila[0]))
                    folio = int(fila[0])
                    
                    buscadorTemporal = 21
                    datoExtraidoTemporal = fila[1][buscadorTemporal:len(fila[1])-1]
                    print("\nDescripción:", datoExtraidoTemporal)
                    descripcion = str(datoExtraidoTemporal)
                    
                    buscadorTemporal = 15
                    datoExtraidoTemporal = fila[2][buscadorTemporal:len(fila[2])]
                    print("Cantidad vendida:", datoExtraidoTemporal)
                    cantidadVenta = int(datoExtraidoTemporal)
                    
                    buscadorTemporal = 13
                    datoExtraidoTemporal = fila[3][buscadorTemporal:len(fila[3])]
                    print("Precio Venta:", datoExtraidoTemporal)
                    precioVenta = float(datoExtraidoTemporal)
                    
                    buscadorTemporal = 13
                    datoExtraidoTemporal = fila[4][buscadorTemporal:len(fila[4])-3]
                    print("Fecha venta:", datoExtraidoTemporal)
                    fecha = str(datoExtraidoTemporal)
                    
                    # Inyección de datos a Diccionario
                    organizacionVenta = Venta(descripcion,cantidadVenta, precioVenta, fecha)
                    ListaVentas.append(organizacionVenta)
                    DiccionarioVentas[folio] = ListaVentas
                    
                    break
    
                else: # En caso de que haya más de 1 elemento en la misma fila
                    
                    
                    if detectoAlMenosUnElementoEnFila == False:
                        print("\n-- Venta ID: {} (se detectó más de 1 producto)".format(fila[0]))
                        folio = int(fila[0])
                    
                    contadorInternoTamañoFila = contadorTamañoFila
                    buscadorTemporal = 21
                    datoExtraidoTemporal = fila[contadorInternoTamañoFila-4][buscadorTemporal:len(fila[contadorInternoTamañoFila-4])-1]
                    print("\nDescripción:", datoExtraidoTemporal)
                    descripcion = str(datoExtraidoTemporal)
                    
                    buscadorTemporal = 15
                    datoExtraidoTemporal = fila[contadorInternoTamañoFila-3][buscadorTemporal:len(fila[contadorInternoTamañoFila-3])]
                    print("Cantidad vendida:", datoExtraidoTemporal)
                    cantidadVenta = int(datoExtraidoTemporal)
                    
                    buscadorTemporal = 13
                    datoExtraidoTemporal = fila[contadorInternoTamañoFila-2][buscadorTemporal:len(fila[contadorInternoTamañoFila-2])]
                    print("Precio Venta:", datoExtraidoTemporal)
                    precioVenta = float(datoExtraidoTemporal)
                    
                    buscadorTemporal = 13
                    datoExtraidoTemporal = fila[contadorInternoTamañoFila-1][buscadorTemporal:len(fila[contadorInternoTamañoFila-1])-2]
                    print("Fecha venta:", datoExtraidoTemporal)
                    fecha = str(datoExtraidoTemporal)
                    
                    # Inyección de datos a Diccionario
                    organizacionVenta = Venta(descripcion,cantidadVenta, precioVenta, fecha)
                    ListaVentas.append(organizacionVenta) #<<<<<<<
                    DiccionarioVentas[folio] = ListaVentas
            
                    contadorInternoTamañoFila += 4
                    
                    detectoAlMenosUnElementoEnFila = True
                    
                    
                contadorTamañoFila = contadorTamañoFila + 4 # Para encontrar siguiente conjunto dentro de Fila
            numFila += 1
        
            print("\nAgregado a Diccionario venta ID {}".format(fila[0]))
   
            ListaVentas=[] # Limpieza de la lista
   
    print("\n-- Se ha importado del .csv\n")
    print(separador)

else:
    print("No existe archivo .csv creado")
    print(separador)

##Aqui se hizo el menu principal de las opciones a ofrecer para el usuario 
def Menu():
    opcion = int(input('Menú de opciones:\n[1] Registrar una venta\n[2] Consultar una venta\n[3] Reporte de ventas de fecha\n[4] Mostrar todas las ventas\n[5] Salir y guardar archivo .csv\n» '))
    return opcion


#En esta parte registraremos las ventas, ademas de los datos del cliente o usuario
def RegistrarVenta():
    ListaVentas=[] # Limpieza de la lista
    print('\n--------- Registro de venta ---------')
    while True:
        folio = int(input(f'Introduzca folio de venta de el equipo(s)\n» '))
        if folio in DiccionarioVentas.keys():
            print('Error, ya existe una venta con ese folio de venta')
        else:
            break
    while True:
        Nombre_Cliente = input('Introduzca Nombre del Cliente\n» ')
        fechaVenta = input('Introduzca Fecha de Venta\n» ')
        descripcion = input('Introduzca descripción del tipo de el Equipo \n» ')
        cantidadVenta = int(input('Introduzca cantidad a vender del tipo de el Equipo mencionado\n» '))
        precioVenta = int(input('Introduzca precio (sin iva) del tipo de Equipo (por unidad)\n» $'))
        print(separador)
        subtotal = (cantidadVenta * precioVenta)
        print(f'Subtotal (sin iva) de los Equipo (s) tipo {descripcion}:','${:.2f}'.format(subtotal))
        print(separador)
        fechaVenta = datetime.strptime(fechaVenta, "%d/%m/%Y").date()
        organizacionVenta = Venta(descripcion,cantidadVenta, precioVenta, fechaVenta)
        ListaVentas.append(organizacionVenta)
        DiccionarioVentas[folio] = ListaVentas
        Agrega_Otra_Compu_a_la_Misma_Venta = int(input('¿Desea agregar otra(s) venta(s) de Equipo(s) a la misma venta?\n[1] Si \n[2] No\n» '))
        if  Agrega_Otra_Compu_a_la_Misma_Venta== 2:
            dimensionVentas, acumuladoVentas = 0 , 0
            while dimensionVentas < len(DiccionarioVentas[folio]):
                aculumador = (int(DiccionarioVentas[folio][dimensionVentas].precioVenta) * int(DiccionarioVentas[folio][dimensionVentas].cantidadVenta))
                acumuladoVentas =  aculumador + acumuladoVentas
                dimensionVentas += 1
            print(separador)
            print('Subtotal: ${:.2f}'.format(acumuladoVentas),'\nIVA:','${:.2f}'.format(acumuladoVentas * .16))
            print('-' * 16,'\n\nTotal: ${:.2f}'.format(acumuladoVentas*1.16, 2),f'\nVenta realizada el: {fechaVenta}\n')
            print(separador)
            break

#esta parte es para la opcion de consultar la venta registras por el usuario
def ConsultarVenta():
    consulta = int(input('Folio a consultar: '))
    dimension, totalVentas = 0 , 0
    if consulta in DiccionarioVentas.keys():
        while dimension < len(DiccionarioVentas[consulta]):
            print(separador)
            print(f'Descripción del tipo de Equipo o Producto: {DiccionarioVentas[consulta][dimension].descripcion}')
            print(f'Cantidad de Equipo: {DiccionarioVentas[consulta][dimension].cantidadVenta}')
            print('Precio: ${:.2f}'.format(DiccionarioVentas[consulta][dimension].precioVenta, 2))
            print(f'Fecha: {DiccionarioVentas[consulta][dimension].fechaVenta}')
            totalVentas = (int(DiccionarioVentas[consulta][dimension].precioVenta) * int(DiccionarioVentas[consulta][dimension].cantidadVenta)) + totalVentas
            dimension += 1
        print(separador)
        print('Subtotal: ${:.2f}'.format(totalVentas),'\nIVA:','${:.2f}'.format(totalVentas * .16))
        print('-' * 16,'\n\nTotal: ${:.2f}\n'.format(totalVentas + totalVentas * .16, 2))
        print(separador)
    else:
        print('La clave no esta registrada')

#Aqui tenemos la parte para la consulta de la venta por una fecha en especifica
def VentaFecha():
    print("\nIngrese una fecha para buscar todas las ventas de esta")
    print(f'¡Porfavir digite la fecha en el siguiente formato! (Dia/Mes/Año)')
    print(f'Ejemplo: 23/07/2020')
    
    print("+++++++++++++++++++++++++++++++++++++++++++++")
    for venta, datos in DiccionarioVentas.items():
        print(f'{datos[0]}')

    fec = input("Fecha: ")

    fecFormat = checarFecha(fec)
    print(fecFormat)
    SavePoint = 0
    dataVentas = len(DiccionarioVentas)
    print(f'\n{"*"*50}')
    print(f'Folio,Fecha,Descripción,Cantidad,Total')
    for venta, datos in DiccionarioVentas.items():
        if str(datos[0][3]) == str(fecFormat):
            print(f'{venta}, {datos[0][3]}, {datos[0][0]}, {datos[0][1]}, {datos[0][2]}')
        else:
            SavePoint +=1
            if SavePoint == dataVentas:
                print(f'{"*"*50}')  
                print(f'\nNINGUNA VENTA ENCONTRADA CON ESA FECHA\n')
                print(f'FAVOR DE VERIFICAR QUE: {fecFormat} ESTE CORRECTO')

#Aqui se registrara el reporte de las ventas hechas por el usuario
def ReporteVentas():
    fechaBusqueda = input("Ingrese la fecha para encontrar las ventas de ese día (ej: dd/mm/yyyy)\n» ")
    encontroAlMenosUnDato = False
    Subtotal = 0
    GranTotalVenta = 0
    GranTotalVentasDiaSinIva = 0
    GranTotalVentasDiaConIva = 0

    for key, value in DiccionarioVentas.items() :
        diferentesLlantasDentroMismaVenta = len(value)
        contador = 0
        while contador < diferentesLlantasDentroMismaVenta:
            fechaExtraida = value[contador].fechaVenta # Se evitó el [:-15] en "fechaVenta"

            if fechaBusqueda == fechaExtraida:

                if encontroAlMenosUnDato == False:
                    print("\nSe ha encontrado ventas del día",fechaBusqueda)
                    print("      Folio    |   Descripcion   |  Cantidad  |  Precio c/u  |    Fecha   |  Subtotal    |   IVA      |  Total")
                    encontroAlMenosUnDato = True # Temporal

            if fechaBusqueda == fechaExtraida:
                Subtotal = value[contador].precioVenta*value[contador].cantidadVenta
                IVA = (value[contador].precioVenta*value[contador].cantidadVenta)*.16
                GranTotalVenta = IVA + (value[contador].precioVenta*value[contador].cantidadVenta)
                print(f'\t{key:<6} | {value[contador].descripcion:^15} | {value[contador].cantidadVenta:^10} |   ${value[contador].precioVenta:<9} | {value[contador].fechaVenta[-10:]:<8} |   ${Subtotal:<9} |   ${IVA:<7} |  ${GranTotalVenta:<10}')
                GranTotalVentasDiaSinIva = GranTotalVentasDiaSinIva + (value[contador].precioVenta*value[contador].cantidadVenta)
                GranTotalVentasDiaConIva = GranTotalVentasDiaConIva + GranTotalVenta
            contador+= 1

    if encontroAlMenosUnDato == True:
        print("\nEl día", fechaBusqueda, " se vendió en total:",'${:.2f}'.format(GranTotalVentasDiaSinIva),"con iva:",'${:.2f}'.format(GranTotalVentasDiaConIva))    
    print("")

    if encontroAlMenosUnDato == False:
        print("Error, no se encuentra datos de esa fecha")

#Aqui se guardaran los registro de las ventas  
def GuardarCSV():
    print("Guardando archivo .csv")
    with open('Ventas_Registradas.csv', 'w') as f:
            for key in DiccionarioVentas.keys():
                f.write("%s,%s\n"%(key,DiccionarioVentas[key]))
    print("Se ha guardado archivo .csv en el mismo directorio")
    
def MostrarVentas():
    print(DiccionarioVentas)
    print("Todas las ventas")

#Aqui tenemos el menu de opciones a seleccionar que utilizara el usuario 

while True:
    opcionElegida = Menu()
    if opcionElegida == 1:
        RegistrarVenta()
    if opcionElegida == 2:
        ConsultarVenta()
    if opcionElegida == 3:
        ReporteVentas()
    if opcionElegida == 4:
        MostrarVentas()
    if opcionElegida == 5:
        GuardarCSV()
        break
