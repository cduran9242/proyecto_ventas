from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
import mysql.connector
from app.config.db_config import get_db_connection

class ProductoController:

    def create_producto(self, producto):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            query = """
            INSERT INTO Productos (Codigo_prducto, Nombre_Producto, Descripcion, Categoria, Unidad_medida, estado, Fecha_creacion, Fecha_update)
            VALUES (%s, %s, %s, %s, %s, %s, NOW(), NOW())
            """
            values = (
                producto.Codigo_producto,
                producto.Nombre_Producto,
                producto.Descripcion,
                producto.Categoria,
                producto.Unidad_medida,
                producto.estado
            )

            cursor.execute(query, values)
            conn.commit()

            return {"mensaje": "Producto creado exitosamente"}

        except mysql.connector.Error as err:
            print(f"Error al crear producto: {err}")
            conn.rollback()
            raise HTTPException(status_code=500, detail="Error al crear producto")

        finally:
            conn.close()