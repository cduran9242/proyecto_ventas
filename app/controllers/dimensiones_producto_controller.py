# app/controllers/dimensiones_producto_controller.py
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
import mysql.connector
from app.config.db_config import get_db_connection

class DimensionesProductoController:

    def create_dimensiones_producto(self, dimensiones):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            # Verificar que el producto existe
            cursor.execute("SELECT IdProductos FROM Productos WHERE IdProductos = %s", (dimensiones.IdProducto,))
            if not cursor.fetchone():
                raise HTTPException(status_code=400, detail="El producto no existe")

            query = """
            INSERT INTO Dimensiones_producto (IdProducto, Ancho, Espesor, Diametro_Interno, Diametro_Externo, created_at, updated_at)
            VALUES (%s, %s, %s, %s, %s, NOW(), NOW())
            """
            values = (
                dimensiones.IdProducto,
                dimensiones.Ancho,
                dimensiones.Espesor,
                dimensiones.Diametro_Interno,
                dimensiones.Diametro_Externo
            )

            cursor.execute(query, values)
            conn.commit()

            return {"mensaje": "Dimensiones de producto creadas exitosamente"}

        except mysql.connector.Error as err:
            print(f"Error al crear dimensiones de producto: {err}")
            conn.rollback()
            raise HTTPException(status_code=500, detail="Error al crear dimensiones de producto")

        finally:
            conn.close()

    def get_dimensiones_producto(self, dimensiones_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Dimensiones_producto WHERE IdDimensiones = %s", (dimensiones_id,))
            result = cursor.fetchone()

            if not result:
                raise HTTPException(status_code=404, detail="Dimensiones de producto no encontradas")

            content = {
                "IdDimensiones": int(result[0]),
                "IdProducto": int(result[1]),
                "Ancho": float(result[2]) if result[2] else None,
                "Espesor": float(result[3]) if result[3] else None,
                "Diametro_Interno": float(result[4]) if result[4] else None,
                "Diametro_Externo": float(result[5]) if result[5] else None,
                "created_at": str(result[6]),
                "updated_at": str(result[7])
            }

            return jsonable_encoder(content)

        except mysql.connector.Error as err:
            print(f"Error al obtener dimensiones de producto: {err}")
            raise HTTPException(status_code=500, detail="Error al obtener dimensiones de producto")

        finally:
            conn.close()

    def get_dimensiones_by_producto(self, producto_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                SELECT dp.*, p.Nombre_Producto, p.Codigo_producto 
                FROM Dimensiones_producto dp 
                INNER JOIN Productos p ON dp.IdProducto = p.IdProductos 
                WHERE dp.IdProducto = %s
            """, (producto_id,))
            result = cursor.fetchall()

            if not result:
                raise HTTPException(status_code=404, detail="No se encontraron dimensiones para este producto")

            payload = [
                {
                    "IdDimensiones": data[0],
                    "IdProducto": data[1],
                    "Ancho": float(data[2]) if data[2] else None,
                    "Espesor": float(data[3]) if data[3] else None,
                    "Diametro_Interno": float(data[4]) if data[4] else None,
                    "Diametro_Externo": float(data[5]) if data[5] else None,
                    "created_at": str(data[6]),
                    "updated_at": str(data[7]),
                    "Nombre_Producto": data[8],
                    "Codigo_producto": data[9]
                } for data in result
            ]

            return {"resultado": jsonable_encoder(payload)}

        except mysql.connector.Error as err:
            print(f"Error al obtener dimensiones por producto: {err}")
            raise HTTPException(status_code=500, detail="Error al obtener dimensiones por producto")

        finally:
            conn.close()

    def get_all_dimensiones(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                SELECT dp.*, p.Nombre_Producto, p.Codigo_producto 
                FROM Dimensiones_producto dp 
                INNER JOIN Productos p ON dp.IdProducto = p.IdProductos
            """)
            result = cursor.fetchall()

            if not result:
                raise HTTPException(status_code=404, detail="No se encontraron dimensiones de productos")

            payload = [
                {
                    "IdDimensiones": data[0],
                    "IdProducto": data[1],
                    "Ancho": float(data[2]) if data[2] else None,
                    "Espesor": float(data[3]) if data[3] else None,
                    "Diametro_Interno": float(data[4]) if data[4] else None,
                    "Diametro_Externo": float(data[5]) if data[5] else None,
                    "created_at": str(data[6]),
                    "updated_at": str(data[7]),
                    "Nombre_Producto": data[8],
                    "Codigo_producto": data[9]
                } for data in result
            ]

            return {"resultado": jsonable_encoder(payload)}

        except mysql.connector.Error as err:
            print(f"Error al listar dimensiones de productos: {err}")
            raise HTTPException(status_code=500, detail="Error al listar dimensiones de productos")

        finally:
            conn.close()

    def update_dimensiones_producto(self, dimensiones_id: int, dimensiones):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT IdDimensiones FROM Dimensiones_producto WHERE IdDimensiones = %s", (dimensiones_id,))
            if not cursor.fetchone():
                raise HTTPException(status_code=404, detail="Dimensiones de producto no encontradas")

            query = """
            UPDATE Dimensiones_producto
            SET IdProducto = %s,
                Ancho = %s,
                Espesor = %s,
                Diametro_Interno = %s,
                Diametro_Externo = %s,
                updated_at = NOW()
            WHERE IdDimensiones = %s
            """
            values = (
                dimensiones.IdProducto,
                dimensiones.Ancho,
                dimensiones.Espesor,
                dimensiones.Diametro_Interno,
                dimensiones.Diametro_Externo,
                dimensiones_id
            )

            cursor.execute(query, values)
            conn.commit()

            return {"mensaje": f"Dimensiones de producto con ID {dimensiones_id} actualizadas correctamente"}

        except mysql.connector.Error as err:
            print(f"Error al actualizar dimensiones de producto: {err}")
            conn.rollback()
            raise HTTPException(status_code=500, detail="Error al actualizar dimensiones de producto")

        finally:
            conn.close()

    def delete_dimensiones_producto(self, dimensiones_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT IdDimensiones FROM Dimensiones_producto WHERE IdDimensiones = %s", (dimensiones_id,))
            if not cursor.fetchone():
                raise HTTPException(status_code=404, detail="Dimensiones de producto no encontradas")

            cursor.execute("DELETE FROM Dimensiones_producto WHERE IdDimensiones = %s", (dimensiones_id,))
            conn.commit()

            return {"mensaje": f"Dimensiones de producto con ID {dimensiones_id} eliminadas correctamente"}

        except mysql.connector.Error as err:
            print(f"Error al eliminar dimensiones de producto: {err}")
            conn.rollback()
            raise HTTPException(status_code=500, detail="Error al eliminar dimensiones de producto")

        finally:
            conn.close()
