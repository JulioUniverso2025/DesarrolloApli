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
    if 0 <= float(precio)<= 999:
        st.success(f"El precio ingresado es válido: S/.{precio}")
    else:
        st.error("Error: El precio debe estar entre 0 y 999")
              
#Categorias de productos
 # Definir un array de categorías predefinidas
categorias = ["Chocolates", "Caramelos", "Mashmelos", "Galletas", "Salados","Goma de Mascar"]

# Mostrar las categorías para que el usuario seleccione
categoria_seleccionada = st.selectbox("Selecciona una categoría", categorias)

# Radio button para definir si el producto está en venta o no
estado_venta = st.radio("¿El producto está en venta?", ("Sí", "No"))

#Validacion del producto
if len(nombre)< 20: and  0<= precio<= 999:
       st.success ("Felicidades se agrego el producto")
else:
    st.error("Lo sentimos no se puede crear este producto")
