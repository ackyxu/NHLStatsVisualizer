from QueryEngine.QueryEngine import QueryEngine
from QueryEngine.SummaryInfoQuery import SummaryInfoQuery


class PlayerSeasonSummary(SummaryInfoQuery):

    def __init__(self, qe: QueryEngine, years: int|list[int]|None, positionType: str|None = None, positionName: str|None = None) -> None:
        super().__init__(qe)
        self.years = years
        self.getQuery(positionName=positionName,positionType=positionType)


    def getQuery(self, positionType: str|None = None, positionName: str|None = None):

        sql =  [self.selectLine+" ,year",
                    "FROM Boxscores",]

        if self.years:

            if type(self.years) == int:
                 yearsSQL = [f"WHERE year = {self.years}"]

            else:
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
            else:
                filterSQL=[f"id = {self.id}"]
        sql += filterSQL

        # sql.append("GROUP BY year;")
        
        sql = " ".join(sql)
        print(sql)
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
            
            
    
    def getQueryShotPct(self) -> tuple[int,int,float]:

        goals = self.getPlayerGoals()
        totalShots = self.getPlayerShots()

        print("Goals: %d"%goals)
        print("Shots: %d"%totalShots)
        return (totalShots, goals, goals/totalShots)


