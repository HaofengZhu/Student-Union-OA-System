class DBManager:
    __DBIP = ""
    __DBpw = ""
    def __init__(self):
        pass

    @classmethod
    def setDatabase(cls,ip,pw):
        cls.__DBIP=ip
        cls.__DBpw=pw

    @classmethod
    def query(cls,sql_query):
        pass
