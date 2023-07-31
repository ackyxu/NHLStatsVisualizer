from .QueryEngine import QueryEngine


class InfoQuery:
    retrievedInfo = []

                    
    def __init__(self, qe: QueryEngine):
        self.qe = qe


    """
    calls the QueryEngine to perform specific queries
    """
    def getQuery(self):
        pass
    
    def performQuery(self, sql: str)->str:
        return self.qe.performQuery(sql)

    def getResults(self):
        if not self.emptyRetrivedInfo():
            return self.retrievedInfo
        else:
            raise RuntimeError("There are currently no results retrieved from the Database")

    def getResultsLatest(self):
        if not self.emptyRetrivedInfo():
            return self.retrievedInfo[-1]
        else:
            raise RuntimeError("There are currently no results retrieved from the Database")

    def emptyRetrivedInfo(self) -> bool:
        if len(self.retrievedInfo) == 0:
            return True
        else:
            return False

                


        