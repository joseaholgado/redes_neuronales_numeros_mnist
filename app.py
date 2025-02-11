import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from PIL import Image, ImageOps

# 📌 Cargar el modelo entrenado
@st.cache_resource
def cargar_modelo():
    model = load_model("modelo_mnist.h5")  # Asegúrate de que el modelo esté en la misma carpeta
    return model

model = cargar_modelo()

# 📌 Configuración de la app
st.title("🖌️ Clasificador de Dígitos MNIST")
st.write("Sube una imagen con un número escrito a mano (28x28 en escala de grises) y el modelo intentará reconocerlo.")

# 📌 Cargar la imagen del usuario
uploaded_file = st.file_uploader("Sube una imagen en formato PNG o JPG", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # 📌 Procesar la imagen
    image = Image.open(uploaded_file).convert("L")  # Convertir a escala de grises
    image = image.resize((28, 28))  # Redimensionar a 28x28
    image_array = np.array(image).astype("float32") / 255.0  # Normalizar
    image_array = image_array.reshape(1, 784)  # Aplanar la imagen

    # 📌 Mostrar la imagen cargada
    st.image(image, caption="Imagen Cargada", width=150)

    # 📌 Hacer la predicción
    prediction = model.predict(image_array)
    predicted_class = np.argmax(prediction)

    # 📌 Mostrar el resultado
    st.subheader(f"🎯 Predicción del modelo: **{predicted_class}**")
    st.write(f"📊 Probabilidades por clase: {np.round(prediction, 2)}")
