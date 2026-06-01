import os

# Buscamos la carpeta docs
carpeta = "docs"

# Verificamos si existe la carpeta
if os.path.exists(carpeta):
    archivos = os.listdir(carpeta)
    print("¡Éxito! Encontré los siguientes archivos:")
    for archivo in archivos:
        print("- " + archivo)
else:
    print("No encontré la carpeta 'docs'. Asegúrate de que esté creada dentro de la carpeta principal.")