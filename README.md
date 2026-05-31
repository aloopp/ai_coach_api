# ai_coach_api
API RESTful developed with Python (FastAPI) that integrates AI model (Gemini LLM) with Prompt Engineering to generate technical progressions in sports.

# 🏋️‍♂️ GenAI Coach API - RESTful Backend

A RESTful API developed with **Python** and **FastAPI** that integrates Google's Gemini foundational model(3.5 flash) to generate highly technical physical training progressions. 

This project demonstrates the implementation of modern backend architectures, Large Language Model (LLM) integration via APIs, and the application of Prompt Engineering techniques to structure complex responses into JSON format.

## 🚀 Tech Stack
* **Backend Framework:** FastAPI (Python)
* **LLM Integration:** Google Generative AI (Gemini 1.5)
* **Data Validation:** Pydantic
* **Web Server:** Uvicorn

## 🎯 Key Features
* **Foundational Model Integration:** Connection to the Gemini API for natural language processing.
* **Structured Prompt Engineering:** Design of hidden system prompts to force the LLM to return segmented, technical routines (Conditioning, Strength, Transition, Consolidation).
* **REST Endpoints:** Scalable architecture ready to be consumed by frontend applications or mobile clients.

## ⚙️ Local Installation & Setup

1. Clone this repository:
   ```bash
    git clone https://github.com/aloopp/ai_coach_api.git

2. Install the required dependencies:
 pip install fastapi uvicorn google-generativeai pydantic

3. Set up your Google AI Studio API Key in the main Python file.

4. Run the local server:
   ```bash
   uvicorn api_gemini:app --reload


📡 Usage Example (POST Endpoint)
Note: The API expects and returns data in Spanish.

# Request (JSON):
{
  "movimiento": "Dragon Squat",
  "nivel_actual": "Hago Pistol Squats explosivas pero pierdo el equilibrio al bajar la rodilla trasera",
  "dias_por_semana": 3
}

# Server Response (JSON):

{
  "objetivo": "Dragon Squat",
  "entrenamiento_recomendado": "- Fase 1: [Acondicionamiento y regresiones básicas]\n*Enfoque:* Mejorar la movilidad de la articulación subtalar (tobillo) y la rotación externa/abducción de la cadera estabilizadora para evitar el valgo dinámico de rodilla al cruzar la pierna libre.\n\n*   **Frecuencia:** 3 días a la semana (Lunes, Miércoles, Viernes).\n*   **Rutina de preparación articular (Antes de cada sesión):**\n    *   Dorsiflexión de tobillo con banda elástica (distracción articular): 2 series de 12 repeticiones por lado.\n    *   Rotación externa de cadera activa (posición de 90/90 dinámico): 2 series de 10 repeticiones por lado.\n*   **Bloque Principal de Fuerza (Fase 1):**\n    1.  **Curtsy Squat con déficit (sobre cajón de 10-15 cm):** 3 series x 8 repeticiones por pierna. *Biomecánica:* Permite al fémur de la pierna de apoyo rotar externamente bajo carga, aumentando el rango de movimiento (ROM) en el plano coronal de manera segura.\n    2.  **Dragon Squat asistido con TRX / Anillas:** 4 series x 6 repeticiones por pierna (Tempo 3-1-1-0: 3 segundos de bajada, 1 segundo de pausa abajo, 1 segundo de subida). *Biomecánica:* El agarre superior desplaza el centro de masas hacia atrás, compensando la falta de dorsiflexión y permitiendo mecanizar el recorrido de la rodilla trasera.\n    3.  **Copas de rotación de cadera en bipedestación:** 3 series x 10 repeticiones por lado.\n\n- Fase 2: [Desarrollo de fuerza específica]\n*Enfoque:* Desarrollar el control excéntrico y la fuerza estabilizadora del glúteo medio y el sóleo en el punto crítico de transición (el momento de máxima flexión antes de perder el equilibrio).\n\n*   **Frecuencia:** 3 días a la semana.\n*   **Bloque Principal de Fuerza (Fase 2):**\n    1.  **Dragon Squat excéntrico con parada en el \"punto de fallo\":** 4 series x 4 repeticiones por pierna. *Ejecución:* Baja en 5 segundos de manera controlada. Al llegar al punto donde sueles perder el equilibrio (rodilla trasera casi al suelo), sostén una isometría activa de 3 segundos sin tocar el piso, luego apoya el pie trasero para subir con ambas piernas.\n    2.  **Airborne Squat profundo:** 3 series x 6 repeticiones por pierna. *Biomecánica:* Al mantener el pie trasero elevado sin cruzarlo tanto, se aísla la fuerza unilateral pura del cuádriceps y glúteo de la pierna de apoyo, puente de fuerza ideal hacia el Dragon.\n    3.  **Puentes glúteos unipodales con abducción de cadera:** 3 series x 12 repeticiones por pierna (usando banda elástica alrededor de las rodillas).\n\n- Fase 3: [Transición al movimiento real]\n*Enfoque:* Integración de la estabilidad central (anti-rotación del core) y uso de contrabalance para dominar la trayectoria de la pierna trasera sin perder la línea de gravedad.\n\n*   **Frecuencia:** 3 días a la semana.\n*   **Bloque Principal de Fuerza (Fase 3):**\n    1.  **Counterbalance Dragon Squat (con disco/mancuerna de 2 a 5 kg):** 4 series x 5 repeticiones por pierna. *Biomecánica:* Sostener el peso con los brazos estirados al frente actúa como un contrapeso físico que desplaza el centro de gravedad hacia delante. Esto permite bajar la rodilla trasera sin que el cuerpo colapse hacia atrás, facilitando la alineación perfecta de la pelvis.\n    2.  **Dragon Squats con objetivo propioceptivo:** 3 series x 6 repeticiones por pierna. *Ejecución:* Coloca un disco pequeño de halterofilia o un bloque de yoga detrás de ti. Debes bajar de forma controlada hasta rozar (sin apoyar peso) dicho objeto con la rodilla trasera, y luego subir explosivo. Reduce la altura del bloque progresivamente.\n    3.  **Pistol Squat con pausa isométrica en el fondo (Bottom-up transition):** 3 series x 4 repeticiones.\n\n- Fase 4: [Consolidación]\n*Enfoque:* Transferencia de la fuerza explosiva de la Pistol Squat al Dragon Squat libre, eliminando la asistencia y dominando la transición excéntrica-concéntrica en el rango final de movimiento.\n\n*   **Frecuencia:** 3 días a la semana.\n*   **Bloque Principal de Fuerza (Fase 4):**\n    1.  **Dragon Squat completo (sin asistencia):** 4 series x 3 a 5 repeticiones por pierna. *Técnica:* Descenso controlado, la rodilla de la pierna libre cruza por detrás de la de apoyo buscando el exterior del talón contrario sin tocar el suelo. Subida sólida empujando desde el talón activo.\n    2.  **Combo de transferencia dinámico (Pistol a Dragon):** 3 series x 3 combos por lado (1 Combo = 1 Pistol Squat Explosiva + 1 Dragon Squat Estricta sin descanso intermedio). *Biomecánica:* El sistema neuromuscular aprovecha la fuerza y estabilidad del patrón sagital (Pistol) para estabilizar inmediatamente el patrón rotacional (Dragon).\n    3.  **Sostén isométrico final (Dragon Hold):** 3 series x 10 segundos en la posición más baja por pierna (fuerza de fin de rango)."
}
