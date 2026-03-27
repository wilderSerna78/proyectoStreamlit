import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Configuración de la página (Opcional pero recomendado)
st.set_page_config(page_title="Visualizador de Gráficos", page_icon="📊")

st.title("📊 Gráficos Interactivos")

# --- CARGAR DATOS CON CONTROL DE ERRORES ---
@st.cache_data # Optimiza la carga para que no lea el CSV en cada clic
def cargar_datos():
    try:
        return pd.read_csv("data/datos.csv")
    except FileNotFoundError:
        return None

df = cargar_datos()

if df is not None:
    # Menú interactivo en la barra lateral
    opcion = st.sidebar.selectbox(
        "Selecciona el tipo de gráfico",
        ["Inicio", "Barras", "Líneas", "Pie"]
    )

    st.header("Gráficos de Datos")
    st.write("Visualiza la información de tu dataset de forma dinámica.")

    # Pantalla de Inicio / Información
    if opcion == "Inicio":
        st.markdown("""
        Los gráficos permiten representar datos visualmente:
        - **Barras**: Compara cantidades entre categorías.
        - **Líneas**: Ideal para ver tendencias o cambios.
        - **Pie**: Muestra proporciones de un total.
        - **Dispersión**: Relación entre dos variables numéricas.
        """)
        st.info("👈 Selecciona una opción en el menú lateral para ver los gráficos.")
        st.subheader("Vista previa de los datos")
        st.dataframe(df.head()) # Muestra las primeras filas para verificar

    # --- GRÁFICO DE BARRAS ---
    elif opcion == "Barras":
        st.subheader("Distribución por Curso")
        if "Curso" in df.columns:
            conteo = df["Curso"].value_counts()
            fig, ax = plt.subplots()
            ax.bar(conteo.index, conteo.values, color="skyblue")
            ax.set_xlabel("Curso")
            ax.set_ylabel("Cantidad")
            st.pyplot(fig)
        else:
            st.error("La columna 'Curso' no existe en el CSV.")

    # --- GRÁFICO DE LÍNEAS ---
    elif opcion == "Líneas":
        st.subheader("Tendencia de Edad")
        if "Edad" in df.columns:
            fig, ax = plt.subplots()
            ax.plot(df["Edad"], marker='o', linestyle='-', color='green')
            ax.set_ylabel("Edad")
            ax.set_xlabel("Índice de registro")
            st.pyplot(fig)
        else:
            st.error("La columna 'Edad' no existe en el CSV.")

    # --- GRÁFICO DE PIE ---
    elif opcion == "Pie":
        st.subheader("Proporción por Curso")
        if "Curso" in df.columns:
            conteo = df["Curso"].value_counts()
            fig, ax = plt.subplots()
            ax.pie(conteo.values, labels=conteo.index, autopct="%1.1f%%", startangle=90)
            st.pyplot(fig)
        else:
            st.error("La columna 'Curso' no existe en el CSV.")

else:
    st.error("❌ No se pudo encontrar el archivo 'data/datos.csv'.")
    st.info("Asegúrate de que la carpeta 'data' exista y contenga el archivo CSV.")

st.markdown("---")
st.markdown("© Luz Eliana Martínez")