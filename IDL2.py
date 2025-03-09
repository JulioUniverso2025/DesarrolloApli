import streamlit as st
st.title("Confiteria Dulcino")
st.title("Formulario")

# Solicitar el nombre del producto
nombre=st.text_input("Ingrese el nombre del producto: ")
#Ingrese el precio del producto
precio=st.text_input("Precio del producto:")

#Validar nombre de producto
def validar_nombre_producto(nombre):
    if len(nombre) < 20:
        return True
    else:
        return False
if validar_nombre_producto(nombre):
    print("Nombre válido")
else:
    print("El nombre del producto es demasiado largo")






