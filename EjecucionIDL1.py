import streamlit as st

st.title("Ingrese el codigo o ID del trabajador:")
#Entrada de usuario
valor=st.number_input()

#Ahora la ejecucion
from FuncionesIDL1 import obtener_jefe
obtener_jefe(df1,valor)
