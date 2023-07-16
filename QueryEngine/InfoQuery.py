from .QueryEngine import QueryEngine


class InfoQuery:
    retrievedInfo = {}
    SQLTemplate = ""
    def __init__(self, qe: QueryEngine):
        self.qe = qe


    """
    calls the QueryEngine to perform specific queries
    """
    def performQuery(self, sql: str)->str:
        return self.qe.performQuery(sql)

        