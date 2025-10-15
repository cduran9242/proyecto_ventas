from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
import mysql.connector
from app.config.db_config import get_db_connection

class ModuloRolController:

    def create_modulo_rol(self, modulo_rol):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            query = """
            INSERT INTO moduloXrol (rol_id, modulo_id, estado, created_at, updated_at)
            VALUES (%s, %s, %s, NOW(), NOW())
            """
            values = (modulo_rol.rol_id, modulo_rol.modulo_id, modulo_rol.estado)
            cursor.execute(query, values)
            conn.commit()

            return {"mensaje": "Relación módulo-rol creada exitosamente"}

        except mysql.connector.Error as err:
            print(f"Error al crear relación módulo-rol: {err}")
            conn.rollback()
            raise HTTPException(status_code=500, detail="Error al crear módulo-rol")

        finally:
            conn.close()

    def get_modulo_rol(self, id_relacion: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM moduloXrol WHERE id = %s", (id_relacion,))
            result = cursor.fetchone()

            if not result:
                raise HTTPException(status_code=404, detail="Relación no encontrada")

            content = {
                "id": int(result[0]),
                "rol_id": int(result[1]),
                "modulo_id": int(result[2]),
                "estado": result[3],
                "created_at": str(result[4]),
                "updated_at": str(result[5])
            }

            return jsonable_encoder(content)

        except mysql.connector.Error as err:
            print(f"Error al obtener relación módulo-rol: {err}")
            raise HTTPException(status_code=500, detail="Error al obtener relación")

        finally:
            conn.close()

    def get_modulos_por_rol(self, rol_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            query = """
            SELECT m.id, m.nombre, m.ruta, m.estado
            FROM moduloXrol mr
            INNER JOIN modulos m ON mr.modulo_id = m.id
            WHERE mr.rol_id = %s
            """
            cursor.execute(query, (rol_id,))
            result = cursor.fetchall()

            if not result:
                raise HTTPException(status_code=404, detail="No se encontraron módulos para este rol")

            payload = [
                {
                    "modulo_id": data[0],
                    "nombre": data[1],
                    "ruta": data[2],
                    "estado": data[3]
                } for data in result
            ]

            return {"resultado": jsonable_encoder(payload)}

        except mysql.connector.Error as err:
            print(f"Error al listar módulos por rol: {err}")
            raise HTTPException(status_code=500, detail="Error al listar módulos por rol")

        finally:
            conn.close()

    def delete_modulo_rol(self, id_relacion: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM moduloXrol WHERE id = %s", (id_relacion,))
            if not cursor.fetchone():
                raise HTTPException(status_code=404, detail="Relación no encontrada")

            cursor.execute("DELETE FROM moduloXrol WHERE id = %s", (id_relacion,))
            conn.commit()

            return {"mensaje": f"Relación con ID {id_relacion} eliminada correctamente"}

        except mysql.connector.Error as err:
            print(f"Error al eliminar relación módulo-rol: {err}")
            conn.rollback()
            raise HTTPException(status_code=500, detail="Error al eliminar relación módulo-rol")

        finally:
            conn.close()
