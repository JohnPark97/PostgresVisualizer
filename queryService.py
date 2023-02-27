from connection import ConnectionService
from common import comma_join

class QueryService():
    def connection():
        return ConnectionService.connect()
    
    def cursor(): 
        return ConnectionService.connect().cursor()

    def get(table):
        cursor = QueryService.cursor()
        queryStatement = f"SELECT * FROM {table}"
        cursor.execute(queryStatement)
        rows = cursor.fetchall()
        cursor.close()

        return rows

    def getTables():
        cursor = QueryService.cursor()
        queryStatement = f"SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'"
        cursor.execute(queryStatement)
        tables = cursor.fetchall()
        cursor.close()

        return tables

    def getHeaders(table):
        cursor = QueryService.cursor()
        queryStatement = f"SELECT * FROM {table} WHERE false"
        cursor.execute(queryStatement)
        rows = cursor.fetchall()

        headers = [i[0] for i in cursor.description]

        cursor.close()

        return headers

    def insert(table, columns, values):
        conn = QueryService.connection()
        cursor = conn.cursor()
        queryStatement = f"INSERT INTO {table} ({comma_join(columns)}) VALUES ({generate_variable_marks(columns)})"
        cursor.execute(queryStatement, tuple(values))
        conn.commit()

        cursor.close()
        conn.close()

    def update():
        pass

    def delete():
        pass

def generate_variable_marks(cols):
    return ', '.join(['%s' for i in range(len(cols))])