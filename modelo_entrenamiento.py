import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Cargar datos
df = pd.read_excel("datos_leche.xlsx")

# Definir variables
X = df[['col1e3', 'col1e4']]  # Las características
y = df['label']  # El nivel de riesgo (bajo, medio, alto)

# Dividir en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar el modelo
modelo = RandomForestClassifier()
modelo.fit(X_train, y_train)

# Guardar el modelo entrenado
with open("modelo_leche.pkl", "wb") as f:
    pickle.dump(modelo, f)