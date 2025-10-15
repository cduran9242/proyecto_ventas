from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
import mysql.connector
from app.config.db_config import get_db_connection

class RolController:

    def create_rol(self, rol):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            query = """
            INSERT INTO roles (nombre, descripcion, estado, created_at, updated_at)
            VALUES (%s, %s, %s, NOW(), NOW())
            """
            values = (rol.nombre, rol.descripcion, rol.estado)
            cursor.execute(query, values)
            conn.commit()

            return {"mensaje": "Rol creado exitosamente"}

        except mysql.connector.Error as err:
            print(f"Error al crear rol: {err}")
            conn.rollback()
            raise HTTPException(status_code=500, detail="Error al crear rol")

        finally:
            conn.close()

    def get_rol(self, rol_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM roles WHERE id = %s", (rol_id,))
            result = cursor.fetchone()

            if not result:
                raise HTTPException(status_code=404, detail="Rol no encontrado")

            content = {
                "id": int(result[0]),
                "nombre": result[1],
                "descripcion": result[2],
                "estado": result[3],
                "created_at": str(result[4]),
                "updated_at": str(result[5])
            }

            return jsonable_encoder(content)

        except mysql.connector.Error as err:
            print(f"Error al obtener rol: {err}")
            raise HTTPException(status_code=500, detail="Error al obtener rol")

        finally:
            conn.close()

    def get_roles(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM roles")
            result = cursor.fetchall()

            payload = [
                {
                    "id": data[0],
                    "nombre": data[1],
                    "descripcion": data[2],
                    "estado": data[3],
                    "created_at": str(data[4]),
                    "updated_at": str(data[5])
                } for data in result
            ]

            if not result:
                raise HTTPException(status_code=404, detail="No se encontraron roles")

            return {"resultado": jsonable_encoder(payload)}

        except mysql.connector.Error as err:
            print(f"Error al listar roles: {err}")
            raise HTTPException(status_code=500, detail="Error al listar roles")

        finally:
            conn.close()

    def update_rol(self, rol_id: int, rol):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM roles WHERE id = %s", (rol_id,))
            if not cursor.fetchone():
                raise HTTPException(status_code=404, detail="Rol no encontrado")

            query = """
            UPDATE roles
            SET nombre = %s, descripcion = %s, estado = %s, updated_at = NOW()
            WHERE id = %s
            """
            values = (rol.nombre, rol.descripcion, rol.estado, rol_id)
            cursor.execute(query, values)
            conn.commit()

            return {"mensaje": f"Rol con ID {rol_id} actualizado correctamente"}

        except mysql.connector.Error as err:
            print(f"Error al actualizar rol: {err}")
            conn.rollback()
            raise HTTPException(status_code=500, detail="Error al actualizar rol")

        finally:
            conn.close()

    def delete_rol(self, rol_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM roles WHERE id = %s", (rol_id,))
            if not cursor.fetchone():
                raise HTTPException(status_code=404, detail="Rol no encontrado")

            cursor.execute("DELETE FROM roles WHERE id = %s", (rol_id,))
            conn.commit()

            return {"mensaje": f"Rol con ID {rol_id} eliminado correctamente"}

        except mysql.connector.Error as err:
            print(f"Error al eliminar rol: {err}")
            conn.rollback()
            raise HTTPException(status_code=500, detail="Error al eliminar rol")

        finally:
            conn.close()
