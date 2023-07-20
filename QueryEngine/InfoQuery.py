from .QueryEngine import QueryEngine


class InfoQuery:
    retrievedInfo = []
    SQLTemplate = ""
    selectLine =    "SELECT id, COUNT(id) AS gp, SUM(goals) AS goals, SUM(assists) AS assists, (SUM(goals) + SUM(assists)) AS points,\
                    SUM(shots) AS shots, SUM(hits) AS hits, SUM(faceOffWins) AS faceOffWins, \
                    SUM(faceOffTaken) AS faceOffTaken, SUM(takeaways) AS takeaways, SUM(giveaways) AS giveaways"
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


    def emptyRetrivedInfo(self) -> bool:
        if len(self.retrievedInfo) == 0:
            raise RuntimeError("There are currently no results retrieved from the Database")
        else:
            return False

    def additionalAgg(self)-> None:
        if not self.emptyRetrivedInfo():
            for result in self.getResults():
                result["GoalsPerGame"] = result["goals"]/result["gp"]
                result["PointsPerGame"] = result["points"]/result["gp"]
                result["ShootingPct"] = result["goals"]/result["shots"] if result["shots"] else 0
                

        