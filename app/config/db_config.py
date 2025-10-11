import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="bpvgzsnq2k3dbwukve0u-mysql.services.clever-cloud.com",
        user="umt7vfxnypi7klan",
        password="VV1aQwo77jw9gCqYM2KH",
        database="bpvgzsnq2k3dbwukve0u"
    )