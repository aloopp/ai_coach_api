# 1. Usar una versión de Python oficial y ligera
FROM python:3.10-slim

# 2. Establecer la carpeta de trabajo dentro del contenedor
WORKDIR /app

# 3. Copiar la lista de librerías e instalarlas
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copiar todo el código de tu proyecto al contenedor
COPY . .

# 5. Exponer el puerto por donde se comunicará la API
EXPOSE 8000

# 6. El comando que encenderá el servidor cuando arranque el contenedor
CMD ["uvicorn", "api_gemini:app", "--host", "0.0.0.0", "--port", "8000"]