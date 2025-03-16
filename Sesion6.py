import streamlist as st
from supabase import create_client, client
import os
#Configurar supabase
SUPABASE_URL = "https://wezkgzoocxwvitbraadb.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Indlemtnem9vY3h3dml0YnJhYWRiIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDIxNjE1NjcsImV4cCI6MjA1NzczNzU2N30.dDmHmNGfTckeEn3zM22rBjAOTyhSujtWrmpm2tgchbg"

supabase: Client=create_client(SUPABASE_URL,SUPABASE_KEY)

st.title("Gestion de Clientes - CRYD con Supabase y Streamlit")
#Formulario para agregar cliente
st.header("Agregar Cliente")
nombre=st.text_input("Nombre:")
email=st.text_input("Email:")
telefono=st.text_input("Telefono:")

if st.button("Agregar Cliente"):
     if nombre and email: 
        data={"nombre":nombre, "email":email, "telefono":telefono}
        response=supabase.table("clientes").insert(data).execute()
        st.success("Cliente agregado correctamente")
    else:
        st.wawrning("Nombre y Email son obligatorios")
