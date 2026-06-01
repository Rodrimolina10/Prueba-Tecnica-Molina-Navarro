# Prueba Técnica - Molina Navarro Rodrigo Matías
Este repositorio contiene la solución completa para el desarrollo de un asistente automatizado de soporte técnico, capaz de responder consultas de manera contextual utilizando documentación interna del software "MineCatalog".

# Objetivo del proyecto
El sistema ha sido diseñado para automatizar la resolución de consultas repetitivas de soporte técnico, eliminando la carga operativa manual y garantizando respuestas precisas y basadas estrictamente en la documentación oficial.

# Estructura del repositorio
/docs: Documentación fuente técnica necesaria para el entrenamiento y consulta (formatos .pdf, .txt, .md, .json).  
/python: Núcleo de procesamiento de datos:  
-lector.py: Módulo dedicado a la ingesta y lectura de archivos, preparado para múltiples formatos.  
-procesador.py: Responsable de la normalización, limpieza de ruido, eliminación de caracteres especiales y segmentación (chunking) de contenidos largos.  
-buscador.py: Motor de indexación y búsqueda semántica para recuperar fragmentos relevantes.  
/workflows: Flujo de n8n exportado (My workflow.json) para su integración y ejecución en entornos locales.  

# Tecnologías Utilizadas
n8n: Orquestación integral de workflows y recepción de consultas mediante Webhook HTTP.  
Python: Procesamiento avanzado de lenguaje natural (NLP) para estructurar el conocimiento.  
OpenAI API: Generación de respuestas coherentes, aplicando un manejo estricto de prompts para mantener la fidelidad a la documentación. 

# Capacidades y Funcionalidades del Sistema
Procesamiento de Documentación: Proceso automatizado de limpieza, normalización y fragmentación de documentos, permitiendo manejar contenido desordenado y documentos extensos.  
Gestión Inteligente de Soporte: El sistema procesa preguntas frecuentes sobre autenticación, configuración de servicios, errores técnicos (como códigos 502, duplicidad de materiales, problemas de permisos) y solución de problemas operativos.  
Manejo de Errores y Calidad: Implementación de lógica robusta para gestionar:Consultas sin respuesta en la documentación (el sistema informa explícitamente la falta de información).  
Gestión de errores de API, timeouts y entradas vacías. 
Prevención de alucinaciones (la IA no inventa información externa).

# Instrucciones de Ejecución
Entorno: Preparar el entorno virtual y asegurar la instalación de las dependencias requeridas para la ejecución de los scripts de Python.
n8n: Iniciar la instancia local de n8n e importar el archivo /workflows/My workflow.json para cargar el flujo de trabajo configurado.  Procesamiento: Ejecutar los scripts de Python en la carpeta /python siguiendo el orden lógico (Lector -> Procesador -> Buscador) para generar el índice de documentación.  
Pruebas: Enviar consultas mediante POST al endpoint del Webhook.  
Ejemplo de consulta mediante PowerShell:
Invoke-RestMethod -Uri http://localhost:5678/webhook-test/soporte -Method Post -Body '{"pregunta":"¿Cómo reinicio el servicio de autenticación?"}' -ContentType "application/json"

# Contribución
Este proyecto fue desarrollado como parte de una evaluación técnica. Si deseas replicar esta solución, asegúrate de contar con una versión actualizada de n8n y acceso a las credenciales de OpenAI configuradas correctamente.

# Contacto
Autor: Molina Navarro, Rodrigo Matías

Propósito: Resolución de Prueba Técnica - Unilink
