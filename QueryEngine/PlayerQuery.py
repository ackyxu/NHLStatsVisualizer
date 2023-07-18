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
    
    def getPlayerShotPct(self, years: list[int]|None = None) -> tuple[int,int,float]:
        sql =  (   "SELECT * "
                    +"From Boxscores "
                    +f"WHERE id = {self.playerID} ")
        
        # additionSQL = []
        # for shotType in self.shotOnGoalEvents:
        #      additionSQL.append(f"playType ='{shotType}' ")
        # sql += "AND (" + " OR ".join(additionSQL) + ")"

        if years:
            yearsSQL = "AND year IN ("
            yearSQL = []
            for year in years:
                yearSQL.append(str(year))
            yearsSQL = yearsSQL +  ",".join(yearSQL) + ")" 
        
            sql += yearsSQL   
        results =  self.performQuery(sql)

        totalShots = 0
        goals = 0

        for result in results:
            totalShots += 0 if result["shots"] == "" else int(result["shots"])
            goals += 0 if result["goals"] == "" else int(result["goals"])
      
        print("Goals: %d"%goals)
        print("Shots: %d"%totalShots)
        return (totalShots, goals, goals/totalShots)


