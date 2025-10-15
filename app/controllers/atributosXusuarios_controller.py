from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
import mysql.connector
from app.config.db_config import get_db_connection

class AtributoUsuarioController:

    def create_atributo_usuario(self, atributo_usuario):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            query = """
            INSERT INTO atributoXusuario (usuario_id, atributo_id, tipo, valor, estado, created_at, updated_at)
            VALUES (%s, %s, %s, %s, %s, NOW(), NOW())
            """
            values = (
                atributo_usuario.usuario_id,
                atributo_usuario.atributo_id,
                atributo_usuario.tipo,
                atributo_usuario.valor,
                atributo_usuario.estado
            )
            cursor.execute(query, values)
            conn.commit()

            return {"mensaje": "Atributo asignado al usuario correctamente"}

        except mysql.connector.Error as err:
            print(f"Error al crear atributo de usuario: {err}")
            conn.rollback()
            raise HTTPException(status_code=500, detail="Error al asignar atributo al usuario")

        finally:
            conn.close()

    def get_atributos_por_usuario(self, usuario_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            query = """
            SELECT a.nombre, au.tipo, au.valor, au.estado
            FROM atributoXusuario au
            INNER JOIN atributos a ON au.atributo_id = a.id
            WHERE au.usuario_id = %s
            """
            cursor.execute(query, (usuario_id,))
            result = cursor.fetchall()

            if not result:
                raise HTTPException(status_code=404, detail="No se encontraron atributos para este usuario")

            payload = [
                {
                    "atributo": data[0],
                    "tipo": data[1],
                    "valor": data[2],
                    "estado": data[3]
                } for data in result
            ]

            return {"resultado": jsonable_encoder(payload)}

        except mysql.connector.Error as err:
            print(f"Error al obtener atributos de usuario: {err}")
            raise HTTPException(status_code=500, detail="Error al obtener atributos del usuario")

        finally:
            conn.close()

    def delete_atributo_usuario(self, id_relacion: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM atributoXusuario WHERE id = %s", (id_relacion,))
            if not cursor.fetchone():
                raise HTTPException(status_code=404, detail="Relación no encontrada")

            cursor.execute("DELETE FROM atributoXusuario WHERE id = %s", (id_relacion,))
            conn.commit()

            return {"mensaje": f"Atributo de usuario con ID {id_relacion} eliminado correctamente"}

        except mysql.connector.Error as err:
            print(f"Error al eliminar atributo de usuario: {err}")
            conn.rollback()
            raise HTTPException(status_code=500, detail="Error al eliminar atributo de usuario")

        finally:
            conn.close()
