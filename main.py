import eel
from ShotVisualizer.ShotVisualizer import ShotVisualizer
from ShotVisualizer.ShotPctVisualizer import ShotPctVisualizer
from QueryEngine.QueryEngine import QueryEngine
from QueryEngine.PlayerQuery import PlayerQuery
from QueryEngine.AllPlayerQuery import AllPlayerQuery
from ShotVisualizer.NormalDist import NormalDist
import os
WD = ""
TEMPFOLDER = os.path.join(".","Temp")
HOST = "localhost"
PORT = "8000"
QE = None
PQ = None
APQ = None

def main():
    CreateRinkGraph()

@eel.expose
def CreateRinkGraph():
    rootpath = eel._get_real_path('FrontEnd')
    # if PQ is None:
    #     PQ = PlayerQuery(QE,8480012,[2022])
    results = PQ.performQuery("SELECT * From GamePlays WHERE player1 = 8480012 AND season='20222023'")
    sv = ShotVisualizer(results)
    fig = sv.rinkPlot(sv.filterShotEvents(["GOAL"]),graphType="Heat")
    fig.savefig(os.path.join(rootpath,TEMPFOLDER,"rink.png"),bbox_inches='tight')
    return f'http://{HOST}:{PORT}/{TEMPFOLDER}/rink.png'

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
    fig.savefig(os.path.join(rootpath,TEMPFOLDER,"nd_%s_%d.png"%(field,8480012)),bbox_inches='tight')
    return f'http://{HOST}:{PORT}/{TEMPFOLDER}/nd_{field}_{8480012}.png'
        
    
if __name__ == "__main__":
    # main()
    QE = QueryEngine(r"H:/database.db")
    PQ = PlayerQuery(QE,8480012,[2022])
    APQ =  AllPlayerQuery(QE,2022, positionType="Forward")
    eel.init('FrontEnd')
    eel.start('index.html')
    