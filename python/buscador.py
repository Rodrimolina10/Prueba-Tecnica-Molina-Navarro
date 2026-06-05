import os
import json
# SequenceMatcher mide qué tan parecidas son dos cadenas de texto.
from difflib import SequenceMatcher

# En este prototipo simulo los fragmentos. 
# En producción, esto se escala a una base de datos vectorial (ChromaDB/pgvector).
fragmentos = [
    "La base de datos puede fallar por credenciales incorrectas.",
    "Para reiniciar el servicio, usa el comando sudo systemctl restart.",
    "El error 502 significa problemas de conexión con el servidor.",
    "No se guardan cambios si la sesión expiró.",
]

def buscar_contexto(pregunta):
    mejor_fragmento = ""
    mayor_similitud = 0

    # Iteramos sobre cada fragmento para buscar la mejor coincidencia semántica/textual.
    for frag in fragmentos:
        # .lower() asegura que la comparación sea insensible a mayúsculas.
        # .ratio() devuelve un valor de 0 a 1 indicando el grado de similitud.
        similitud = SequenceMatcher(None, pregunta.lower(), frag.lower()).ratio()
        
        # Guardamos el fragmento con mayor puntuación.
        if similitud > mayor_similitud:
            mayor_similitud = similitud
            mejor_fragmento = frag
    
    # Solo devolvemos resultados si hay una similitud mínima (> 0.1).
    # Si la IA dice "no encontré info", es porque el buscador no pasó este umbral.
    return mejor_fragmento if mayor_similitud > 0.1 else "Lo siento, no encontré información sobre eso."

# Ejecución de prueba para validar el flujo del sistema.
pregunta_usuario = "No puedo acceder, ¿qué pasa con mi sesión?"
resultado = buscar_contexto(pregunta_usuario)
print(f"Pregunta: {pregunta_usuario}")
print(f"Respuesta encontrada: {resultado}")