from QueryEngine.InfoQuery import InfoQuery
from QueryEngine.QueryEngine import QueryEngine


class PlayerBoxscoreQuery(InfoQuery):
    selectLine =    "SELECT id, gameID,goals, assists, (goals + assists) AS points,\
                    shots, hits, faceOffWins, \
                    faceOffTaken, takeaways, giveaways,\
                (   strftime('%s',evenTimeOnIce)-strftime('%s','00:00')) AS evenTOI, (strftime('%s',powerPlayTimeOnIce)-strftime('%s','00:00')) AS ppTOI, (strftime('%s',shortHandedTimeOnIce)-strftime('%s','00:00')) AS pkTOI"
    def __init__(self, qe: QueryEngine, id: int, year: int | list[int]):
        super().__init__(qe)
        self.id = id
        self.year = year


    def getQuery(self):
        sql =   [   self.selectLine,
                    "FROM Boxscores"
                ]

        if type(self.year) == int:
            sql.append(f"WHERE year = {self.year} ")
        else:
            sql.append(f"WHERE year IN {self.year}")

        sql.append(f"AND id = {self.id}")

        sql.append(";")

        sql = " ".join(sql)

        self.retrievedInfo = self.performQuery(sql)
        self.additionalAgg()

    
    def additionalAgg(self)-> None:
        if not self.emptyRetrivedInfo():
            for result in self.getResults():
                result["Total_Time_On_Ice"] = int(result["evenTOI"] or 0) + int(result["ppTOI"] or 0) + int(result["pkTOI"] or 0)
                result["Goals_Per_60"] = ((result["goals"]/(result["Total_Time_On_Ice"]/60)) * 60) if result["Total_Time_On_Ice"] else 0
                result["Points_Per_60"] = ((result["points"]/(result["Total_Time_On_Ice"]/60)) * 60) if result["Total_Time_On_Ice"] else 0