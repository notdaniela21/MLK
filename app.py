# app.py
import streamlit as st
import pickle
import numpy as np
import matplotlib.pyplot as plt

# Cargar el modelo previamente entrenado
with open('modelo_leche.pkl', 'rb') as f:
    modelo = pickle.load(f)

# Función que da análisis y sugerencias según el riesgo
def obtener_sugerencias(riesgo):
    if riesgo == "Bajo":
        return """
        ✅ **Análisis: Riesgo Bajo**  
        La muestra se encuentra dentro de los límites microbiológicos aceptables.  
        - No se detectan indicios de contaminación.  
        - Se recomienda mantener las buenas prácticas de higiene, refrigeración y transporte.  
        """
    elif riesgo == "Medio":
        return """
        ⚠️ **Análisis: Riesgo Medio**  
        Se detecta una carga microbiana moderada, lo que indica posibles fallos en el manejo.  
        - Revise las condiciones de almacenamiento y equipos de pasteurización.  
        - Aplique monitoreos más frecuentes en la cadena de frío.  
        - Podría ser necesaria una reinspección del lote.  
        """
    elif riesgo == "Alto":
        return """
        ❌ **Análisis: Riesgo Alto**  
        La muestra presenta una alta probabilidad de contaminación microbiana.  
        - Se recomienda inmovilizar el lote hasta su verificación en laboratorio.  
        - Aumente los controles de limpieza y sanitización de equipos.  
        - Evalúe la capacitación del personal en buenas prácticas de manufactura (BPM).  
        """
    else:
        return "Riesgo no determinado. Verifique los datos ingresados."

# Título de la aplicación
st.title("Clasificador de Riesgo Microbiológico en Leche")

# Entrada de datos para el usuario
col1e3 = st.number_input('Recuento 10³ (UFC/mL):', min_value=0)
col1e4 = st.number_input('Recuento 10⁴ (UFC/mL):', min_value=0)

# Predecir el nivel de riesgo y mostrar gráfica
if st.button('Clasificar Riesgo'):
    entrada = np.array([[col1e3, col1e4]])
    prediccion = modelo.predict(entrada)

    if prediccion == 0:
        riesgo = "Bajo"
    elif prediccion == 1:
        riesgo = "Medio"
    else:
        riesgo = "Alto"

    # Mostrar nivel de riesgo y sugerencias
    st.subheader(f"🔍 Nivel de Riesgo: {riesgo}")
    st.markdown(obtener_sugerencias(riesgo))

    # Crear gráfica
    fig, ax = plt.subplots()
    etiquetas = ['Coliformes 10³', 'Coliformes 10⁴']
    valores = [col1e3, col1e4]
    colores = ['green', 'orange'] if riesgo == "Medio" else ['green', 'green'] if riesgo == "Bajo" else ['red', 'red']
    ax.bar(etiquetas, valores, color=colores)
    ax.set_ylabel('Recuento UFC/mL')
    ax.set_title('Recuento Bacteriano por Muestra')
    st.pyplot(fig)
