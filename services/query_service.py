from services.connection_service import ConnectionService
from common import comma_join, specifier_join

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

    def insert(table, columns, values, id_col):
        conn = QueryService.connection()
        cursor = conn.cursor()
        queryStatement = f"INSERT INTO {table} ({comma_join(columns)}) VALUES ({generate_variable_marks(columns)}) RETURNING {id_col}"
        cursor.execute(queryStatement, tuple(values))

        inserted_id = cursor.fetchone()[0]
        print(f"Inserted id: {inserted_id} values: {tuple(values)}")

        conn.commit()

        cursor.close()
        conn.close()

        return inserted_id

    def update(table, columns, values, id_col, id_val):
        conn = QueryService.connection()
        # Create a cursor
        cur = conn.cursor()

        queryStatement = f"UPDATE {table} SET {specifier_join(columns)} WHERE {id_col} = %s"
        values.append(id_val)
        # Execute an update statement
        cur.execute(queryStatement, tuple(values))

        # Commit the changes
        conn.commit()

        # Close the cursor and connection
        cur.close()
        conn.close()

    def delete():
        # TODO: Feb 27
        pass

def generate_variable_marks(cols):
    return ', '.join(['%s' for i in range(len(cols))])