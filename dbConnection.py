import cx_Oracle
class DbConnection:
    def __init__(self):
        with open(r'dbcon', 'r', encoding='utf-8') as fp:
            constr = fp.read()
        self._conn = cx_Oracle.connect(constr)
        self._cursor = self._conn.cursor()

    def __del__(self):
        self._cursor.close()
        self._conn.close()

    def execute(self, sql):
        print(sql)
        self._cursor.execute(sql)

    def commit(self):
        self._conn.commit()

    def getData(self):
        data = []
        for i, in self._cursor.fetchall():
            data.append(i)
        return data