# app/controllers/atributosXusuarios_controller.py
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
import mysql.connector
from app.config.db_config import get_db_connection

class AtributosXusuariosController:

    def create_atributo_usuario(self, atributo_usuario):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            # Verificar que el usuario existe
            cursor.execute("SELECT id FROM usuarios WHERE id = %s", (atributo_usuario.usuario_id,))
            if not cursor.fetchone():
                raise HTTPException(status_code=400, detail="El usuario no existe")

            # Verificar que el atributo existe
            cursor.execute("SELECT id FROM atributos WHERE id = %s", (atributo_usuario.atributo_id,))
            if not cursor.fetchone():
                raise HTTPException(status_code=400, detail="El atributo no existe")

            query = """
            INSERT INTO atributoXusuario (usuario_id, atributo_id, tipo, valor, estado_id, created_at, updated_at)
            VALUES (%s, %s, %s, %s, %s, NOW(), NOW())
            """
            values = (
                atributo_usuario.usuario_id,
                atributo_usuario.atributo_id,
                atributo_usuario.tipo,
                atributo_usuario.valor,
                atributo_usuario.estado_id
            )

            cursor.execute(query, values)
            conn.commit()

            return {"mensaje": "Atributo de usuario creado exitosamente"}

        except mysql.connector.Error as err:
            print(f"Error al crear atributo de usuario: {err}")
            conn.rollback()
            raise HTTPException(status_code=500, detail="Error al crear atributo de usuario")

        finally:
            conn.close()

    def get_atributo_usuario(self, atributo_usuario_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM atributoXusuario WHERE id = %s", (atributo_usuario_id,))
            result = cursor.fetchone()

            if not result:
                raise HTTPException(status_code=404, detail="Atributo de usuario no encontrado")

            content = {
                "id": int(result[0]),
                "usuario_id": int(result[1]),
                "atributo_id": int(result[2]),
                "tipo": result[3],
                "valor": result[4],
                "estado_id": int(result[5]),
                "created_at": str(result[6]),
                "updated_at": str(result[7])
            }

            return jsonable_encoder(content)

        except mysql.connector.Error as err:
            print(f"Error al obtener atributo de usuario: {err}")
            raise HTTPException(status_code=500, detail="Error al obtener atributo de usuario")

        finally:
            conn.close()

    def get_atributos_by_usuario(self, usuario_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                SELECT au.*, a.nombre as atributo_nombre, a.descripcion as atributo_descripcion
                FROM atributoXusuario au 
                INNER JOIN atributos a ON au.atributo_id = a.id 
                WHERE au.usuario_id = %s
            """, (usuario_id,))
            result = cursor.fetchall()

            if not result:
                raise HTTPException(status_code=404, detail="No se encontraron atributos para este usuario")

            payload = [
                {
                    "id": data[0],
                    "usuario_id": data[1],
                    "atributo_id": data[2],
                    "tipo": data[3],
                    "valor": data[4],
                    "estado_id": data[5],
                    "created_at": str(data[6]),
                    "updated_at": str(data[7]),
                    "atributo_nombre": data[8],
                    "atributo_descripcion": data[9]
                } for data in result
            ]

            return {"resultado": jsonable_encoder(payload)}

        except mysql.connector.Error as err:
            print(f"Error al obtener atributos por usuario: {err}")
            raise HTTPException(status_code=500, detail="Error al obtener atributos por usuario")

        finally:
            conn.close()

    def get_atributosXusuarios(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                SELECT au.*, a.nombre as atributo_nombre, u.nombres, u.apellidos
                FROM atributoXusuario au 
                INNER JOIN atributos a ON au.atributo_id = a.id 
                INNER JOIN usuarios u ON au.usuario_id = u.id
            """)
            result = cursor.fetchall()

            if not result:
                raise HTTPException(status_code=404, detail="No se encontraron atributos de usuarios")

            payload = [
                {
                    "id": data[0],
                    "usuario_id": data[1],
                    "atributo_id": data[2],
                    "tipo": data[3],
                    "valor": data[4],
                    "estado_id": data[5],
                    "created_at": str(data[6]),
                    "updated_at": str(data[7]),
                    "atributo_nombre": data[8],
                    "usuario_nombre": f"{data[9]} {data[10]}"
                } for data in result
            ]

            return {"resultado": jsonable_encoder(payload)}

        except mysql.connector.Error as err:
            print(f"Error al listar atributos de usuarios: {err}")
            raise HTTPException(status_code=500, detail="Error al listar atributos de usuarios")

        finally:
            conn.close()

    def update_atributo_usuario(self, atributo_usuario_id: int, atributo_usuario):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT id FROM atributoXusuario WHERE id = %s", (atributo_usuario_id,))
            if not cursor.fetchone():
                raise HTTPException(status_code=404, detail="Atributo de usuario no encontrado")

            query = """
            UPDATE atributoXusuario
            SET usuario_id = %s,
                atributo_id = %s,
                tipo = %s,
                valor = %s,
                estado_id = %s,
                updated_at = NOW()
            WHERE id = %s
            """
            values = (
                atributo_usuario.usuario_id,
                atributo_usuario.atributo_id,
                atributo_usuario.tipo,
                atributo_usuario.valor,
                atributo_usuario.estado_id,
                atributo_usuario_id
            )

            cursor.execute(query, values)
            conn.commit()

            return {"mensaje": f"Atributo de usuario con ID {atributo_usuario_id} actualizado correctamente"}

        except mysql.connector.Error as err:
            print(f"Error al actualizar atributo de usuario: {err}")
            conn.rollback()
            raise HTTPException(status_code=500, detail="Error al actualizar atributo de usuario")

        finally:
            conn.close()

    def delete_atributo_usuario(self, atributo_usuario_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT id FROM atributoXusuario WHERE id = %s", (atributo_usuario_id,))
            if not cursor.fetchone():
                raise HTTPException(status_code=404, detail="Atributo de usuario no encontrado")

            cursor.execute("DELETE FROM atributoXusuario WHERE id = %s", (atributo_usuario_id,))
            conn.commit()

            return {"mensaje": f"Atributo de usuario con ID {atributo_usuario_id} eliminado correctamente"}

        except mysql.connector.Error as err:
            print(f"Error al eliminar atributo de usuario: {err}")
            conn.rollback()
            raise HTTPException(status_code=500, detail="Error al eliminar atributo de usuario")

        finally:
            conn.close()