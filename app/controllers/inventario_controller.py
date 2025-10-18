# app/controllers/inventario_controller.py
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
import mysql.connector
from app.config.db_config import get_db_connection

class InventarioController:

    def create_inventario(self, inventario):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            # Verificar que el producto existe
            cursor.execute("SELECT IdProductos FROM Productos WHERE IdProductos = %s", (inventario.IdProducto,))
            if not cursor.fetchone():
                raise HTTPException(status_code=400, detail="El producto no existe")

            query = """
            INSERT INTO Inventario (IdProducto, Lote, Cantidad_disponible, created_at, updated_at)
            VALUES (%s, %s, %s, NOW(), NOW())
            """
            values = (
                inventario.IdProducto,
                inventario.Lote,
                inventario.Cantidad_disponible
            )

            cursor.execute(query, values)
            conn.commit()

            return {"mensaje": "Registro de inventario creado exitosamente"}

        except mysql.connector.Error as err:
            print(f"Error al crear inventario: {err}")
            conn.rollback()
            raise HTTPException(status_code=500, detail="Error al crear inventario")

        finally:
            conn.close()

    def get_inventario(self, inventario_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Inventario WHERE Idinvnetario = %s", (inventario_id,))
            result = cursor.fetchone()

            if not result:
                raise HTTPException(status_code=404, detail="Registro de inventario no encontrado")

            content = {
                "Idinvnetario": int(result[0]),
                "IdProducto": int(result[1]),
                "Lote": result[2],
                "Cantidad_disponible": float(result[3]),
                "created_at": str(result[4]),
                "updated_at": str(result[5])
            }

            return jsonable_encoder(content)

        except mysql.connector.Error as err:
            print(f"Error al obtener inventario: {err}")
            raise HTTPException(status_code=500, detail="Error al obtener inventario")

        finally:
            conn.close()

    def get_inventario_by_producto(self, producto_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Inventario WHERE IdProducto = %s", (producto_id,))
            result = cursor.fetchall()

            if not result:
                raise HTTPException(status_code=404, detail="No se encontró inventario para este producto")

            payload = [
                {
                    "Idinvnetario": data[0],
                    "IdProducto": data[1],
                    "Lote": data[2],
                    "Cantidad_disponible": float(data[3]),
                    "created_at": str(data[4]),
                    "updated_at": str(data[5])
                } for data in result
            ]

            return {"resultado": jsonable_encoder(payload)}

        except mysql.connector.Error as err:
            print(f"Error al obtener inventario por producto: {err}")
            raise HTTPException(status_code=500, detail="Error al obtener inventario")

        finally:
            conn.close()

    def get_all_inventario(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                SELECT i.*, p.Nombre_Producto, p.Codigo_producto 
                FROM Inventario i 
                INNER JOIN Productos p ON i.IdProducto = p.IdProductos
            """)
            result = cursor.fetchall()

            if not result:
                raise HTTPException(status_code=404, detail="No se encontraron registros de inventario")

            payload = [
                {
                    "Idinvnetario": data[0],
                    "IdProducto": data[1],
                    "Lote": data[2],
                    "Cantidad_disponible": float(data[3]),
                    "created_at": str(data[4]),
                    "updated_at": str(data[5]),
                    "Nombre_Producto": data[6],
                    "Codigo_producto": data[7]
                } for data in result
            ]

            return {"resultado": jsonable_encoder(payload)}

        except mysql.connector.Error as err:
            print(f"Error al listar inventario: {err}")
            raise HTTPException(status_code=500, detail="Error al listar inventario")

        finally:
            conn.close()

    def update_inventario(self, inventario_id: int, inventario):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT Idinvnetario FROM Inventario WHERE Idinvnetario = %s", (inventario_id,))
            if not cursor.fetchone():
                raise HTTPException(status_code=404, detail="Registro de inventario no encontrado")

            query = """
            UPDATE Inventario
            SET IdProducto = %s,
                Lote = %s,
                Cantidad_disponible = %s,
                updated_at = NOW()
            WHERE Idinvnetario = %s
            """
            values = (
                inventario.IdProducto,
                inventario.Lote,
                inventario.Cantidad_disponible,
                inventario_id
            )

            cursor.execute(query, values)
            conn.commit()

            return {"mensaje": f"Inventario con ID {inventario_id} actualizado correctamente"}

        except mysql.connector.Error as err:
            print(f"Error al actualizar inventario: {err}")
            conn.rollback()
            raise HTTPException(status_code=500, detail="Error al actualizar inventario")

        finally:
            conn.close()

    def delete_inventario(self, inventario_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT Idinvnetario FROM Inventario WHERE Idinvnetario = %s", (inventario_id,))
            if not cursor.fetchone():
                raise HTTPException(status_code=404, detail="Registro de inventario no encontrado")

            cursor.execute("DELETE FROM Inventario WHERE Idinvnetario = %s", (inventario_id,))
            conn.commit()

            return {"mensaje": f"Inventario con ID {inventario_id} eliminado correctamente"}

        except mysql.connector.Error as err:
            print(f"Error al eliminar inventario: {err}")
            conn.rollback()
            raise HTTPException(status_code=500, detail="Error al eliminar inventario")

        finally:
            conn.close()