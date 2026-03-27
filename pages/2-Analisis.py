import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

st.title("📊 Análisis de Datos")

# --- CARGA DE DATOS SEGURA ---
@st.cache_data
def load_data():
    try:
        return pd.read_csv("data/datos.csv")
    except FileNotFoundError:
        return None

df = load_data()

if df is not None:
    st.header("Valores del DataSet")
    st.dataframe(df)

    # Crear pestañas (Se asegura que cada variable corresponda a su índice)
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "Detalles",
        "Información",
        "Valores nulos",
        "Valores duplicados",
        "Estadísticas"
    ])

    # 📌 TAB 1: DETALLES
    with tab1:
        st.subheader("📝 Detalles del Proyecto")
        st.markdown("""
        El DataSet contiene información sobre los estudiantes de una universidad.
        Incluye las siguientes columnas:
        - **Nombre**: El nombre del estudiante.
        - **Edad**: La edad del estudiante.
        - **Sexo**: El género del estudiante.
        - **Calificación**: La calificación en una asignatura.
        """)

    # 📌 TAB 2: INFORMACIÓN
    with tab2:
        st.subheader("📂 Vista del DataSet")
        col1, col2 = st.columns(2)
        with col1:
            st.write("**Primeros registros**")
            st.dataframe(df.head())
        with col2:
            st.write("**Últimos registros**")
            st.dataframe(df.tail())

        st.write("**Tipos de datos por columna:**")
        st.write(df.dtypes.astype(str)) # Convertido a string para mejor visualización

    # 📌 TAB 3: VALORES NULOS
    with tab3:
        st.subheader("🔍 Análisis de Vacíos")
        nulos = df.isnull().sum()
        st.write("Conteo de valores nulos por columna:")
        st.table(nulos) # Usar table para una vista más limpia

    # 📌 TAB 4: DUPLICADOS
    with tab4:
        st.subheader("👥 Registros Duplicados")
        total_duplicados = df.duplicated().sum()
        st.metric("Total de duplicados", total_duplicados)
        
        if total_duplicados > 0:
            st.write("Filas repetidas encontradas:")
            st.dataframe(df[df.duplicated()])
        else:
            st.success("No se encontraron registros duplicados. ✅")

    # 📌 TAB 5: ESTADÍSTICAS
    with tab5:
        st.subheader("📈 Resumen Estadístico")
        st.dataframe(df.describe())

else:
    st.error("❌ No se encontró el archivo 'data/datos.csv'.")
    st.info("Verifica que la ruta sea correcta para poder visualizar el análisis.")

st.markdown("---")
st.markdown("© Luz Eliana Martínez")