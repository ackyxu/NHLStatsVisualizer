from .InfoQuery import InfoQuery
from .QueryEngine import QueryEngine


class PlayerQuery(InfoQuery):
    shotOnGoalEvents = ['SHOT','BLOCKED_SHOT','GOAL']
    def __init__(self, qe: QueryEngine, playerID:int, years: list[int]|None) -> None:
        super().__init__(qe)
        self.playerID = playerID
        self.years = years
        self.getQuery()

        
    def getPlayerInfo(self, html = False) -> tuple[str,int,str]:
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

        return (" ".join([results[0]["firstname"],results[0]["lastname"]]), self.playerID, positionStr)

    def getQuery(self):

        sql =  " ".join([   self.selectLine+" ,year",

                            "FROM Boxscores",

                            f"WHERE id = {self.playerID}",
                ])

        if self.years:
            yearsSQL = " "
            yearsSQL += "AND year IN ("
            yearSQL = []
            for year in self.years:
                yearSQL.append(str(year))
            yearsSQL = yearsSQL +  ",".join(yearSQL) + ")" 
            sql += yearsSQL 
        sql +=  " GROUP BY id,year;"  
        self.retrievedInfo =  self.performQuery(sql)
        self.additionalAgg()
        
    def getPlayerGoals(self) -> int:
        goals = 0
        if len(self.retrievedInfo) > 1:
            for line in self.retrievedInfo:
                goals += line["goals"]
        else:
            goals = self.retrievedInfo[0]["goals"]

        return goals

    def getPlayerShots(self) -> int:
        try: 
            self.emptyRetrivedInfo()
            shots = 0
            if len(self.retrievedInfo) > 1:
                for line in self.retrievedInfo:
                    shots += line["shots"]
            else:
                shots = self.retrievedInfo[0]["shots"]
            return shots
        except Exception as e:
            print(e)
            return 0
            
            
    
    def getPlayerShotPct(self) -> tuple[int,int,float]:

        # goals = self.getPlayerGoals()
        # totalShots = self.getPlayerShots()

        # print("Goals: %d"%goals)
        # print("Shots: %d"%totalShots)
        result = self.getResults()[0]
        goals = result["goals"]
        totalShots = result["shots"]
        pct = result["ShootingPct"]
        return (totalShots, goals, pct)



