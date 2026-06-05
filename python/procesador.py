import os
import json
# LangChain es el estándar para manipular documentos en proyectos de IA.
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def procesar_y_dividir():
    docs_folder = "docs"
    contenido_total = []

    # 1. INGESTA POLIMÓRFICA: Adaptamos el cargador según el tipo de archivo.
    for archivo in os.listdir(docs_folder):
        ruta = os.path.join(docs_folder, archivo)
        if archivo.endswith(".pdf"):
            loader = PyPDFLoader(ruta)
            contenido_total.extend(loader.load())
        elif archivo.endswith(".txt") or archivo.endswith(".md"):
            loader = TextLoader(ruta, encoding='utf-8')
            contenido_total.extend(loader.load())
        elif archivo.endswith(".json"):
            # Normalizamos el JSON a texto para que la IA lo procese de forma coherente.
            with open(ruta, 'r', encoding='utf-8') as f:
                data = json.load(f)
                contenido_total.append(type('Doc', (object,), {'page_content': str(data), 'metadata': {'source': archivo}})())

    # 2. CHUNKING (SEGMENTACIÓN): Dividimos textos largos en trozos manejables.
    # DEFENSA: chunk_size=500 optimiza la ventana de contexto de la IA.
    # chunk_overlap=50: asegura que el significado no se pierda al cortar entre fragmentos.
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    fragmentos = splitter.split_documents(contenido_total)
    
    return fragmentos

# Ejecutamos el flujo de preparación de datos
print("Procesando y dividiendo...")
fragmentos = procesar_y_dividir()
print(f"Éxito: Se crearon {len(fragmentos)} fragmentos de texto listos para la IA.")