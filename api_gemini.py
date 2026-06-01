from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from google import genai
import chromadb
import pandas as pd
import os
from dotenv import load_dotenv 

# Cargar el archivo .env de forma invisible
load_dotenv()

#Extraer la llave
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise ValueError("No se encontró la GOOGLE_API_KEY en el archivo .env")

# Configuración de la API de Gemini
cliente_gemini = genai.Client(api_key=GOOGLE_API_KEY)

# Inicializar FastAPI
app = FastAPI(title="Entrenador AI - API con arquitectura RAG")

# INICIALIZACIÓN DE LA BASE DE DATOS VECTORIAL
# PersistentClient guarda los vectores en una carpeta local para no recalcularlos cada vez
cliente_chroma = chromadb.PersistentClient(path="./bd_vectores")
coleccion = cliente_chroma.get_or_create_collection(name="manual_calistenia")

# CARGA DE DATOS (DATA LOADER)
# Esta función lee el CSV y lo mete a la base vectorial si está vacía

def cargar_dataset():
    if coleccion.count() == 0:
        print("Base de datos vacía. Iniciando lectura del CSV y vectorización...")
        df = pd.read_csv("dataset_ejercicios.csv")
        
        for index, fila in df.iterrows():
            texto_documento = f"Ejercicio: {fila['nombre']}. Enfoque: {fila['enfoque']}. Técnica: {fila['descripcion_tecnica']}"
            
            # --- CORRECCIÓN: Nueva sintaxis para crear embeddings ---
            respuesta_embed = cliente_gemini.models.embed_content(
                model="gemini-embedding-001",
                contents=texto_documento
            )
            vector = respuesta_embed.embeddings[0].values
            
            # Guarda en ChromaDB
            coleccion.add(
                embeddings=[vector],
                documents=[texto_documento],
                ids=[str(fila['id_ejercicio'])]
            )
        print("¡Datos vectorizados y guardados con éxito!")
    else:
        print(f"La base vectorial ya contiene {coleccion.count()} registros.")

# Ejecutamos la carga de datos al arrancar la API
cargar_dataset()

# MODELO DE ENTRADA
class ConsultaUsuario(BaseModel):
    pregunta: str

# ENDPOINT PRINCIPAL (El motor RAG) 
@app.post("/coach-inteligente")
async def obtener_rutina(consulta: ConsultaUsuario):
    try:
        # Vectorizar la pregunta con la nueva sintaxis
        respuesta_embed_pregunta = cliente_gemini.models.embed_content(
            model="gemini-embedding-001",
            contents=consulta.pregunta
        )
        vector_pregunta = respuesta_embed_pregunta.embeddings[0].values
        
        resultados = coleccion.query(
            query_embeddings=[vector_pregunta],
            n_results=1
        )
        
        contexto_extraido = resultados['documents'][0][0] if resultados['documents'] else "No hay información técnica disponible."
        
        # Prompt Engineering con contexto inyectado
        prompt_rag = f"""
        Eres un entrenador de élite de fuerza relativa. Responde a la pregunta del usuario basándote ESTRICTAMENTE en la siguiente información técnica de nuestra base de datos.
        
        <informacion_tecnica>
        {contexto_extraido}
        </informacion_tecnica>
        
        Pregunta del usuario: "{consulta.pregunta}"
        
        Instrucciones de formato: Responde de forma clara, directa y estructurada.
        """
        
        # Generación de la respuesta final
        respuesta = cliente_gemini.models.generate_content(
            model='gemini-3.5-flash',
            contents=prompt_rag
        )
        
        return {
            "pregunta_original": consulta.pregunta,
            "documento_encontrado_en_bd": contexto_extraido,
            "respuesta_ia": respuesta.text
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))