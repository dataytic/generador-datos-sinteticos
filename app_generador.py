import pandas as pd
from faker import Faker
import random
import streamlit as st

# Configurar Faker
fake = Faker('es_CO')

# Campos disponibles con funciones
campos = {
    'Nombre Completo': lambda: fake.name(),
    'Correo': lambda: f"{fake.first_name().lower()}.{fake.last_name().lower()}@{random.choice(['gmail.com','hotmail.com','outlook.com'])}",
    'Ciudad': lambda: fake.city(),
    'Teléfono': lambda: fake.phone_number(),
    'Fecha de nacimiento': lambda: fake.date_of_birth().isoformat(),
    'Inclinación sexual': lambda: random.choice(['Heterosexual', 'Homosexual', 'Bisexual', 'Asexual']),
    'Inclinación política': lambda: random.choice(['Izquierda', 'Derecha', 'Centro', 'Independiente']),
    'Estado civil': lambda: random.choice(['Soltero', 'Casado', 'Unión libre']),
    'Religión': lambda: random.choice(['Católico', 'Cristiano', 'Ateo', 'Judío']),
    'Profesión': lambda: random.choice(['Abogado', 'Ingeniero', 'Docente', 'Médico'])
}

# Interfaz
st.title("🧠 Generador de Datos Sintéticos Colombianos")

cantidad = st.slider("Cantidad de registros:", 10, 1000, 100)
seleccionados = st.multiselect("Campos que deseas incluir:", list(campos.keys()), default=list(campos.keys()))

if st.button("Generar datos"):
    data = []
    for _ in range(cantidad):
        fila = {campo: campos[campo]() for campo in seleccionados}
        data.append(fila)
    
    df = pd.DataFrame(data)
    st.success("✅ Datos generados correctamente")
    st.dataframe(df)
    st.download_button("📥 Descargar CSV", df.to_csv(index=False), file_name="datos_sinteticos.csv", mime="text/csv")
