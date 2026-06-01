import os
import json
# Importamos herramientas para comparar texto
from difflib import SequenceMatcher

# (Simulamos que cargamos los fragmentos de nuevo para este ejemplo)
# En un sistema real esto se guardaría en una base de datos vectorial
fragmentos = [
    "La base de datos puede fallar por credenciales incorrectas.",
    "Para reiniciar el servicio, usa el comando sudo systemctl restart.",
    "El error 502 significa problemas de conexión con el servidor.",
    "No se guardan cambios si la sesión expiró.",
    # ... aquí estarían tus 19 fragmentos reales
]

def buscar_contexto(pregunta):
    mejor_fragmento = ""
    mayor_similitud = 0

    for frag in fragmentos:
        # Comparamos la pregunta con cada fragmento
        similitud = SequenceMatcher(None, pregunta.lower(), frag.lower()).ratio()
        if similitud > mayor_similitud:
            mayor_similitud = similitud
            mejor_fragmento = frag
    
    return mejor_fragmento if mayor_similitud > 0.1 else "Lo siento, no encontré información sobre eso."

# Prueba rápida
pregunta_usuario = "No puedo acceder, ¿qué pasa con mi sesión?"
resultado = buscar_contexto(pregunta_usuario)
print(f"Pregunta: {pregunta_usuario}")
print(f"Respuesta encontrada: {resultado}")