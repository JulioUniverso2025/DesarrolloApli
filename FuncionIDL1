import pandas as pd
df1=pd.read_csv("Creacion datos IDL1.csv")


#Primero las funciones
#Ingresar el codigo del empleado (ID del empleado) "valor"
def obtener_jefe(df1,valor):
    # Verificar si el ID_EMPLEADO existe en el DataFrame
    if valor not in df1["ID EMPLEADO"].values:
        return f"El empleado con ID {valor} no existe en la base de datos."

 # Obtener el NOMBRE del trabajador
    resultado1= df1[df1["ID EMPLEADO"] == valor]
    resultado1
    print("Nombre del trabajador:",resultado1.iloc[0,3])

   
    #Obtener su Puesto de Trabajo
    Puesto=resultado1.iloc[0,2]
    print("Puesto del trabajador:",Puesto)

     # Obtener el NOMBRE del jefe inmediato
    resultado1= df1[df1["ID EMPLEADO"] == valor]
    resultado1
    print("Jefe inmediato:",resultado1.iloc[0,4])
