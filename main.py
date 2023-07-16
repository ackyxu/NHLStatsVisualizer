import eel
from ShotVisualizer.ShotVisualizer import ShotVisualizer
from ShotVisualizer.ShotPctVisualizer import ShotPctVisualizer
from QueryEngine.QueryEngine import QueryEngine
from QueryEngine.PlayerQuery import PlayerQuery
import os
WD = ""
TEMPFOLDER = os.path.join(".","Temp")
HOST = "localhost"
PORT = "8000"
QE = None

def main():
    CreateRinkGraph()

@eel.expose
def CreateRinkGraph():
    rootpath = eel._get_real_path('FrontEnd')
    pq = PlayerQuery(QE,8480012)
    results = pq.performQuery("SELECT * From GamePlays WHERE player1 = 8480012")
    sv = ShotVisualizer(results)
    fig = sv.rinkPlot(sv.filterShotEvents(["GOAL"]),graphType="Heat")
    fig.savefig(os.path.join(rootpath,TEMPFOLDER,"rink.png"),bbox_inches='tight')
    return f'http://{HOST}:{PORT}/{TEMPFOLDER}/rink.png'

@eel.expose
def GetPlayerInfo():
        pq = PlayerQuery(QE,8480012)
        return pq.getPlayerInfo(html=True)

@eel.expose
def PlayerShotStats():
    rootpath = eel._get_real_path('FrontEnd')
    pq = PlayerQuery(QE,8480012)
    shotStats = pq.getPlayerShotPct()
    spv = ShotPctVisualizer(shotStats)
    fig = spv.piePlot()
    fig.savefig(os.path.join(rootpath,TEMPFOLDER,"pie.png"),bbox_inches='tight')
    return (shotStats,f'http://{HOST}:{PORT}/{TEMPFOLDER}/pie.png')
    

    
if __name__ == "__main__":
    # main()
    QE = QueryEngine(r"H:/database.db")
    eel.init('FrontEnd')
    eel.start('index.html')
    