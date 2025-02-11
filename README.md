# Clasificador de Dígitos MNIST con Streamlit

Este proyecto implementa una red neuronal para clasificar dígitos escritos a mano utilizando el dataset MNIST. Se ha desarrollado una aplicación en **Streamlit** para permitir la carga de imágenes y obtener predicciones en tiempo real.

## 🚀 Características
- Modelo de red neuronal entrenado con TensorFlow/Keras.
- Interfaz gráfica en Streamlit para cargar imágenes y obtener predicciones.
- Despliegue en **Streamlit Cloud**.

---

## 📦 Instalación
### 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/joseaholgado/redes_neuronales_numeros_mnist.git
cd TU_REPOSITORIO
```

### 2️⃣ Instalar dependencias
Ejecuta el siguiente comando para instalar los paquetes necesarios:
```bash
pip install -r requirements.txt
```

### 3️⃣ Ejecutar la aplicación localmente
```bash
streamlit run app.py
```
Esto abrirá la aplicación en tu navegador.

---

## 📥 Descargar el modelo entrenado
Si no tienes el modelo `modelo_mnist.h5`, puedes descargarlo desde Google Colab o desde el repositorio:
```bash
wget https://github.com/joseaholgado/redes_neuronales_numeros_mnist/blob/main/modelo_mnist.h5
```

---

## 🚀 Despliegue en Streamlit Cloud
### 1️⃣ Subir el código a un repositorio de GitHub
Asegúrate de que los archivos **`app.py`**, **`modelo_mnist.h5`** y **`requirements.txt`** están en tu repositorio.

### 2️⃣ Crear un archivo `requirements.txt`
```txt
streamlit
tensorflow
numpy
p
pillow
```

### 3️⃣ Subir a Streamlit Cloud
1. Ir a [Streamlit Cloud](https://share.streamlit.io/)
2. Conectar con GitHub y seleccionar el repositorio
3. Configurar `app.py` como el archivo principal
4. ¡Listo! La aplicación estará disponible en la nube.

---

## 📌 Uso de la Aplicación
1️⃣ **Sube una imagen de un número manuscrito** (28x28 en escala de grises).
2️⃣ **La red neuronal analizará la imagen y mostrará la predicción**.
3️⃣ **Revisar la probabilidad de cada número (0-9)**.

---

## 🛠 Tecnologías Usadas
- **Python**
- **TensorFlow/Keras**
- **Streamlit**
- **NumPy**
- **Pillow** (Para manejo de imágenes)

---

## 📄 Licencia
Este proyecto está bajo la licencia MIT. Puedes usarlo y modificarlo libremente.

📌 **Autor:** [Jose Antonio Holgado Bonet](https://github.com/joseaholgado)

📢 **¡Contribuciones y mejoras son bienvenidas!** 🚀

