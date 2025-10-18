# app/controllers/ordenes_produccion_controller.py
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
import mysql.connector
from app.config.db_config import get_db_connection

class OrdenesProduccionController:

    def create_orden_produccion(self, orden):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            query = """
            INSERT INTO Ordenes_Produccion (Estado_Siguiente, Estado_Anterior, Fecha_Inicio, Fecha_Fin_Estimada, Fecha_Fin_Real, created_at, updated_at)
            VALUES (%s, %s, %s, %s, %s, NOW(), NOW())
            """
            values = (
                orden.Estado_Siguiente,
                orden.Estado_Anterior,
                orden.Fecha_Inicio,
                orden.Fecha_Fin_Estimada,
                orden.Fecha_Fin_Real
            )

            cursor.execute(query, values)
            orden_id = cursor.lastrowid
            conn.commit()

            return {"mensaje": "Orden de producción creada exitosamente", "IdWo": orden_id}

        except mysql.connector.Error as err:
            print(f"Error al crear orden de producción: {err}")
            conn.rollback()
            raise HTTPException(status_code=500, detail="Error al crear orden de producción")

        finally:
            conn.close()

    def get_orden_produccion(self, orden_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Ordenes_Produccion WHERE IdWo = %s", (orden_id,))
            result = cursor.fetchone()

            if not result:
                raise HTTPException(status_code=404, detail="Orden de producción no encontrada")

            content = {
                "IdWo": int(result[0]),
                "Estado_Siguiente": result[1],
                "Estado_Anterior": result[2],
                "Fecha_Inicio": str(result[3]) if result[3] else None,
                "Fecha_Fin_Estimada": str(result[4]) if result[4] else None,
                "Fecha_Fin_Real": str(result[5]) if result[5] else None,
                "created_at": str(result[6]),
                "updated_at": str(result[7])
            }

            return jsonable_encoder(content)

        except mysql.connector.Error as err:
            print(f"Error al obtener orden de producción: {err}")
            raise HTTPException(status_code=500, detail="Error al obtener orden de producción")

        finally:
            conn.close()

    def get_ordenes_produccion(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Ordenes_Produccion")
            result = cursor.fetchall()

            if not result:
                raise HTTPException(status_code=404, detail="No se encontraron órdenes de producción")

            payload = [
                {
                    "IdWo": data[0],
                    "Estado_Siguiente": data[1],
                    "Estado_Anterior": data[2],
                    "Fecha_Inicio": str(data[3]) if data[3] else None,
                    "Fecha_Fin_Estimada": str(data[4]) if data[4] else None,
                    "Fecha_Fin_Real": str(data[5]) if data[5] else None,
                    "created_at": str(data[6]),
                    "updated_at": str(data[7])
                } for data in result
            ]

            return {"resultado": jsonable_encoder(payload)}

        except mysql.connector.Error as err:
            print(f"Error al listar órdenes de producción: {err}")
            raise HTTPException(status_code=500, detail="Error al listar órdenes de producción")

        finally:
            conn.close()

    def get_ordenes_by_estado(self, estado: str):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Ordenes_Produccion WHERE Estado_Siguiente = %s", (estado,))
            result = cursor.fetchall()

            if not result:
                raise HTTPException(status_code=404, detail=f"No se encontraron órdenes con estado {estado}")

            payload = [
                {
                    "IdWo": data[0],
                    "Estado_Siguiente": data[1],
                    "Estado_Anterior": data[2],
                    "Fecha_Inicio": str(data[3]) if data[3] else None,
                    "Fecha_Fin_Estimada": str(data[4]) if data[4] else None,
                    "Fecha_Fin_Real": str(data[5]) if data[5] else None,
                    "created_at": str(data[6]),
                    "updated_at": str(data[7])
                } for data in result
            ]

            return {"resultado": jsonable_encoder(payload)}

        except mysql.connector.Error as err:
            print(f"Error al obtener órdenes por estado: {err}")
            raise HTTPException(status_code=500, detail="Error al obtener órdenes por estado")

        finally:
            conn.close()

    def update_orden_produccion(self, orden_id: int, orden):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT IdWo FROM Ordenes_Produccion WHERE IdWo = %s", (orden_id,))
            if not cursor.fetchone():
                raise HTTPException(status_code=404, detail="Orden de producción no encontrada")

            query = """
            UPDATE Ordenes_Produccion
            SET Estado_Siguiente = %s,
                Estado_Anterior = %s,
                Fecha_Inicio = %s,
                Fecha_Fin_Estimada = %s,
                Fecha_Fin_Real = %s,
                updated_at = NOW()
            WHERE IdWo = %s
            """
            values = (
                orden.Estado_Siguiente,
                orden.Estado_Anterior,
                orden.Fecha_Inicio,
                orden.Fecha_Fin_Estimada,
                orden.Fecha_Fin_Real,
                orden_id
            )

            cursor.execute(query, values)
            conn.commit()

            return {"mensaje": f"Orden de producción con ID {orden_id} actualizada correctamente"}

        except mysql.connector.Error as err:
            print(f"Error al actualizar orden de producción: {err}")
            conn.rollback()
            raise HTTPException(status_code=500, detail="Error al actualizar orden de producción")

        finally:
            conn.close()

    def delete_orden_produccion(self, orden_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT IdWo FROM Ordenes_Produccion WHERE IdWo = %s", (orden_id,))
            if not cursor.fetchone():
                raise HTTPException(status_code=404, detail="Orden de producción no encontrada")

            cursor.execute("DELETE FROM Ordenes_Produccion WHERE IdWo = %s", (orden_id,))
            conn.commit()

            return {"mensaje": f"Orden de producción con ID {orden_id} eliminada correctamente"}

        except mysql.connector.Error as err:
            print(f"Error al eliminar orden de producción: {err}")
            conn.rollback()
            raise HTTPException(status_code=500, detail="Error al eliminar orden de producción")

        finally:
            conn.close()

    def cambiar_estado_orden(self, orden_id: int, nuevo_estado: str):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            # Obtener el estado actual
            cursor.execute("SELECT Estado_Siguiente FROM Ordenes_Produccion WHERE IdWo = %s", (orden_id,))
            result = cursor.fetchone()
            
            if not result:
                raise HTTPException(status_code=404, detail="Orden de producción no encontrada")

            estado_anterior = result[0]

            # Actualizar el estado
            query = """
            UPDATE Ordenes_Produccion
            SET Estado_Anterior = %s,
                Estado_Siguiente = %s,
                updated_at = NOW()
            WHERE IdWo = %s
            """
            values = (estado_anterior, nuevo_estado, orden_id)

            cursor.execute(query, values)
            conn.commit()

            return {"mensaje": f"Estado de orden {orden_id} cambiado de {estado_anterior} a {nuevo_estado}"}

        except mysql.connector.Error as err:
            print(f"Error al cambiar estado de orden: {err}")
            conn.rollback()
            raise HTTPException(status_code=500, detail="Error al cambiar estado de orden")

        finally:
            conn.close()
