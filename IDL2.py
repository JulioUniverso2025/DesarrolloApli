import streamlit as st
st.title("Confiteria Dulcino")
st.title("Formulario")

# Solicitar el nombre del producto
producto = st.text_input("Ingrese el nombre del producto: ")
if validar_nombre_producto(producto):
    print("Nombre válido.")
else:
    print("El nombre del producto es demasiado largo.")