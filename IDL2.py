import streamlit as st
st.title("Confiteria Dulcino")
st.title("Formulario")

#Validar nombre de producto
def validar_nombre_producto(nombre):
    if len(nombre) < 20:
        return True
    else:
        return False


# Solicitar el nombre del producto
nombre = st.text_input("Ingrese el nombre del producto: ")
if validar_nombre_producto(nombre):
    print("Nombre válido")
else:
    print("El nombre del producto es demasiado largo")





