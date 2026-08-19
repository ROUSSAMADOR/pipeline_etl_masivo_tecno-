import sqlite3
import pandas as pd 
conexion=sqlite3.connect("almacen_central.db")
datos_sucios=pd.read_csv("ventas_masivas_sucias.csv")
reporte_venta_limpio=datos_sucios.dropna().drop_duplicates()
reporte_venta_limpio.to_sql("inventario_limpio",conexion,if_exists="replace",index=False)
sql_query="SELECT * FROM inventario_limpio WHERE precio_venta >=2000 ORDER BY precio_venta DESC;"
tabla_solicitada=pd.read_sql_query(sql_query,conexion)
tabla_solicitada.to_csv("reporte_alta_gerencia.csv", index=False)