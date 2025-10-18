from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
import mysql.connector
from app.config.db_config import get_db_connection

class EstadoController:

    def create_estado(self, estado):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            query = """
            INSERT INTO estados (nombre, descripcion, created_at, updated_at)
            VALUES (%s, %s, NOW(), NOW())
            """
            values = (estado.nombre, estado.descripcion)
            cursor.execute(query, values)
            conn.commit()
            return {"mensaje": "Estado creado exitosamente"}

        except mysql.connector.Error as err:
            print(f"Error al crear estado: {err}")
            conn.rollback()
            raise HTTPException(status_code=500, detail="Error al crear estado")

        finally:
            conn.close()

    def get_estado(self, estado_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM estados WHERE id = %s", (estado_id,))
            result = cursor.fetchone()

            if not result:
                raise HTTPException(status_code=404, detail="Estado no encontrado")

            content = {
                "id": int(result[0]),
                "nombre": result[1],
                "descripcion": result[2],
                "created_at": str(result[3]),
                "updated_at": str(result[4])
            }

            return jsonable_encoder(content)

        except mysql.connector.Error as err:
            print(f"Error al obtener estado: {err}")
            raise HTTPException(status_code=500, detail="Error al obtener estado")

        finally:
            conn.close()

    def get_estados(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM estados")
            result = cursor.fetchall()

            if not result:
                raise HTTPException(status_code=404, detail="No se encontraron estados")

            payload = [
                {
                    "id": data[0],
                    "nombre": data[1],
                    "descripcion": data[2],
                    "created_at": str(data[3]),
                    "updated_at": str(data[4])
                }
                for data in result
            ]

            return {"resultado": jsonable_encoder(payload)}

        except mysql.connector.Error as err:
            print(f"Error al listar estados: {err}")
            raise HTTPException(status_code=500, detail="Error al listar estados")

        finally:
            conn.close()
