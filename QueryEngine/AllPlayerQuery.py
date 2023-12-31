from QueryEngine.QueryEngine import QueryEngine
from QueryEngine.SummaryInfoQuery import SummaryInfoQuery
from .InfoQuery import InfoQuery


class AllPlayerQuery(SummaryInfoQuery):
    shotOnGoalEvents = ['SHOT','BLOCKED_SHOT','GOAL']
    def __init__(self, qe: QueryEngine, years: int|list[int]|None, positionType: str|None = None, positionName: str|None = None, by_year: bool = False) -> None:
        super().__init__(qe)
        self.years = years
        self.getQuery(positionName=positionName,positionType=positionType, by_year=by_year)


    def getQuery(self, positionType: str|None = None, positionName: str|None = None, by_year: bool = False):
        sql = [self.selectLine]
        if by_year:
            sql[0] =  sql[0]+",year"
        sql.append("FROM Boxscores")
        if self.years:
            if type(self.years) == list:
                yearsSQL = ["WHERE year IN ("]
                yearSQL = []
                for year in self.years:
                    yearSQL.append(str(year))
                yearsSQL.append(",".join(yearSQL))
                yearsSQL.append( ")" )
                
            else: #type(self.years) == int
                yearsSQL = [f"WHERE year={self.years}"]

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
        
        if by_year:
            sql.append("GROUP BY id,year")
        else:
            sql.append("GROUP BY id")

        sql.append("HAVING gp >= 20")
        sql.append(";")

        sql = " ".join(sql)
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
            
            
    
    def getSummaryShotPct(self) -> tuple[int,int,float]:

        goals = self.getPlayerGoals()
        totalShots = self.getPlayerShots()

        print("Goals: %d"%goals)
        print("Shots: %d"%totalShots)
        return (totalShots, goals, goals/totalShots)


