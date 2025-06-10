try: 

    mi_ruta =  'C:\\Users\\user\\Documents\\Archivos\\'
    mi_archivo = open(mi_ruta + 'datos.txt', 'r')
    contenido =  mi_archivo.read()
    print(contenido)
    mi_archivo.close()

except FileNotFoundError:
    print("El archivo no se encuentra en la ruta especficada")
    