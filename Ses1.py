import streamlit as st
st.title("Hola mundo por fin me salio la sesion1")

#Solicitar nombre del usuario
nombre=st.text_input("Por favor ingresa tu nombre:")

#Mostrar el saludo si el usuario ingresa su nombre
if nombre:
    st.write (f"Hola {nombre} Bienvenido a esta aplicacion")