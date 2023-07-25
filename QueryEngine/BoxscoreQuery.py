from QueryEngine.InfoQuery import InfoQuery
from .QueryEngine import QueryEngine
class BoxscoreQuery(InfoQuery):

    def __init__(self, qe: QueryEngine) -> None:
        super().__init__(qe)


    def queryYearsDB(self) -> list[int]:
        sql = " ".join([
                        "Select DISTINCT year",
                        "From Boxscores"
                        ])

        return [result["year"] for result in self.performQuery(sql)]

    def queryTeamsByYear(self, year:int) -> list[dict]:
        teamsSQL =" ".join(["SELECT locationName, teamName, id",
                            "FROM Teams", 
                            f"WHERE id in (SELECT DISTINCT teamID FROM Boxscores WHERE year = {year})",
                            "ORDER BY locationName"
                            ]) 
        return self.performQuery(teamsSQL)

    def queryTeamRosterByYear(self, year:int, teamID: int) -> list[dict]:
        
        teamRosterSQL =  " ".join(["SELECT DISTINCT Players.firstname, Players.lastname, Players.id",
                            "FROM Players", 
                            "JOIN Boxscores ON Players.id = Boxscores.id", 
                            f"WHERE Boxscores.year = {year} AND Boxscores.teamID ={teamID} AND positionType='Forward'",
                            "ORDER BY firstname"
                            ])


        return self.performQuery(teamRosterSQL)