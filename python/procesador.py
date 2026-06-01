import os
import json
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def procesar_y_dividir():
    docs_folder = "docs"
    contenido_total = []

    # 1. Leer archivos
    for archivo in os.listdir(docs_folder):
        ruta = os.path.join(docs_folder, archivo)
        if archivo.endswith(".pdf"):
            loader = PyPDFLoader(ruta)
            contenido_total.extend(loader.load())
        elif archivo.endswith(".txt") or archivo.endswith(".md"):
            loader = TextLoader(ruta, encoding='utf-8')
            contenido_total.extend(loader.load())
        elif archivo.endswith(".json"):
            with open(ruta, 'r', encoding='utf-8') as f:
                data = json.load(f)
                # Convertimos el JSON a texto simple para procesarlo
                contenido_total.append(type('Doc', (object,), {'page_content': str(data), 'metadata': {'source': archivo}})())

    # 2. Dividir en fragmentos (Chunking)
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    fragmentos = splitter.split_documents(contenido_total)
    
    return fragmentos

# Ejecutamos
print("Procesando y dividiendo...")
fragmentos = procesar_y_dividir()
print(f"Éxito: Se crearon {len(fragmentos)} fragmentos de texto listos para la IA.")