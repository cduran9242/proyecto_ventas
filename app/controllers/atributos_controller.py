from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
import mysql.connector
from app.config.db_config import get_db_connection

class AtributoController:

    def create_atributo(self, atributo):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            query = """
            INSERT INTO atributos (nombre, tipo_dato, descripcion, es_requerido, estado, created_at, updated_at)
            VALUES (%s, %s, %s, %s, %s, NOW(), NOW())
            """
            values = (atributo.nombre, atributo.tipo_dato, atributo.descripcion, atributo.es_requerido, atributo.estado)
            cursor.execute(query, values)
            conn.commit()
            return {"mensaje": "Atributo creado exitosamente"}

        except mysql.connector.Error as err:
            print(f"Error al crear atributo: {err}")
            conn.rollback()
            raise HTTPException(status_code=500, detail="Error al crear atributo")

        finally:
            conn.close()

    def get_atributo(self, atributo_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM atributos WHERE id = %s", (atributo_id,))
            result = cursor.fetchone()

            if not result:
                raise HTTPException(status_code=404, detail="Atributo no encontrado")

            content = {
                "id": int(result[0]),
                "nombre": result[1],
                "tipo_dato": result[2],
                "descripcion": result[3],
                "es_requerido": bool(result[4]),
                "estado": result[5],
                "created_at": str(result[6]),
                "updated_at": str(result[7])
            }

            return jsonable_encoder(content)

        except mysql.connector.Error as err:
            print(f"Error al obtener atributo: {err}")
            raise HTTPException(status_code=500, detail="Error al obtener atributo")

        finally:
            conn.close()

    def get_atributos(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM atributos")
            result = cursor.fetchall()

            if not result:
                raise HTTPException(status_code=404, detail="No se encontraron atributos")

            payload = [
                {
                    "id": data[0],
                    "nombre": data[1],
                    "tipo_dato": data[2],
                    "descripcion": data[3],
                    "es_requerido": bool(data[4]),
                    "estado": data[5],
                    "created_at": str(data[6]),
                    "updated_at": str(data[7])
                } for data in result
            ]

            return {"resultado": jsonable_encoder(payload)}

        except mysql.connector.Error as err:
            print(f"Error al listar atributos: {err}")
            raise HTTPException(status_code=500, detail="Error al listar atributos")

        finally:
            conn.close()
