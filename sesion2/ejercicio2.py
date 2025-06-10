#Ejercicio 2: Contador de Líneas
#• Problema: Desarrolla un programa que pida al usuario el nombre de un archivo de texto. El
#programa deberá leer el archivo y mostrar en pantalla el número total de líneas que contiene.
#Debe manejar el error en caso de que el archivo no exista.
#Paso a paso:
#1. Solicitar al usuario el nombre del archivo (ej: poema.txt).
#2. Usar un bloque try...except para manejar la excepción FileNotFoundError.
#3. Dentro del try, abrir el archivo en modo lectura ('r').
#4. Utilizar el método readlines() para leer todas las líneas en una lista.
#5. Calcular la longitud de la lista (que es igual al número de líneas) y mostrarla.
#6. En el bloque except, si el archivo no se encuentra, imprimir un mensaje de error
#amigable.

try:
    mi_ruta = 'C:\\Users\\user\\Documents\\Archivos\\'
    nombre_archivo = input("Ingrese el nombre del archivo [El formato debe ser .txt]: ")
    archivo = open(mi_ruta + nombre_archivo,"r" )
    
    lineas = archivo.readlines()
    cantidad_lineas = len(lineas)
    
    print(f"El número de líneas del archivo {nombre_archivo} es de {cantidad_lineas}")
    
except FileNotFoundError:
    print("Archivo no encontrado")
    