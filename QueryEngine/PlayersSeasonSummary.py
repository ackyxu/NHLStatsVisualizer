from QueryEngine.QueryEngine import QueryEngine
from .InfoQuery import InfoQuery


class PlayerSeasonSummary(InfoQuery):
    shotOnGoalEvents = ['SHOT','BLOCKED_SHOT','GOAL']
    def __init__(self, qe: QueryEngine, years: list[int]|None, positionType: str|None = None, positionName: str|None = None) -> None:
        super().__init__(qe)
        self.years = years
        self.getQuery(positionName=positionName,positionType=positionType)


    def getQuery(self, positionType: str|None = None, positionName: str|None = None):

        sql =  [    "SELECT id, year,COUNT(id) AS gp, SUM(goals) AS goals, SUM(assists) AS assists, (SUM(goals) + SUM(assists)) AS points, SUM(shots) AS shots, SUM(hits) AS hits, SUM(faceOffWins) AS faceOffWins, \
                    SUM(faceOffTaken) AS faceOffTaken, SUM(takeaways) AS takeaways, SUM(giveaways) AS giveaways",

                    "FROM Boxscores",]

        if self.years:
            yearsSQL = ["WHERE year IN ("]
            yearSQL = []
            for year in self.years:
                yearSQL.append(str(year))
            yearsSQL.append(",".join(yearSQL))
            yearsSQL.append( ")" )
            sql += yearsSQL 

        
        if positionType and positionName:
            print("WARNING: Only one of positionType or positionName filter can be selected.  Defaulting to positionName")

        if positionName or positionType:
            if self.years:
                filterSQL = ["AND"]
            else:
                filterSQL = ["WHERE"]
            if positionName:
                filterSQL.append(f"id IN (SELECT id FROM Players WHERE positionName='{positionName}')")
            elif positionType:
                filterSQL.append(f"id IN (SELECT id FROM Players WHERE positionType='{positionType}')")
            sql += filterSQL

        sql.append("GROUP BY year;")
        
        sql = " ".join(sql)
        print(sql)
        self.retrievedInfo =  self.performQuery(sql)

        
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
            
            
    
    def getQueryShotPct(self) -> tuple[int,int,float]:

        goals = self.getPlayerGoals()
        totalShots = self.getPlayerShots()

        print("Goals: %d"%goals)
        print("Shots: %d"%totalShots)
        return (totalShots, goals, goals/totalShots)


