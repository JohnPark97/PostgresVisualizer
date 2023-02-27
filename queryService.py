from connection import ConnectionService

class QueryService():
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

    def insert(table, values):
        cursor = QueryService.cursor()
        queryStatement = f"INSERT INTO {table} VALUES ({values})"
        cursor.execute(queryStatement)

        cursor.close()

    def update():
        pass

    def delete():
        pass
