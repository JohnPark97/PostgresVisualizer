from connection import ConnectionService

class QueryService():
    def cursor(): 
        return ConnectionService.connect().cursor()

    def get(table):
        cursor = QueryService.cursor()
        queryStatement = f"SELECT * FROM {table}"
        cursor.execute(queryStatement)
        rows = cursor.fetchall()

        headers = [i[0] for i in cursor.description]

        cursor.close()

        return rows

    def getHeaders(table):
        cursor = QueryService.cursor()
        queryStatement = f"SELECT * FROM {table} WHERE false"
        cursor.execute(queryStatement)
        rows = cursor.fetchall()

        headers = [i[0] for i in cursor.description]

        cursor.close()

        return headers

    def insert():
        pass

    def update():
        pass

    def delete():
        pass