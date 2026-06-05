import os

# La carpeta docs es nuestra única fuente de verdad.
# Al aislar los docs aquí, el sistema es modular y fácil de mantener.
carpeta = "docs"

# VALIDACIÓN Y SEGURIDAD: Comprobamos la existencia del directorio antes de operar.
# Esto evita errores en tiempo de ejecución (Runtime Errors).
if os.path.exists(carpeta):
    # INGESTA DINÁMICA: Listamos todos los archivos contenidos.
    # DEFENSA: Usar os.listdir permite que el sistema sea escalable; 
    # si agregamos un archivo nuevo, el código no necesita cambios.
    archivos = os.listdir(carpeta)
    print("¡Éxito! Encontré los siguientes archivos:")
    for archivo in archivos:
        print("- " + archivo)
else:
    # GESTIÓN DE ERRORES: Mensaje claro para el usuario/administrador.
    print("No encontré la carpeta 'docs'. Asegúrate de que esté creada dentro de la carpeta principal.")