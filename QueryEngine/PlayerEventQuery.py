from QueryEngine.EventQuery import EventQuery
from QueryEngine.QueryEngine import QueryEngine


class PlayerEventQuery(EventQuery):
    shotEvents = ['SHOT', 'MISSED_SHOT','BLOCKED_SHOT', 'GOAL']
    def __init__(self, qe: QueryEngine,id:int, year: int | list[int] | None):
        super().__init__(qe)
        self.year = year
        self.id = id


    def getQuery(self):
        sql = [self.selectFrom]

        sql.append("WHERE")

        if type(self.year) == int:
            sql.append(f"season = {self.year}{self.year+1}")
        elif type(self.year) == list:
            sql.append(f"season IN {[str(y)+str(y+1) for y in self.year]}")

        if  self.year:
            sql.append(f"AND (player1 = {self.id} OR player2 = {self.id} OR player3 = {self.id} OR player4 = {self.id})")
        else:
            sql.append(f"WHERE player1 = {self.id} OR player2 = {self.id} OR player3 = {self.id} OR player4 = {self.id}")

        sql.append("ORDER BY sequence AND gameID")

        sql.append(";")
        sql = " ".join(sql)

        self.retrievedInfo = self.performQuery(sql)

    def getShotsQuery(self, playType: list[str] = None):
        if self.emptyRetrivedInfo():
            self.getQuery()


        result = self.getResults()

        shotList = []
        #default arg, where we want all the shot events
        if not playType:
            playType = self.shotEvents

        for event in result:
            
            if event["playType"] in playType and int(event["player1"]) == self.id:
                shotList.append(event)

        return shotList

        
        

        
        