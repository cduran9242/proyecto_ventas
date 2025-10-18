# app/controllers/producto_controller.py
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
import mysql.connector
from app.config.db_config import get_db_connection

class ProductoController:

    def create_producto(self, producto):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            # Verificar si el código de producto ya existe
            cursor.execute("SELECT IdProductos FROM Productos WHERE Codigo_producto = %s", (producto.Codigo_producto,))
            if cursor.fetchone():
                raise HTTPException(status_code=400, detail="El código de producto ya existe")

            query = """
            INSERT INTO Productos (Codigo_producto, Nombre_Producto, Descripcion, Categoria, Unidad_medida, estado, created_at, updated_at)
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

    def get_producto(self, producto_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Productos WHERE IdProductos = %s", (producto_id,))
            result = cursor.fetchone()

            if not result:
                raise HTTPException(status_code=404, detail="Producto no encontrado")

            content = {
                "IdProductos": int(result[0]),
                "Codigo_producto": result[1],
                "Nombre_Producto": result[2],
                "Descripcion": result[3],
                "Categoria": result[4],
                "Unidad_medida": result[5],
                "estado": bool(result[6]) if result[6] is not None else None,
                "created_at": str(result[7]),
                "updated_at": str(result[8])
            }

            return jsonable_encoder(content)

        except mysql.connector.Error as err:
            print(f"Error al obtener producto: {err}")
            raise HTTPException(status_code=500, detail="Error al obtener producto")

        finally:
            conn.close()

    def get_productos(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Productos")
            result = cursor.fetchall()

            if not result:
                raise HTTPException(status_code=404, detail="No se encontraron productos")

            payload = [
                {
                    "IdProductos": data[0],
                    "Codigo_producto": data[1],
                    "Nombre_Producto": data[2],
                    "Descripcion": data[3],
                    "Categoria": data[4],
                    "Unidad_medida": data[5],
                    "estado": bool(data[6]) if data[6] is not None else None,
                    "created_at": str(data[7]),
                    "updated_at": str(data[8])
                } for data in result
            ]

            return {"resultado": jsonable_encoder(payload)}

        except mysql.connector.Error as err:
            print(f"Error al listar productos: {err}")
            raise HTTPException(status_code=500, detail="Error al listar productos")

        finally:
            conn.close()

    def update_producto(self, producto_id: int, producto):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT IdProductos FROM Productos WHERE IdProductos = %s", (producto_id,))
            if not cursor.fetchone():
                raise HTTPException(status_code=404, detail="Producto no encontrado")

            query = """
            UPDATE Productos
            SET Codigo_producto = %s,
                Nombre_Producto = %s,
                Descripcion = %s,
                Categoria = %s,
                Unidad_medida = %s,
                estado = %s,
                updated_at = NOW()
            WHERE IdProductos = %s
            """
            values = (
                producto.Codigo_producto,
                producto.Nombre_Producto,
                producto.Descripcion,
                producto.Categoria,
                producto.Unidad_medida,
                producto.estado,
                producto_id
            )

            cursor.execute(query, values)
            conn.commit()

            return {"mensaje": f"Producto con ID {producto_id} actualizado correctamente"}

        except mysql.connector.Error as err:
            print(f"Error al actualizar producto: {err}")
            conn.rollback()
            raise HTTPException(status_code=500, detail="Error al actualizar producto")

        finally:
            conn.close()

    def delete_producto(self, producto_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT IdProductos FROM Productos WHERE IdProductos = %s", (producto_id,))
            if not cursor.fetchone():
                raise HTTPException(status_code=404, detail="Producto no encontrado")

            cursor.execute("DELETE FROM Productos WHERE IdProductos = %s", (producto_id,))
            conn.commit()

            return {"mensaje": f"Producto con ID {producto_id} eliminado correctamente"}

        except mysql.connector.Error as err:
            print(f"Error al eliminar producto: {err}")
            conn.rollback()
            raise HTTPException(status_code=500, detail="Error al eliminar producto")

        finally:
            conn.close()