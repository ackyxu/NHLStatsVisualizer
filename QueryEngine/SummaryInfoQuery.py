from QueryEngine.InfoQuery import InfoQuery
from .QueryEngine import QueryEngine


class SummaryInfoQuery(InfoQuery):
    retrievedInfo = []
    SQLTemplate = ""
    selectLine =    "SELECT id, COUNT(evenTimeOnIce) AS gp, SUM(goals) AS goals, SUM(assists) AS assists, (SUM(goals) + SUM(assists)) AS points,\
                    SUM(shots) AS shots, SUM(hits) AS hits, SUM(faceOffWins) AS faceOffWins, \
                    SUM(faceOffTaken) AS faceOffTaken, SUM(takeaways) AS takeaways, SUM(giveaways) AS giveaways,\
                   SUM(strftime('%s',evenTimeOnIce)-strftime('%s','00:00')) AS evenTOI, SUM(strftime('%s',powerPlayTimeOnIce)-strftime('%s','00:00')) AS ppTOI, SUM(strftime('%s',shortHandedTimeOnIce)-strftime('%s','00:00')) AS pkTOI"


                    
    def __init__(self, qe: QueryEngine):
        super().__init__(qe)


    def additionalAgg(self)-> None:
        if not self.emptyRetrivedInfo():
            for result in self.getResults():
                result["GoalsPerGame"] = result["goals"]/result["gp"] if result["gp"] else 0
                result["PointsPerGame"] = result["points"]/result["gp"] if result["gp"] else 0
                result["ShootingPct"] = result["goals"]/result["shots"] if result["shots"] else 0
                
                result["Total_Time_On_Ice"] = int(result["evenTOI"] or 0) + int(result["ppTOI"] or 0) + int(result["pkTOI"] or 0)
                result["Avg_Time_On_Ice"] = (result["Total_Time_On_Ice"] / result["gp"]) if result["gp"] else 0 #"%d:%d"%(rawATOI//60,int(rawATOI % 60))
                result["Goals_Per_60"] = ((result["goals"]/(result["Total_Time_On_Ice"]/60)) * 60) if result["Total_Time_On_Ice"] else 0
                result["Points_Per_60"] = ((result["points"]/(result["Total_Time_On_Ice"]/60)) * 60) if result["Total_Time_On_Ice"] else 0
                


        