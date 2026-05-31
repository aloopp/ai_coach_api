from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import google.generativeai as genai

# Configuración de la API de Gemini
GOOGLE_API_KEY = "API_KEY"
genai.configure(api_key=GOOGLE_API_KEY)

#Modelo gratis actual en 2026, cambiar si es necesario
model = genai.GenerativeModel('gemini-3.5-flash')

# Inicializar FastAPI
app = FastAPI(title="AI Coach API", description="API para generar progresiones físicas")

# Modelo de datos que espera recibir la API
class ObjetivoFisico(BaseModel):
    movimiento: str
    nivel_actual: str
    dias_por_semana: int

@app.post("/generar_progresion/")
async def generar_progresion(objetivo: ObjetivoFisico):
    prompt = f"""
    Eres un entrenador experto en biomecánica, calistenia y escalada. 
    Un atleta quiere lograr el siguiente movimiento/objetivo: {objetivo.movimiento}.
    Su nivel actual es: {objetivo.nivel_actual}.
    Puede entrenar {objetivo.dias_por_semana} días a la semana.
    
    Genera una progresión de 4 semanas muy técnica y estructurada. 
    Devuelve la respuesta estrictamente con el siguiente formato:
    - Fase 1: [Acondicionamiento y regresiones básicas]
    - Fase 2: [Desarrollo de fuerza específica]
    - Fase 3: [Transición al movimiento real]
    - Fase 4: [Consolidación]
    """
    
    try:
        response = model.generate_content(prompt)
        return {
            "objetivo": objetivo.movimiento,
            "entrenamiento_recomendado": response.text
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))