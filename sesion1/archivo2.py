try:
    mi_ruta = 'C:\\Users\\user\\Documents\\Archivos\\'
    mi_archivo =  open(mi_ruta + "notas.txt",'w')
    texto = input("Dime algo: ")
    mi_archivo.write(texto)
    
    mi_archivo.close()
    
except Exception:
    print("ERROR")