import eel
from ShotVisualizer.ShotVisualizer import ShotVisualizer
from ShotVisualizer.ShotPctVisualizer import ShotPctVisualizer
from QueryEngine.QueryEngine import QueryEngine
from QueryEngine.PlayerQuery import PlayerQuery
from QueryEngine.AllPlayerQuery import AllPlayerQuery
from ShotVisualizer.NormalDist import NormalDist
from QueryEngine.BoxscoreQuery import BoxscoreQuery
import os


WD = ""
TEMPFOLDER = os.path.join(".","Temp")
HOST = "localhost"
PORT = "8000"
QE = None
PQ = None
APQ = None

YEAR = None
ID = None

def main():
    CreateRinkGraph()

@eel.expose
def CreateRinkGraph():
    rootpath = eel._get_real_path('FrontEnd')
    # if PQ is None:
    #     PQ = PlayerQuery(QE,8480012,[2022])
    results = PQ.performQuery(f"SELECT * From GamePlays WHERE player1 = {ID} AND season='{YEAR}{YEAR+1}'")
    sv = ShotVisualizer(results)
    fig = sv.rinkPlot(sv.filterShotEvents(["GOAL"]),graphType="Heat")
    fig.savefig(os.path.join(rootpath,TEMPFOLDER,"rink.png"),bbox_inches='tight')
    return f'http://{HOST}:{PORT}/{TEMPFOLDER}/rink.png'

@eel.expose
def GetPlayerSeasonSummary():
    return PQ.getResults()

@eel.expose
def GetPlayerInfo():
    # if PQ is None:
    #     PQ = PlayerQuery(QE,8480012, [2022])
    return PQ.getPlayerInfo(html=True)

@eel.expose
def PlayerShotStats():
    rootpath = eel._get_real_path('FrontEnd')
    # if PQ is None: 
    #     PQ = PlayerQuery(QE,8480012, [2022])
    shotStats = PQ.getPlayerShotPct()
    spv = ShotPctVisualizer(shotStats)
    fig = spv.piePlot()
    fig.savefig(os.path.join(rootpath,TEMPFOLDER,"pie.png"),bbox_inches='tight')
    return (shotStats,f'http://{HOST}:{PORT}/{TEMPFOLDER}/pie.png')

@eel.expose
def NormalDistGraphs(field: str)->str:
    rootpath = eel._get_real_path('FrontEnd')
    # if APQ is None:
    #     APQ = AllPlayerQuery(QE,2022, positionType="Forward")
    # if PQ is None: 
    #     PQ = PlayerQuery(QE,8480012, [2022])
    nd = NormalDist()
    fig = nd.createPDFDist(field,APQ.getResults(), PQ.getResults()[0][field])
    fig.savefig(os.path.join(rootpath,TEMPFOLDER,"nd_%s_%d.png"%(field,ID)),bbox_inches='tight')
    return f'http://{HOST}:{PORT}/{TEMPFOLDER}/nd_{field}_{ID}.png'
        

@eel.expose
def queryYearsDB() -> list[int]:
    return BQ.queryYearsDB()

@eel.expose
def queryTeamsByYear(year:int) -> list[dict]:
    return BQ.queryTeamsByYear(year)


@eel.expose
def queryTeamRosterByYear(year:int, teamID:int) -> list[dict]:
    return BQ.queryTeamRosterByYear(year,teamID)
    
@eel.expose
def setPlayerYearID(year:int,id:int):
    global PQ,APQ,YEAR,ID
    YEAR = year
    ID = id



@eel.expose
def createFowardReportCard(year:int, id:int):
    global PQ,APQ,YEAR,ID
    YEAR = int(year)
    ID = int(id)
    PQ = PlayerQuery(QE,id,[year])
    APQ =  AllPlayerQuery(QE,year, positionType="Forward")
    eel.show("index.html")


    
if __name__ == "__main__":
    # main()
    QE = QueryEngine(r"H:/database.db")
    # PQ = PlayerQuery(QE,8480012,[2022])
    # APQ =  AllPlayerQuery(QE,2022, positionType="Forward")
    BQ = BoxscoreQuery(QE)
    eel.init('FrontEnd')
    eel.start('FowardSelect.html')
