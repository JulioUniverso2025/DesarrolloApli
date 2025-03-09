import streamlit as st
st.title("Confiteria Dulcino")
st.title("Formulario")

# Solicitar el nombre del producto
nombre=st.text_input("Ingrese el nombre del producto: ")

#Validar nombre de producto
if len(nombre) < 20:
    print("Nombre valido")
else:
    print("El nombre del producto es demasiado largo")

#Ingrese el precio del producto
precio=st.text_input("Precio del producto:")




