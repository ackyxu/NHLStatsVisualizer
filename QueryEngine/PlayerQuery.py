from .InfoQuery import InfoQuery
from .QueryEngine import QueryEngine


class PlayerQuery(InfoQuery):
    shotOnGoalEvents = ['SHOT','BLOCKED_SHOT','GOAL']
    def __init__(self, qe: QueryEngine, playerID = int) -> None:
        super().__init__(qe)
        self.playerID = playerID
        
    def getPlayerInfo(self, html = False) -> str:
        sql = f"SELECT * From Players WHERE id = {self.playerID}"
        results =  self.performQuery(sql)
        output = ""
        if html:
            br = "<br>"
        else:
            br = "\n"
        output += "Player Name:\t %s %s %s"%(results[0]["firstname"],results[0]["lastname"],br)
        output += "Player ID:\t %d %s"%(results[0]["id"],br)
        position = []
        if len(results) > 1:
            for result in results:
                if result["positionName"] != "Unknown":
                    position.append(result["positionName"])
            positionStr = " / ".join(position)
        else:
            positionStr = results[0]["positionName"]
        output += "Postion:\t %s"%positionStr

        return output
    
    def getPlayerShotPct(self) -> tuple[int,int,float]:
        sql =  (   "SELECT * "
                    +"From GamePlays "
                    +f"WHERE player1 = {self.playerID} ")
        
        additionSQL = []
        for shotType in self.shotOnGoalEvents:
             additionSQL.append(f"playType ='{shotType}' ")
        sql += "AND (" + " OR ".join(additionSQL) + ")"

        
        results =  self.performQuery(sql)
        totalShots = len(results)

        goals = 0
        for event in results:
            if event["playType"] == "GOAL": goals += 1


        return (totalShots, goals, goals/totalShots)


