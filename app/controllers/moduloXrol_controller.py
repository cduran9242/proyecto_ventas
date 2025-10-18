# app/controllers/moduloXrol_controller.py
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
import mysql.connector
from app.config.db_config import get_db_connection

class ModuloXrolController:

    def create_modulo_rol(self, modulo_rol):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            # Verificar que el rol existe
            cursor.execute("SELECT id FROM roles WHERE id = %s", (modulo_rol.rol_id,))
            if not cursor.fetchone():
                raise HTTPException(status_code=400, detail="El rol no existe")

            # Verificar que el módulo existe
            cursor.execute("SELECT id FROM modulos WHERE id = %s", (modulo_rol.modulo_id,))
            if not cursor.fetchone():
                raise HTTPException(status_code=400, detail="El módulo no existe")

            # Verificar que la combinación rol-módulo no existe
            cursor.execute("SELECT id FROM moduloXrol WHERE rol_id = %s AND modulo_id = %s", 
                          (modulo_rol.rol_id, modulo_rol.modulo_id))
            if cursor.fetchone():
                raise HTTPException(status_code=400, detail="Esta combinación rol-módulo ya existe")

            query = """
            INSERT INTO moduloXrol (rol_id, modulo_id, permisos, estado_id, created_at, updated_at)
            VALUES (%s, %s, %s, %s, NOW(), NOW())
            """
            values = (
                modulo_rol.rol_id,
                modulo_rol.modulo_id,
                modulo_rol.permisos,
                modulo_rol.estado_id
            )

            cursor.execute(query, values)
            conn.commit()

            return {"mensaje": "Permiso de módulo por rol creado exitosamente"}

        except mysql.connector.Error as err:
            print(f"Error al crear permiso de módulo por rol: {err}")
            conn.rollback()
            raise HTTPException(status_code=500, detail="Error al crear permiso de módulo por rol")

        finally:
            conn.close()

    def get_modulo_rol(self, modulo_rol_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM moduloXrol WHERE id = %s", (modulo_rol_id,))
            result = cursor.fetchone()

            if not result:
                raise HTTPException(status_code=404, detail="Permiso de módulo por rol no encontrado")

            content = {
                "id": int(result[0]),
                "rol_id": int(result[1]),
                "modulo_id": int(result[2]),
                "permisos": result[3],
                "estado_id": int(result[4]),
                "created_at": str(result[5]),
                "updated_at": str(result[6])
            }

            return jsonable_encoder(content)

        except mysql.connector.Error as err:
            print(f"Error al obtener permiso de módulo por rol: {err}")
            raise HTTPException(status_code=500, detail="Error al obtener permiso de módulo por rol")

        finally:
            conn.close()

    def get_modulos_by_rol(self, rol_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                SELECT mxr.*, m.nombre as modulo_nombre, m.descripcion as modulo_descripcion, m.ruta
                FROM moduloXrol mxr 
                INNER JOIN modulos m ON mxr.modulo_id = m.id 
                WHERE mxr.rol_id = %s
            """, (rol_id,))
            result = cursor.fetchall()

            if not result:
                raise HTTPException(status_code=404, detail="No se encontraron módulos para este rol")

            payload = [
                {
                    "id": data[0],
                    "rol_id": data[1],
                    "modulo_id": data[2],
                    "permisos": data[3],
                    "estado_id": data[4],
                    "created_at": str(data[5]),
                    "updated_at": str(data[6]),
                    "modulo_nombre": data[7],
                    "modulo_descripcion": data[8],
                    "ruta": data[9]
                } for data in result
            ]

            return {"resultado": jsonable_encoder(payload)}

        except mysql.connector.Error as err:
            print(f"Error al obtener módulos por rol: {err}")
            raise HTTPException(status_code=500, detail="Error al obtener módulos por rol")

        finally:
            conn.close()

    def get_roles_by_modulo(self, modulo_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                SELECT mxr.*, r.nombre as rol_nombre, r.descripcion as rol_descripcion
                FROM moduloXrol mxr 
                INNER JOIN roles r ON mxr.rol_id = r.id 
                WHERE mxr.modulo_id = %s
            """, (modulo_id,))
            result = cursor.fetchall()

            if not result:
                raise HTTPException(status_code=404, detail="No se encontraron roles para este módulo")

            payload = [
                {
                    "id": data[0],
                    "rol_id": data[1],
                    "modulo_id": data[2],
                    "permisos": data[3],
                    "estado_id": data[4],
                    "created_at": str(data[5]),
                    "updated_at": str(data[6]),
                    "rol_nombre": data[7],
                    "rol_descripcion": data[8]
                } for data in result
            ]

            return {"resultado": jsonable_encoder(payload)}

        except mysql.connector.Error as err:
            print(f"Error al obtener roles por módulo: {err}")
            raise HTTPException(status_code=500, detail="Error al obtener roles por módulo")

        finally:
            conn.close()

    def get_moduloXrol(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                SELECT mxr.*, r.nombre as rol_nombre, m.nombre as modulo_nombre
                FROM moduloXrol mxr 
                INNER JOIN roles r ON mxr.rol_id = r.id 
                INNER JOIN modulos m ON mxr.modulo_id = m.id
            """)
            result = cursor.fetchall()

            if not result:
                raise HTTPException(status_code=404, detail="No se encontraron permisos de módulos por rol")

            payload = [
                {
                    "id": data[0],
                    "rol_id": data[1],
                    "modulo_id": data[2],
                    "permisos": data[3],
                    "estado_id": data[4],
                    "created_at": str(data[5]),
                    "updated_at": str(data[6]),
                    "rol_nombre": data[7],
                    "modulo_nombre": data[8]
                } for data in result
            ]

            return {"resultado": jsonable_encoder(payload)}

        except mysql.connector.Error as err:
            print(f"Error al listar permisos de módulos por rol: {err}")
            raise HTTPException(status_code=500, detail="Error al listar permisos de módulos por rol")

        finally:
            conn.close()

    def update_modulo_rol(self, modulo_rol_id: int, modulo_rol):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT id FROM moduloXrol WHERE id = %s", (modulo_rol_id,))
            if not cursor.fetchone():
                raise HTTPException(status_code=404, detail="Permiso de módulo por rol no encontrado")

            query = """
            UPDATE moduloXrol
            SET rol_id = %s,
                modulo_id = %s,
                permisos = %s,
                estado_id = %s,
                updated_at = NOW()
            WHERE id = %s
            """
            values = (
                modulo_rol.rol_id,
                modulo_rol.modulo_id,
                modulo_rol.permisos,
                modulo_rol.estado_id,
                modulo_rol_id
            )

            cursor.execute(query, values)
            conn.commit()

            return {"mensaje": f"Permiso de módulo por rol con ID {modulo_rol_id} actualizado correctamente"}

        except mysql.connector.Error as err:
            print(f"Error al actualizar permiso de módulo por rol: {err}")
            conn.rollback()
            raise HTTPException(status_code=500, detail="Error al actualizar permiso de módulo por rol")

        finally:
            conn.close()

    def delete_modulo_rol(self, modulo_rol_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT id FROM moduloXrol WHERE id = %s", (modulo_rol_id,))
            if not cursor.fetchone():
                raise HTTPException(status_code=404, detail="Permiso de módulo por rol no encontrado")

            cursor.execute("DELETE FROM moduloXrol WHERE id = %s", (modulo_rol_id,))
            conn.commit()

            return {"mensaje": f"Permiso de módulo por rol con ID {modulo_rol_id} eliminado correctamente"}

        except mysql.connector.Error as err:
            print(f"Error al eliminar permiso de módulo por rol: {err}")
            conn.rollback()
            raise HTTPException(status_code=500, detail="Error al eliminar permiso de módulo por rol")

        finally:
            conn.close()