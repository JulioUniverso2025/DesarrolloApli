import streamlit as st
st.title("Confiteria Dulcino")
st.title("Formulario")

# Solicitar el nombre del producto
nombre=st.text_input("Ingrese el nombre del producto: ")

#Validar nombre de producto
if nombre:
   if len(nombre) < 20:
       st.success (f"El Nombre es valido")
   else:
      st.error("El nombre del producto no debe ser mayor a 20 caracteres")

#Ingrese el precio del producto
precio=st.number_input("Precio del producto:")
if precio: 
    if 0 <= float(precio)<= 99:
        st.success(f"El precio ingresado es válido: S/.{precio}")
    else:
        st.error("Error: El precio debe estar entre 0 y 999")
              
    


