# app/controllers/detalle_wo_controller.py
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
import mysql.connector
from app.config.db_config import get_db_connection

class DetalleWoController:

    def create_detalle_wo(self, detalle_wo):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            # Verificar que la orden de trabajo existe
            cursor.execute("SELECT IdWo FROM Ordenes_Produccion WHERE IdWo = %s", (detalle_wo.IdWo,))
            if not cursor.fetchone():
                raise HTTPException(status_code=400, detail="La orden de trabajo no existe")

            # Verificar que el producto existe
            cursor.execute("SELECT IdProductos FROM Productos WHERE IdProductos = %s", (detalle_wo.IdProducto,))
            if not cursor.fetchone():
                raise HTTPException(status_code=400, detail="El producto no existe")

            query = """
            INSERT INTO Detalle_Wo (IdWo, IdPedido, IdProducto, Cantidad_Solicitada, Cantidad_Producida, created_at, updated_at)
            VALUES (%s, %s, %s, %s, %s, NOW(), NOW())
            """
            values = (
                detalle_wo.IdWo,
                detalle_wo.IdPedido,
                detalle_wo.IdProducto,
                detalle_wo.Cantidad_Solicitada,
                detalle_wo.Cantidad_Producida
            )

            cursor.execute(query, values)
            conn.commit()

            return {"mensaje": "Detalle de orden de trabajo creado exitosamente"}

        except mysql.connector.Error as err:
            print(f"Error al crear detalle de orden de trabajo: {err}")
            conn.rollback()
            raise HTTPException(status_code=500, detail="Error al crear detalle de orden de trabajo")

        finally:
            conn.close()

    def get_detalle_wo(self, detalle_wo_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Detalle_Wo WHERE Id_Detalle_WO = %s", (detalle_wo_id,))
            result = cursor.fetchone()

            if not result:
                raise HTTPException(status_code=404, detail="Detalle de orden de trabajo no encontrado")

            content = {
                "Id_Detalle_WO": int(result[0]),
                "IdWo": int(result[1]),
                "IdPedido": result[2],
                "IdProducto": int(result[3]),
                "Cantidad_Solicitada": float(result[4]),
                "Cantidad_Producida": float(result[5]) if result[5] else None,
                "created_at": str(result[6]),
                "updated_at": str(result[7])
            }

            return jsonable_encoder(content)

        except mysql.connector.Error as err:
            print(f"Error al obtener detalle de orden de trabajo: {err}")
            raise HTTPException(status_code=500, detail="Error al obtener detalle de orden de trabajo")

        finally:
            conn.close()

    def get_detalles_by_wo(self, wo_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                SELECT dw.*, p.Nombre_Producto, p.Codigo_producto 
                FROM Detalle_Wo dw 
                INNER JOIN Productos p ON dw.IdProducto = p.IdProductos 
                WHERE dw.IdWo = %s
            """, (wo_id,))
            result = cursor.fetchall()

            if not result:
                raise HTTPException(status_code=404, detail="No se encontraron detalles para esta orden de trabajo")

            payload = [
                {
                    "Id_Detalle_WO": data[0],
                    "IdWo": data[1],
                    "IdPedido": data[2],
                    "IdProducto": data[3],
                    "Cantidad_Solicitada": float(data[4]),
                    "Cantidad_Producida": float(data[5]) if data[5] else None,
                    "created_at": str(data[6]),
                    "updated_at": str(data[7]),
                    "Nombre_Producto": data[8],
                    "Codigo_producto": data[9]
                } for data in result
            ]

            return {"resultado": jsonable_encoder(payload)}

        except mysql.connector.Error as err:
            print(f"Error al obtener detalles por orden de trabajo: {err}")
            raise HTTPException(status_code=500, detail="Error al obtener detalles por orden de trabajo")

        finally:
            conn.close()

    def get_all_detalles_wo(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                SELECT dw.*, p.Nombre_Producto, p.Codigo_producto, op.Estado_Siguiente
                FROM Detalle_Wo dw 
                INNER JOIN Productos p ON dw.IdProducto = p.IdProductos 
                INNER JOIN Ordenes_Produccion op ON dw.IdWo = op.IdWo
            """)
            result = cursor.fetchall()

            if not result:
                raise HTTPException(status_code=404, detail="No se encontraron detalles de órdenes de trabajo")

            payload = [
                {
                    "Id_Detalle_WO": data[0],
                    "IdWo": data[1],
                    "IdPedido": data[2],
                    "IdProducto": data[3],
                    "Cantidad_Solicitada": float(data[4]),
                    "Cantidad_Producida": float(data[5]) if data[5] else None,
                    "created_at": str(data[6]),
                    "updated_at": str(data[7]),
                    "Nombre_Producto": data[8],
                    "Codigo_producto": data[9],
                    "Estado_Orden": data[10]
                } for data in result
            ]

            return {"resultado": jsonable_encoder(payload)}

        except mysql.connector.Error as err:
            print(f"Error al listar detalles de órdenes de trabajo: {err}")
            raise HTTPException(status_code=500, detail="Error al listar detalles de órdenes de trabajo")

        finally:
            conn.close()

    def update_detalle_wo(self, detalle_wo_id: int, detalle_wo):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT Id_Detalle_WO FROM Detalle_Wo WHERE Id_Detalle_WO = %s", (detalle_wo_id,))
            if not cursor.fetchone():
                raise HTTPException(status_code=404, detail="Detalle de orden de trabajo no encontrado")

            query = """
            UPDATE Detalle_Wo
            SET IdWo = %s,
                IdPedido = %s,
                IdProducto = %s,
                Cantidad_Solicitada = %s,
                Cantidad_Producida = %s,
                updated_at = NOW()
            WHERE Id_Detalle_WO = %s
            """
            values = (
                detalle_wo.IdWo,
                detalle_wo.IdPedido,
                detalle_wo.IdProducto,
                detalle_wo.Cantidad_Solicitada,
                detalle_wo.Cantidad_Producida,
                detalle_wo_id
            )

            cursor.execute(query, values)
            conn.commit()

            return {"mensaje": f"Detalle de orden de trabajo con ID {detalle_wo_id} actualizado correctamente"}

        except mysql.connector.Error as err:
            print(f"Error al actualizar detalle de orden de trabajo: {err}")
            conn.rollback()
            raise HTTPException(status_code=500, detail="Error al actualizar detalle de orden de trabajo")

        finally:
            conn.close()

    def delete_detalle_wo(self, detalle_wo_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT Id_Detalle_WO FROM Detalle_Wo WHERE Id_Detalle_WO = %s", (detalle_wo_id,))
            if not cursor.fetchone():
                raise HTTPException(status_code=404, detail="Detalle de orden de trabajo no encontrado")

            cursor.execute("DELETE FROM Detalle_Wo WHERE Id_Detalle_WO = %s", (detalle_wo_id,))
            conn.commit()

            return {"mensaje": f"Detalle de orden de trabajo con ID {detalle_wo_id} eliminado correctamente"}

        except mysql.connector.Error as err:
            print(f"Error al eliminar detalle de orden de trabajo: {err}")
            conn.rollback()
            raise HTTPException(status_code=500, detail="Error al eliminar detalle de orden de trabajo")

        finally:
            conn.close()
